#!/usr/bin/env python3
"""
Integrated Protein Morphing Pipeline

This script performs three main tasks:
1. (Optional) Local interpolation (“local walk”) between two protein configurations
   using specified residue ranges. Each interpolated structure is refined using GROMACS.
   The refined files are saved with a prefix (default "localwalk_") and a numeric index.
2. The refined interpolated structures (or preexisting ones matching the pattern 
   "localwalk_*_refined.pdb") are loaded as the baseline pathway (“beads on a string”),
   and a CorrectionNet/NEB optimization pipeline is run to drive the pathway toward
   a low–energy transition. The training loop uses mixed precision and cyclic simulated
   annealing (heating/cooling cycles) for efficiency.
3. Finally, a separate GROMACS minimization pipeline is run on each final image.
   Energy data are extracted and plotted versus image number.

All key parameters (interpolation, CorrectionNet training, SA parameters, etc.) are
configurable via command-line flags.

Usage Examples:
  # Full pipeline with interpolation and chain-specific residues:
  python -m lwalkm --conf1 model_01A.pdb --conf2 model_01B.pdb \
    --interpolate --residues "61,62,78-91" --chain_residues "A:1-10,B:20-30" \
    --steps 5 --chains A,B --output_prefix localwalk \
    --pretrain_epochs 200 --sac_timesteps 50 \
    --sa_steps 1000 --sa_cycles 4 --sa_steps_per_cycle 300 --sa_T_high 450 --sa_T_low 40 --sa_update_frequency 3 \
    --lr 0.0003 --sigma 0.01 \
    --lbfgs_maxiter 3000 --lbfgs_disp --max_steps 50 --run_minimizer

  # Quick test run (0 training epochs):
  python -m lwalkm --conf1 model_01A.pdb --conf2 model_01B.pdb \
    --interpolate --residues "1-10" --steps 2 --pretrain_epochs 0 --sac_timesteps 0 --run_minimizer
"""

import argparse
import os
import sys
import subprocess
import shutil
import logging
import time
import random
import math
import copy
import glob
import re
from typing import List, Tuple, Optional, Dict, Any

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import scipy.optimize

# ------------------------------
# Bio.PDB Imports (for interpolation)
from Bio.PDB import PDBParser, PDBIO, Superimposer

# ------------------------------
# OpenMM and Related Imports
from openmm.app import PDBFile, Simulation, ForceField, Topology, PDBFile as PDBWriter
from openmm import System, CustomBondForce, LangevinIntegrator, LocalEnergyMinimizer, Platform, Vec3
from openmm.unit import kelvin, picosecond, nanometer, kilojoule_per_mole

# ------------------------------
# Gymnasium and Stable-Baselines3 Imports (for NEB optimization)
import gymnasium as gym
from stable_baselines3 import SAC
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv

# -----------------------------------------------------------------------------
# Logging and Global Settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
gmx_cmd = "gmx"  # Adjust if necessary
output_base = "gmx_refine"
if not os.path.exists(output_base):
    os.makedirs(output_base)

MINIM_MDP_CONTENT = """; minim.mdp - used as input into grompp to generate em.tpr
integrator  = steep         
emtol       = 1000.0       
emstep      = 0.0001       
nsteps      = 50000         

nstlist         = 1         
cutoff-scheme   = Verlet    
ns_type         = grid      
coulombtype     = PME       
rcoulomb        = 1.0       
rvdw            = 1.0       
pbc             = xyz       
"""

# -----------------------------------------------------------------------------
# Helper Functions for Running Commands and Verifying Files
def run_command(cmd: str, cwd: str) -> None:
    logging.info(f"Running command: {cmd} (in {cwd})")
    try:
        result = subprocess.run(cmd, shell=True, check=True, cwd=cwd,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e.stderr}")
        raise

def verify_input_file(filepath: str) -> None:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: {filepath}")
    logging.info(f"Verified input file: {filepath}")

# -----------------------------------------------------------------------------
# GROMACS Refinement Functions
def remove_solvent_and_ions(input_pdb: str, output_pdb: str, remove_set: set = {"SOL", "NA", "CL"}) -> None:
    with open(input_pdb, 'r') as fin, open(output_pdb, 'w') as fout:
        for line in fin:
            if line.startswith("ATOM"):
                resname = line[17:20].strip()
                if resname in remove_set:
                    continue
            fout.write(line)
    logging.info(f"Solvent/ions removed: {output_pdb}")

def run_gmx_refinement(label: str, input_file: str) -> str:
    verify_input_file(input_file)
    folder = os.path.join(output_base, label)
    os.makedirs(folder, exist_ok=True)
    src = os.path.abspath(input_file)
    dest_filename = f"{label}_structure.pdb"
    dest = os.path.join(folder, dest_filename)
    shutil.copy(src, dest)
    logging.info(f"{label}: Copied {src} to {dest}")
    run_command(f"{gmx_cmd} pdb2gmx -f {dest_filename} -o processed.gro -water tip3p -ff amber99sb -ignh", folder)
    run_command(f"{gmx_cmd} editconf -f processed.gro -o newbox.gro -c -d 1.0 -bt cubic", folder)
    minim_mdp_file = os.path.join(folder, "minim.mdp")
    with open(minim_mdp_file, "w") as f:
        f.write(MINIM_MDP_CONTENT)
    logging.info(f"{label}: minim.mdp created")
    run_command(f"{gmx_cmd} grompp -f minim.mdp -c newbox.gro -p topol.top -o em.tpr -maxwarn 10", folder)
    run_command(f"{gmx_cmd} mdrun -v -deffnm em -c final_em.pdb", folder)
    final_em = os.path.join(folder, "final_em.pdb")
    output_refined = f"{label}_refined.pdb"
    remove_solvent_and_ions(final_em, output_refined)
    logging.info(f"{label}: Final refined structure saved as {output_refined}")
    return output_refined

# -----------------------------------------------------------------------------
# Interpolation Functions
def parse_residues_input(residue_input: str) -> List[int]:
    if os.path.isfile(residue_input):
        with open(residue_input, 'r') as f:
            residue_str = f.read().strip()
    else:
        residue_str = residue_input
    residues = set()
    for token in residue_str.split(','):
        token = token.strip()
        if not token:
            continue
        if '-' in token:
            try:
                start_str, end_str = token.split('-')
                start = int(start_str.strip())
                end = int(end_str.strip())
                for r in range(start, end + 1):
                    residues.add(r)
            except ValueError:
                logging.warning(f"Unable to parse range token '{token}'. Skipping.")
        else:
            try:
                residues.add(int(token))
            except ValueError:
                logging.warning(f"Unable to parse residue token '{token}'. Skipping.")
    return sorted(residues)

def parse_chain_residues(chain_residues_input: str) -> Dict[str, List[int]]:
    """
    Parse a string of chain-specific residues.
    Format: "A:1-10,B:20,22-25" becomes {"A": [1,2,...,10], "B": [20,22,23,24,25]}
    """
    chain_dict = {}
    for part in chain_residues_input.split(','):
        part = part.strip()
        if not part:
            continue
        try:
            chain_id, res_str = part.split(':')
            res_list = parse_residues_input(res_str)
            chain_dict[chain_id.strip()] = res_list
        except Exception as e:
            logging.warning(f"Unable to parse chain-specific residue token '{part}': {e}")
    return chain_dict

def get_common_chains(modelA, modelB, chains_arg: Optional[str]=None) -> List[str]:
    if chains_arg:
        chains_requested = {ch.strip() for ch in chains_arg.split(',') if ch.strip()}
        chains_common = {ch.id for ch in modelA}.intersection({ch.id for ch in modelB})
        chains = sorted(ch for ch in chains_requested if ch in chains_common)
    else:
        chains = sorted({ch.id for ch in modelA}.intersection({ch.id for ch in modelB}))
    if not chains:
        logging.warning("No common chains found; defaulting to ['A'].")
        chains = ["A"]
    return chains

def global_superimpose(structA, structB):
    modelA = structA[0]
    modelB = structB[0]
    fixed_atoms = []
    moving_atoms = []
    for chainA in modelA:
        chain_id = chainA.id if chainA.id.strip() else "A"
        if chain_id not in {ch.id for ch in modelB}:
            continue
        chainB = None
        for ch in modelB:
            if ch.id == chain_id:
                chainB = ch
                break
        if chainB is None:
            chainB = list(modelB.get_chains())[0]
        for resA in chainA:
            if resA.id[0] != " ":
                continue
            if "CA" not in resA:
                continue
            try:
                resB = chainB[resA.id]
            except KeyError:
                continue
            if "CA" not in resB:
                continue
            fixed_atoms.append(resA["CA"])
            moving_atoms.append(resB["CA"])
    if fixed_atoms and moving_atoms:
        sup = Superimposer()
        sup.set_atoms(fixed_atoms, moving_atoms)
        all_moving = list(modelB.get_atoms())
        sup.apply(all_moving)
        logging.info(f"Global superimposition RMSD: {sup.rms:.3f} Å")
    else:
        logging.warning("No common CA atoms found for superimposition.")
    return structA, structB

def interpolate_residues(structA, structB, residue_numbers: List[int], steps: int, chains: List[str],
                         chain_residues: Optional[Dict[str, List[int]]] = None) -> List:
    """
    For each chain in 'chains', if chain_residues is provided and contains the chain,
    use the chain-specific list; otherwise, use the global residue_numbers.
    """
    interpolated_structs = []
    modelA = structA[0]
    modelB = structB[0]
    for step in range(steps + 1):
        alpha = step / steps
        new_struct = copy.deepcopy(structA)
        new_model = new_struct[0]
        for chain_id in chains:
            if chain_id not in new_model or chain_id not in modelB:
                continue
            new_chain = new_model[chain_id]
            chainB = modelB[chain_id]
            res_list = chain_residues.get(chain_id) if chain_residues and chain_id in chain_residues else residue_numbers
            for res in new_chain:
                if res.id[0] != " ":
                    continue
                resnum = res.id[1]
                if resnum in res_list:
                    try:
                        resB = chainB[res.id]
                    except KeyError:
                        continue
                    for atom in res:
                        if atom.name in resB:
                            coordA = atom.get_coord()
                            coordB = resB[atom.name].get_coord()
                            new_coord = coordA + alpha * (coordB - coordA)
                            atom.set_coord(new_coord)
        interpolated_structs.append(new_struct)
    return interpolated_structs

def compute_region_rmsd(struct1, struct2, residue_numbers: List[int], chains: List[str]) -> Optional[float]:
    model1 = struct1[0]
    model2 = struct2[0]
    coords1 = []
    coords2 = []
    for chain_id in chains:
        if chain_id not in model1 or chain_id not in model2:
            continue
        chain1 = model1[chain_id]
        chain2 = model2[chain_id]
        for res in chain1:
            if res.id[0] != " ":
                continue
            if res.id[1] in residue_numbers:
                try:
                    res2 = chain2[res.id]
                except KeyError:
                    continue
                for atom in res:
                    if atom.name in res2:
                        coords1.append(atom.get_coord())
                        coords2.append(res2[atom.name].get_coord())
    coords1 = np.array(coords1)
    coords2 = np.array(coords2)
    if len(coords1) == 0:
        return None
    diff = coords1 - coords2
    rmsd = np.sqrt(np.sum(diff * diff) / len(coords1))
    return rmsd

def perform_local_interpolation(pdb_file_A: str, pdb_file_B: str,
                                residues: str, steps: int,
                                output_prefix: str, chains_arg: Optional[str],
                                chain_residues_str: Optional[str] = None) -> List[str]:
    global_residues = parse_residues_input(residues)
    chain_residues = parse_chain_residues(chain_residues_str) if chain_residues_str else None
    logging.info(f"Global residues: {global_residues}")
    if chain_residues:
        logging.info(f"Chain-specific residues: {chain_residues}")
    
    pdb_parser = PDBParser(QUIET=True)
    structA = pdb_parser.get_structure("ProteinA", pdb_file_A)
    structB = pdb_parser.get_structure("ProteinB", pdb_file_B)
    
    modelA = structA[0]
    modelB = structB[0]
    chains = get_common_chains(modelA, modelB, chains_arg)
    logging.info(f"Processing chains: {', '.join(chains)}")
    
    structA, structB = global_superimpose(structA, structB)
    interpolated = interpolate_residues(structA, structB, global_residues, steps, chains, chain_residues)
    
    interp_files = []
    io = PDBIO()
    for i, s in enumerate(interpolated):
        filename = f"{output_prefix}_{i}.pdb"
        io.set_structure(s)
        io.save(filename)
        logging.info(f"Saved interpolation step {i} to {filename}")
        interp_files.append(filename)
    
    rmsd = compute_region_rmsd(interpolated[-1], structB, global_residues, chains)
    if rmsd is not None:
        logging.info(f"Final region RMSD: {rmsd:.3f} Å")
    else:
        logging.info("Could not compute region RMSD.")
    
    refined_files = []
    for file in interp_files:
        label = os.path.splitext(os.path.basename(file))[0]
        refined = run_gmx_refinement(label, file)
        refined_files.append(refined)
    
    logging.info("Local interpolation and refinement complete.")
    logging.info(f"Refined files: {refined_files}")
    return sorted(refined_files, key=lambda x: int(re.findall(r'\d+', x)[0]))

# -----------------------------------------------------------------------------
# CorrectionNet and NEB Pipeline
input_A: Optional[str] = None
input_B: Optional[str] = None
N_IMAGES: int = 16
PRETRAIN_EPOCHS: int = 200
SAC_TIMESTEPS: int = 50
SA_STEPS: int = 1000
LBFGS_MAXITER: int = 5000
LBFGS_DISP: bool = False
MAX_STEPS: int = 50

def set_random_seed_pipeline(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    logging.info(f"Random seed set to {seed}")

set_random_seed_pipeline(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if device.type == "cpu":
    logging.warning("CUDA device not found. Performance will be slow!")
else:
    logging.info(f"Using device: {device}")

def main_prepare() -> None:
    logging.info("Starting endpoint refinement with GROMACS...")
    run_gmx_refinement("A", input_A)
    run_gmx_refinement("B", input_B)
    logging.info("Endpoint refinement complete.")

def get_angle_triplets(bonds_list: List[Tuple[int, int]], n_atoms: int) -> List[Tuple[int, int, int]]:
    neighbors = {i: set() for i in range(n_atoms)}
    for i, j in bonds_list:
        neighbors[i].add(j)
        neighbors[j].add(i)
    triplets = []
    for j in range(n_atoms):
        neigh = list(neighbors[j])
        for a in range(len(neigh)):
            for b in range(a+1, len(neigh)):
                triplets.append((neigh[a], j, neigh[b]))
    return triplets

def get_dihedral_quadruplets(bonds_list: List[Tuple[int, int]], n_atoms: int) -> List[Tuple[int, int, int, int]]:
    neighbors = {i: set() for i in range(n_atoms)}
    for i, j in bonds_list:
        neighbors[i].add(j)
        neighbors[j].add(i)
    quadruplets = []
    for j, k in bonds_list:
        for i in neighbors[j]:
            if i == k:
                continue
            for l in neighbors[k]:
                if l == j:
                    continue
                quadruplets.append((i, j, k, l))
    return quadruplets

def compute_bond_angles(positions: torch.Tensor, angle_triplets: List[Tuple[int, int, int]]) -> torch.Tensor:
    angles = []
    for (i, j, k) in angle_triplets:
        v1 = positions[:, i, :] - positions[:, j, :]
        v2 = positions[:, k, :] - positions[:, j, :]
        dot_prod = (v1 * v2).sum(dim=1)
        norm1 = torch.norm(v1, dim=1)
        norm2 = torch.norm(v2, dim=1)
        cos_angle = dot_prod / (norm1 * norm2 + 1e-8)
        cos_angle = torch.clamp(cos_angle, -1.0, 1.0)
        angle = torch.acos(cos_angle)
        angles.append(angle)
    return torch.stack(angles, dim=1)

def compute_dihedrals(positions: torch.Tensor, dihedral_quadruplets: List[Tuple[int, int, int, int]]) -> torch.Tensor:
    dihedrals = []
    for (i, j, k, l) in dihedral_quadruplets:
        b1 = positions[:, j, :] - positions[:, i, :]
        b2 = positions[:, k, :] - positions[:, j, :]
        b3 = positions[:, l, :] - positions[:, k, :]
        b2_norm = b2 / (torch.norm(b2, dim=1, keepdim=True) + 1e-8)
        n1 = torch.cross(b1, b2, dim=1)
        n2 = torch.cross(b2, b3, dim=1)
        m1 = torch.cross(n1, b2_norm, dim=1)
        x = (n1 * n2).sum(dim=1)
        y = (m1 * n2).sum(dim=1)
        dihedral = -torch.atan2(y, x)
        dihedrals.append(dihedral)
    return torch.stack(dihedrals, dim=1)

def compute_ideal_geometries(positions: torch.Tensor, angle_triplets: List[Tuple[int, int, int]],
                             dihedral_quadruplets: List[Tuple[int, int, int, int]]) -> Tuple[torch.Tensor, torch.Tensor]:
    positions = positions.unsqueeze(0)
    ideal_angles = compute_bond_angles(positions, angle_triplets)[0]
    ideal_dihedrals = compute_dihedrals(positions, dihedral_quadruplets)[0]
    return ideal_angles, ideal_dihedrals

def compute_smoothness_loss(path: torch.Tensor) -> torch.Tensor:
    diffs = path[1:] - path[:-1]
    loss = torch.sum(diffs ** 2) / (path.shape[0] - 1)
    return loss

# Neural Network Components
class ResidualBlock(nn.Module):
    def __init__(self, hidden_dim: int):
        super(ResidualBlock, self).__init__()
        self.linear1 = nn.Linear(hidden_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_dim, hidden_dim)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        out += identity
        return self.relu(out)

class GraphMessagePassing(nn.Module):
    def __init__(self, n_atoms: int, hidden_dim: int = 128, n_iters: int = 2):
        super(GraphMessagePassing, self).__init__()
        self.n_iters = n_iters
        self.msg_linear = nn.Linear(3, hidden_dim)
        self.update_linear = nn.Linear(hidden_dim, 3)
    
    def forward(self, positions: torch.Tensor, bonds: List[Tuple[int, int]]) -> torch.Tensor:
        batch, n_atoms, _ = positions.shape
        h = positions
        adj_list = [[] for _ in range(n_atoms)]
        for i, j in bonds:
            adj_list[i].append(j)
            adj_list[j].append(i)
        for _ in range(self.n_iters):
            msgs = torch.zeros(batch, n_atoms, 128, device=positions.device)
            for atom in range(n_atoms):
                if len(adj_list[atom]) > 0:
                    neighbor_feats = h[:, adj_list[atom], :]
                    neighbor_msgs = self.msg_linear(neighbor_feats)
                    msgs[:, atom, :] = neighbor_msgs.mean(dim=1)
            h = h + self.update_linear(msgs)
        return h

class DualBranchCorrectionNet(nn.Module):
    def __init__(self, n_atoms: int):
        super(DualBranchCorrectionNet, self).__init__()
        self.standard_branch = nn.Sequential(
            nn.Linear(1, 256),
            nn.ReLU(),
            nn.Dropout(0.1),
            ResidualBlock(256),
            ResidualBlock(256),
            nn.Linear(256, n_atoms * 3)
        )
        self.graph_branch = GraphMessagePassing(n_atoms, hidden_dim=128, n_iters=2)
        self.graph_out = nn.Linear(3, 3)
    
    def forward(self, alpha: torch.Tensor, baseline_positions: torch.Tensor, bonds: List[Tuple[int, int]]) -> torch.Tensor:
        standard_out = self.standard_branch(alpha)
        standard_out = standard_out.view(-1, standard_out.shape[-1] // 3, 3)
        graph_features = self.graph_branch(baseline_positions, bonds)
        graph_out = self.graph_out(graph_features)
        correction = standard_out + graph_out
        return correction

# -----------------------------------------------------------------------------
# Cyclic Simulated Annealing Refinement
def cyclic_simulated_annealing_refinement(candidate_positions: np.ndarray, integrator, simulation,
                                          cycles: int, steps_per_cycle: int,
                                          T_high: float, T_low: float) -> float:
    best_energy = float('inf')
    best_positions = candidate_positions.copy()
    for cycle in range(cycles):
        decay_rate = np.log(T_low / T_high) / steps_per_cycle
        for step in range(steps_per_cycle):
            new_T = T_high * math.exp(decay_rate * step)
            integrator.setTemperature(new_T * kelvin)
            simulation.step(10)
        LocalEnergyMinimizer.minimize(simulation.context)
        state = simulation.context.getState(getPositions=True, getEnergy=True)
        energy = state.getPotentialEnergy().value_in_unit(kilojoule_per_mole)
        if energy < best_energy:
            best_energy = energy
            best_positions = state.getPositions(asNumpy=True)
        simulation.context.setPositions(best_positions)
        logging.info(f"Cycle {cycle+1}/{cycles} completed with energy {energy:.2f} kJ/mol")
    return best_energy

# -----------------------------------------------------------------------------
# Main Pipeline Run Function (CorrectionNet/NEB)
def main_run() -> None:
    logging.info("Loading endpoints from A_refined.pdb and B_refined.pdb...")
    pdbA = PDBFile("A_refined.pdb")
    pdbB = PDBFile("B_refined.pdb")
    topology: Topology = pdbA.topology
    positions_A = pdbA.getPositions()
    positions_B = pdbB.getPositions()
    n_atoms = topology.getNumAtoms()
    logging.info(f"Topology has {n_atoms} atoms.")
    
    uA = np.array([[p.x, p.y, p.z] for p in positions_A])
    uB = np.array([[p.x, p.y, p.z] for p in positions_B])
    
    bonds_list = [(bond[0].index, bond[1].index) for bond in topology.bonds()]
    ref_bond_lengths = [0.5 * (np.linalg.norm(uA[i]-uA[j]) + np.linalg.norm(uB[i]-uB[j]))
                        for i, j in bonds_list]
    bonds_tensor = torch.tensor(bonds_list, dtype=torch.long, device=device)
    ref_bond_tensor = torch.tensor(ref_bond_lengths, dtype=torch.float32, device=device)
    lambda_geom = 100.0

    angle_triplets = get_angle_triplets(bonds_list, n_atoms)
    dihedral_quadruplets = get_dihedral_quadruplets(bonds_list, n_atoms)
    logging.info(f"Found {len(angle_triplets)} angle and {len(dihedral_quadruplets)} dihedral constraints.")

    ideal_angles, ideal_dihedrals = compute_ideal_geometries(
        torch.tensor(uA, device=device, dtype=torch.float32),
        angle_triplets, dihedral_quadruplets
    )
    max_triplets = 500
    max_dihedrals = 500
    baseline_tensor_single = torch.tensor(uA, device=device, dtype=torch.float32)

    def filter_angle_triplets(baseline, angle_triplets, ideal_angles, K):
        baseline = baseline.unsqueeze(0)
        baseline_angles = compute_bond_angles(baseline, angle_triplets)[0]
        errors = torch.abs(baseline_angles - ideal_angles)
        topk = torch.topk(errors, K, largest=True)
        filtered_triplets = [angle_triplets[i] for i in topk.indices.tolist()]
        filtered_ideal_angles = ideal_angles[topk.indices]
        return filtered_triplets, filtered_ideal_angles

    def filter_dihedral_quadruplets(baseline, dihedral_quadruplets, ideal_dihedrals, K):
        baseline = baseline.unsqueeze(0)
        baseline_dihedrals = compute_dihedrals(baseline, dihedral_quadruplets)[0]
        errors = torch.abs(baseline_dihedrals - ideal_dihedrals)
        topk = torch.topk(errors, K, largest=True)
        filtered_quadruplets = [dihedral_quadruplets[i] for i in topk.indices.tolist()]
        filtered_ideal_dihedrals = ideal_dihedrals[topk.indices]
        return filtered_quadruplets, filtered_ideal_dihedrals

    filtered_angle_triplets, filtered_ideal_angles = filter_angle_triplets(
        baseline_tensor_single, angle_triplets, ideal_angles, max_triplets)
    filtered_dihedral_quadruplets, filtered_ideal_dihedrals = filter_dihedral_quadruplets(
        baseline_tensor_single, dihedral_quadruplets, ideal_dihedrals, max_dihedrals)
    logging.info(f"Using {len(filtered_angle_triplets)} angle and {len(filtered_dihedral_quadruplets)} dihedral constraints.")

    box = topology.getPeriodicBoxVectors()
    if box is None or all(b == Vec3(0,0,0) for b in box):
        logging.info("No valid box vectors; setting default cube.")
        dummy_box = [Vec3(100,0,0)*nanometer, Vec3(0,100,0)*nanometer, Vec3(0,0,100)*nanometer]
        topology.setPeriodicBoxVectors(dummy_box)
    
    forcefield = ForceField('amber14-all.xml')
    system_full = forcefield.createSystem(topology, constraints="HBonds", rigidWater=True)
    logging.info("Created full–atom system.")
    
    # Load refined interpolated structures as baseline pathway.
    localwalk_files = sorted(glob.glob("localwalk_*_refined.pdb"), key=lambda x: int(re.findall(r'\d+', x)[0]))
    if len(localwalk_files) == 0:
        raise ValueError("No refined interpolated files found matching 'localwalk_*_refined.pdb'")
    N_IMAGES = len(localwalk_files)
    logging.info(f"Found {N_IMAGES} refined interpolated structures: {localwalk_files}")
    baseline_list = []
    for pdb_file in localwalk_files:
        pdb_local = PDBFile(pdb_file)
        pos_local = pdb_local.getPositions()
        pos_arr = np.array([[p.x, p.y, p.z] for p in pos_local])
        baseline_list.append(pos_arr)
    baseline_path = np.stack(baseline_list, axis=0)
    baseline_tensor = torch.tensor(baseline_path, dtype=torch.float32, device=device)
    alphas_tensor = torch.zeros((N_IMAGES, 1), dtype=torch.float32, device=device)
    baseline_positions_tensor = baseline_tensor

    correction_net = DualBranchCorrectionNet(n_atoms).to(device)
    optimizer = optim.Adam(correction_net.parameters(), lr=args.lr)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=20, factor=0.5)
    
    def replicate_system(system: System, N_images: int) -> Tuple[System, List[int]]:
        combined = System()
        offsets = []
        n = system.getNumParticles()
        for _ in range(N_images):
            offsets.append(combined.getNumParticles())
            for j in range(n):
                combined.addParticle(system.getParticleMass(j))
        return combined, offsets

    combined_system, offsets = replicate_system(system_full, N_IMAGES)
    neb_force = CustomBondForce("0.5*k*(r - r0)^2")
    neb_force.addPerBondParameter("r0")
    neb_force.addGlobalParameter("k", 1000 * kilojoule_per_mole / (nanometer**2))
    for i in range(N_IMAGES-1):
        for j in range(n_atoms):
            atom1 = offsets[i] + j
            atom2 = offsets[i+1] + j
            r0_val = np.linalg.norm(uA[j]-uB[j])/(N_IMAGES-1)
            neb_force.addBond(atom1, atom2, [r0_val])
    combined_system.addForce(neb_force)
    
    def build_combined_positions(path_np: np.ndarray) -> np.ndarray:
        combined = []
        for i in range(path_np.shape[0]):
            for j in range(n_atoms):
                combined.append(path_np[i, j])
        return np.array(combined) * nanometer
    
    integrator = LangevinIntegrator(300*kelvin, 1.0/picosecond, 0.002*picosecond)
    available_platforms = [Platform.getPlatform(i).getName() for i in range(Platform.getNumPlatforms())]
    if "CUDA" in available_platforms:
        platform = Platform.getPlatformByName('CUDA')
        logging.info("Using CUDA platform for OpenMM simulation.")
    else:
        platform = Platform.getPlatformByName('Reference')
        logging.info("Using Reference platform for OpenMM simulation.")
    simulation = Simulation(topology, combined_system, integrator, platform)
    simulation.context.setPeriodicBoxVectors(*topology.getPeriodicBoxVectors())
    
    def simulated_annealing_update(candidate_positions: np.ndarray, sa_update_frequency: int, epoch: int, last_energy: Optional[float]) -> float:
        if epoch % sa_update_frequency == 0:
            simulation.context.setPositions(candidate_positions)
            LocalEnergyMinimizer.minimize(simulation.context)
            refined_energy = cyclic_simulated_annealing_refinement(candidate_positions, integrator, simulation,
                                                                   cycles=args.sa_cycles,
                                                                   steps_per_cycle=args.sa_steps_per_cycle,
                                                                   T_high=args.sa_T_high,
                                                                   T_low=args.sa_T_low)
            return refined_energy
        else:
            return last_energy if last_energy is not None else 0.0

    logging.info("Starting CorrectionNet pre-training...")
    n_pretrain = PRETRAIN_EPOCHS
    baseline_value: Optional[float] = None
    sigma = args.sigma
    const_log = torch.tensor(sigma * math.sqrt(2 * math.pi), dtype=torch.float32, device=device)
    energy_history: List[float] = []
    start_time = time.time()
    lambda_smooth = 50
    sa_update_frequency = args.sa_update_frequency
    last_refined_energy = None

    scaler = torch.cuda.amp.GradScaler() if device.type == "cuda" else None
    ideal_angles_exp = ideal_angles.unsqueeze(0)
    ideal_dihedrals_exp = ideal_dihedrals.unsqueeze(0)

    for epoch in range(n_pretrain):
        optimizer.zero_grad()
        with torch.amp.autocast(device_type='cuda', enabled=(scaler is not None)):
            sampled_correction = correction_net(alphas_tensor, baseline_positions_tensor, bonds_list)
            noise = sigma * torch.randn_like(sampled_correction)
            sampled_correction_noisy = sampled_correction + noise
            bc_penalty = torch.norm(sampled_correction_noisy[0])**2 + torch.norm(sampled_correction_noisy[-1])**2
            baseline_plus = baseline_tensor + sampled_correction_noisy
            pos1 = baseline_plus[:, bonds_tensor[:, 0], :]
            pos2 = baseline_plus[:, bonds_tensor[:, 1], :]
            diff = pos1 - pos2
            d = torch.norm(diff, dim=2)
            geom_penalty = torch.sum((d - ref_bond_tensor.unsqueeze(0))**2)
            angle_pred = compute_bond_angles(baseline_plus, filtered_angle_triplets)
            dihedral_pred = compute_dihedrals(baseline_plus, filtered_dihedral_quadruplets)
            angle_loss = nn.MSELoss()(angle_pred, ideal_angles_exp.expand_as(angle_pred)) / len(filtered_angle_triplets)
            dihedral_loss = nn.MSELoss()(dihedral_pred, ideal_dihedrals_exp.expand_as(dihedral_pred)) / len(filtered_dihedral_quadruplets)
            smoothness_loss = compute_smoothness_loss(baseline_plus)
            def build_combined_positions(path_np: np.ndarray) -> np.ndarray:
                combined = []
                for i in range(path_np.shape[0]):
                    for j in range(n_atoms):
                        combined.append(path_np[i, j])
                return np.array(combined) * nanometer
            candidate_positions = build_combined_positions(baseline_path + sampled_correction_noisy.detach().cpu().numpy())
            refined_energy = simulated_annealing_update(candidate_positions, sa_update_frequency, epoch, last_refined_energy)
            last_refined_energy = refined_energy
            energy = refined_energy
            reward = -energy
            energy_history.append(energy)
            baseline_value = reward if baseline_value is None else 0.9 * baseline_value + 0.1 * reward
            advantage = reward - baseline_value
            log_probs = -0.5 * ((noise/sigma)**2) - torch.log(const_log)
            log_prob = torch.sum(log_probs)
            loss = (-advantage * log_prob + 1000 * bc_penalty + lambda_geom * geom_penalty +
                    50 * angle_loss + 50 * dihedral_loss + lambda_smooth * smoothness_loss)
        if scaler is not None:
            scaler.scale(loss).backward()
            torch.nn.utils.clip_grad_norm_(correction_net.parameters(), max_norm=5.0)
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
            torch.nn.utils.clip_grad_norm_(correction_net.parameters(), max_norm=5.0)
            optimizer.step()
        scheduler.step(loss)
        if epoch % 100 == 0:
            logging.info(f"[Pretrain] Epoch {epoch:5d}, Energy: {energy:.2f} kJ/mol, Loss: {loss.item():.4f}")
    elapsed = time.time() - start_time
    logging.info(f"Pre-training complete in {elapsed:.1f} seconds.")
    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(n_pretrain), energy_history, label="Energy")
    plt.xlabel("Epoch")
    plt.ylabel("Energy (kJ/mol)")
    plt.title("CorrectionNet Pre-training Energy History")
    plt.grid(True)
    plt.legend()
    plt.savefig("pretrain_energy_history.png")
    plt.close()
    final_correction = sampled_correction_noisy.detach().cpu().numpy()
    baseline_path = baseline_path + final_correction
    logging.info("Baseline path updated with learned corrections.")

    bonds_arr = np.array(bonds_list)
    ref_bond_array = ref_bond_tensor.cpu().numpy()
    
    class NEBMorphingEnv(gym.Env):
        metadata = {'render.modes': ['human']}
        def __init__(self, baseline_path: np.ndarray, topology: Topology, combined_system: System, offsets: List[int],
                     integrator: LangevinIntegrator, simulation: Simulation, n_atoms: int, N_images: int,
                     lambda_geom: float, bonds_arr: np.ndarray, ref_bond_array: np.ndarray,
                     T_initial: float = 300, T_final: float = 50, n_steps: int = SA_STEPS, max_steps: int = MAX_STEPS):
            super(NEBMorphingEnv, self).__init__()
            self.baseline_path = baseline_path
            with torch.no_grad():
                self.current_correction = correction_net(alphas_tensor, baseline_positions_tensor, bonds_list).detach().cpu().numpy()
            self.topology = topology
            self.combined_system = combined_system
            self.offsets = offsets
            self.integrator = integrator
            self.simulation = simulation
            self.n_atoms = n_atoms
            self.N_images = N_images
            self.lambda_geom = lambda_geom
            self.bonds_arr = bonds_arr
            self.ref_bond_array = ref_bond_array
            self.T_initial = T_initial
            self.T_final = T_final
            self.n_steps = n_steps
            self.max_steps = max_steps
            self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf,
                                                     shape=(N_images * n_atoms * 3,), dtype=np.float32)
            self.action_space = gym.spaces.Box(low=-0.1, high=0.1,
                                               shape=(N_images * n_atoms * 3,), dtype=np.float32)
            self.current_path = self.baseline_path + self.current_correction
            self.current_energy = self.evaluate_current_energy()
            self.step_count = 0
        
        def build_combined_positions(self, path_np: np.ndarray) -> np.ndarray:
            combined = []
            for i in range(path_np.shape[0]):
                for j in range(self.n_atoms):
                    combined.append(path_np[i, j])
            return np.array(combined)*nanometer
        
        def evaluate_current_energy(self) -> float:
            candidate_positions = self.build_combined_positions(self.current_path)
            self.simulation.context.setPositions(candidate_positions)
            LocalEnergyMinimizer.minimize(self.simulation.context)
            state = self.simulation.context.getState(getPositions=True, getEnergy=True)
            return state.getPotentialEnergy().value_in_unit(kilojoule_per_mole)
        
        def simulated_annealing_refinement(self, candidate_positions: np.ndarray) -> float:
            decay_rate = np.log(self.T_final/self.T_initial) / self.n_steps
            for step in range(self.n_steps):
                new_T = self.T_initial * math.exp(decay_rate * step)
                self.integrator.setTemperature(new_T * kelvin)
                self.simulation.step(10)
            LocalEnergyMinimizer.minimize(self.simulation.context)
            state = self.simulation.context.getState(getPositions=True, getEnergy=True)
            energy = state.getPotentialEnergy().value_in_unit(kilojoule_per_mole)
            self.integrator.setTemperature(self.T_initial * kelvin)
            return energy
        
        def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
            self.step_count += 1
            action = action.reshape(self.N_images, self.n_atoms, 3)
            self.current_correction += action
            self.current_path = self.baseline_path + self.current_correction
            bc_penalty = np.linalg.norm(self.current_correction[0])**2 + np.linalg.norm(self.current_correction[-1])**2
            pos1 = self.current_path[:, self.bonds_arr[:, 0], :]
            pos2 = self.current_path[:, self.bonds_arr[:, 1], :]
            diff = pos1 - pos2
            d = np.linalg.norm(diff, axis=2)
            geom_penalty = np.sum((d - self.ref_bond_array)**2)
            smoothness_loss = np.sum(np.linalg.norm(self.current_path[1:] - self.current_path[:-1], axis=2)**2) / (self.N_images - 1)
            candidate_positions = self.build_combined_positions(self.current_path)
            self.simulation.context.setPositions(candidate_positions)
            LocalEnergyMinimizer.minimize(self.simulation.context)
            refined_energy = self.simulated_annealing_refinement(candidate_positions)
            reward = -refined_energy - 1000 * bc_penalty - self.lambda_geom * geom_penalty - 50 * smoothness_loss
            self.current_energy = refined_energy
            obs = self.current_path.flatten().astype(np.float32)
            terminated = self.step_count >= self.max_steps
            truncated = False
            info = {"energy": self.current_energy}
            return obs, reward, terminated, truncated, info
        
        def reset(self, seed: Optional[int] = None, options: Optional[dict] = None) -> Tuple[np.ndarray, dict]:
            self.current_correction = correction_net(alphas_tensor, baseline_positions_tensor, bonds_list).detach().cpu().numpy()
            self.current_path = self.baseline_path + self.current_correction
            self.current_energy = self.evaluate_current_energy()
            self.step_count = 0
            obs = self.current_path.flatten().astype(np.float32)
            return obs, {}
        
        def render(self, mode="human") -> None:
            print(f"Step {self.step_count}, Energy: {self.current_energy:.2f} kJ/mol")
    
    env_instance = NEBMorphingEnv(
        baseline_path, topology, combined_system, offsets,
        integrator, simulation, n_atoms, N_IMAGES, lambda_geom,
        np.array(bonds_list), ref_bond_tensor.cpu().numpy(),
        T_initial=300, T_final=50, n_steps=SA_STEPS, max_steps=MAX_STEPS
    )
    env = DummyVecEnv([lambda: Monitor(env_instance)])
    
    logging.info("Training SAC agent to optimize the morphing path...")
    start_time = time.time()
    sac_model = SAC("MlpPolicy", env, verbose=1, tensorboard_log="./sac_neb_tensorboard/")
    sac_model.learn(total_timesteps=SAC_TIMESTEPS)
    elapsed_sac = time.time() - start_time
    logging.info(f"SAC training complete in {elapsed_sac:.1f} seconds.")
    
    obs = env.reset()
    done = False
    while not done:
        action, _ = sac_model.predict(obs, deterministic=True)
        obs, rewards, dones, infos = env.step(action)
        env_instance.render()
        done = dones[0] or infos[0].get("terminated", False) or infos[0].get("truncated", False)
    
    final_corrections = env_instance.current_correction
    final_path = baseline_path + final_corrections
    np.save("final_path.npy", final_path)
    logging.info("Final learned trajectory saved as 'final_path.npy'.")
    
    logging.info("Starting final pathway minimization using SciPy L‑BFGS‑B optimizer...")
    pdb_ref = PDBFile("A_refined.pdb")
    forcefield_ref = ForceField("amber14-all.xml")
    system_ref = forcefield_ref.createSystem(topology, constraints="HBonds", rigidWater=True)
    integrator_ref = LangevinIntegrator(300*kelvin, 1.0/picosecond, 0.002*picosecond)
    if "CUDA" in available_platforms:
        platform_ref = Platform.getPlatformByName("CUDA")
    else:
        platform_ref = Platform.getPlatformByName("Reference")
    simulation_ref = Simulation(topology, system_ref, integrator_ref, platform_ref)
    box = topology.getPeriodicBoxVectors()
    if box is not None:
        simulation_ref.context.setPeriodicBoxVectors(*box)
    final_path = np.load("final_path.npy")
    logging.info(f"Loaded final_path with shape {final_path.shape}.")
    N_images_final = final_path.shape[0]
    n_atoms_final = final_path.shape[1]
    
    def energy_and_gradient(flat_positions: np.ndarray) -> Tuple[float, np.ndarray]:
        positions = flat_positions.reshape((n_atoms_final, 3))
        simulation_ref.context.setPositions(positions*nanometer)
        state = simulation_ref.context.getState(getEnergy=True, getForces=True)
        energy = state.getPotentialEnergy().value_in_unit(kilojoule_per_mole)
        forces = state.getForces(asNumpy=True)
        grad = -forces
        return energy, grad.flatten()
    
    minimized_energies = []
    for i in range(N_images_final):
        logging.info(f"Minimizing image {i+1} using L‑BFGS‑B optimizer...")
        initial_positions = final_path[i]
        initial_flat = initial_positions.flatten()
        result = scipy.optimize.minimize(
            energy_and_gradient,
            initial_flat,
            method="L-BFGS-B",
            jac=True,
            options={'maxiter': LBFGS_MAXITER, 'disp': LBFGS_DISP}
        )
        minimized_energy = result.fun
        minimized_energies.append(minimized_energy)
        minimized_positions = result.x.reshape((n_atoms_final, 3))
        final_path[i] = minimized_positions
        output_filename = f"final_structure_{i+1}.pdb"
        with open(output_filename, 'w') as f:
            PDBWriter.writeFile(topology, minimized_positions*nanometer, f)
        logging.info(f"Saved minimized structure as {output_filename} with energy {minimized_energy:.2f} kJ/mol.")
    np.save("final_path_minimized.npy", final_path)
    logging.info("Final minimized pathway saved as 'final_path_minimized.npy'.")
    
    if args.run_minimizer:
        run_minimizer()
    
    logging.info("Pathway generation complete.")
    print("Pathway generation complete.")
    sys.exit(0)

def replicate_system(system: System, N_images: int) -> Tuple[System, List[int]]:
    combined = System()
    offsets = []
    n = system.getNumParticles()
    for _ in range(N_images):
        offsets.append(combined.getNumParticles())
        for j in range(n):
            combined.addParticle(system.getParticleMass(j))
    return combined, offsets

# -----------------------------------------------------------------------------
# Main Entry Point
def main():
    parser = argparse.ArgumentParser(description="Integrated Protein Morphing Pipeline")
    # Endpoints
    parser.add_argument("-conf1", required=True, help="Protein A PDB file (e.g. model_01A.pdb)")
    parser.add_argument("-conf2", required=True, help="Protein B PDB file (e.g. model_01B.pdb)")
    # Interpolation options
    parser.add_argument("--interpolate", action="store_true", help="Perform local interpolation")
    parser.add_argument("--residues", help="Global residues to interpolate (e.g. '61,62,78-91' or filename)")
    parser.add_argument("--chain_residues", help="Chain-specific residues, format: 'A:1-10,B:20-30'")
    parser.add_argument("--steps", type=int, default=10, help="Number of interpolation steps (default: 10)")
    parser.add_argument("--chains", help="Comma-separated list of chain IDs for interpolation (default: all common)")
    parser.add_argument("--output_prefix", default="localwalk", help="Output prefix for interpolated files (default: 'localwalk')")
    # Pipeline parameters
    parser.add_argument("-nimages", type=int, default=16, help="Expected number of images if not using interpolation")
    parser.add_argument("-pretrain_epochs", type=int, default=200, help="Pre-training epochs for CorrectionNet")
    parser.add_argument("-sac_timesteps", type=int, default=50, help="Total timesteps for SAC training")
    parser.add_argument("--sa_steps", type=int, default=1000, help="Number of simulated annealing steps (NEB environment)")
    parser.add_argument("--max_steps", type=int, default=50, help="Maximum steps per NEB episode")
    # Cyclic SA parameters (for CorrectionNet pre-training)
    parser.add_argument("--sa_cycles", type=int, default=3, help="Number of cycles for cyclic SA (default: 3)")
    parser.add_argument("--sa_steps_per_cycle", type=int, default=300, help="Steps per cycle in cyclic SA (default: 300)")
    parser.add_argument("--sa_T_high", type=float, default=400, help="High temperature for cyclic SA (default: 400)")
    parser.add_argument("--sa_T_low", type=float, default=50, help="Low temperature for cyclic SA (default: 50)")
    parser.add_argument("--sa_update_frequency", type=int, default=5, help="Frequency (in epochs) to run cyclic SA (default: 5)")
    # CorrectionNet hyperparameters
    parser.add_argument("--lr", type=float, default=0.0005, help="Learning rate for CorrectionNet (default: 0.0005)")
    parser.add_argument("--sigma", type=float, default=0.05, help="Sigma for noise in CorrectionNet (default: 0.05)")
    # L-BFGS-B parameters for final minimization
    parser.add_argument("--lbfgs_maxiter", type=int, default=5000, help="Max iterations for L-BFGS-B (default: 5000)")
    parser.add_argument("--lbfgs_disp", action="store_true", help="Display L-BFGS-B optimizer output")
    # Final GROMACS minimizer pipeline option
    parser.add_argument("--run_minimizer", action="store_true", help="Run final GROMACS minimizer pipeline")
    args = parser.parse_args()
    
    global input_A, input_B, PRETRAIN_EPOCHS, SAC_TIMESTEPS, SA_STEPS, LBFGS_MAXITER, LBFGS_DISP, MAX_STEPS
    input_A = args.conf1
    input_B = args.conf2
    PRETRAIN_EPOCHS = args.pretrain_epochs
    SAC_TIMESTEPS = args.sac_timesteps
    SA_STEPS = args.sa_steps
    LBFGS_MAXITER = args.lbfgs_maxiter
    LBFGS_DISP = args.lbfgs_disp
    MAX_STEPS = args.max_steps

    main_prepare()
    main_run()
    logging.info("Pathway generation complete.")
    print("Pathway generation complete.")
    sys.exit(0)

if __name__ == "__main__":
    main()
