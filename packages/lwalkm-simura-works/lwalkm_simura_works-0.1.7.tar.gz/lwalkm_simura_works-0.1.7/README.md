## lwalkm

**lwalkm** is an integrated protein morphing pipeline designed for research in structural biology. It combines several steps into one tool:

1. **Local Interpolation ("Local Walk")**  
   Optionally, generate intermediate structures by interpolating between two protein configurations over a user‐defined set of residues. Each interpolated structure is refined using GROMACS.

2. **CorrectionNet/NEB Optimization**  
   The refined interpolation frames (or preexisting ones matching the pattern `localwalk_*_refined.pdb`) are loaded as a baseline pathway ("beads on a string"). A CorrectionNet neural network is then pre‐trained and integrated with a NEB (Nudged Elastic Band) framework—using cyclic simulated annealing and a SAC (Soft Actor-Critic) agent—to drive the pathway toward a lower–energy transition.

3. **Final Minimization**  
   Finally, a separate GROMACS minimization pipeline can be run on each final image, with energy extraction and plotting.

All key parameters (for interpolation, CorrectionNet training, simulated annealing, etc.) are configurable via command-line flags.

---

## Installation

### Installing from PyPI

If you want to install **lwalkm** from PyPI, simply run:

```bash
pip install lwalkm-simura-works
```

After installation, the console script `lwalkm` will be available in your environment’s PATH.

### Installing from Source

If you prefer to build and install from source, follow these steps:

1. **Install Build Tools:**  
   Ensure you have up-to-date pip, setuptools, and wheel:
   ```bash
   python3 -m pip install --upgrade pip setuptools wheel
   ```

2. **Build the Package:**  
   From the project root (where `pyproject.toml` is located):
   ```bash
   python3 -m build
   ```
   This will create a `dist/` folder with your distribution files (e.g., a `.whl` file).

3. **Install Locally:**  
   To install the package, run:
   ```bash
   python3 -m pip install .
   ```
   After installation, a console script named `lwalkm` will be available in your environment’s `bin` directory.

---

## Usage

Once installed, you can run the pipeline from the command line. Here are some examples and troubleshooting tips:

### Primary Command

If your environment is configured correctly and the `lwalkm` script is in your PATH, run:

```bash
lwalkm -conf1 model_01A.pdb -conf2 model_01B.pdb --interpolate --residues "1-10"
```

This command:
- Loads the endpoints (`model_01A.pdb` and `model_01B.pdb`).
- Performs local interpolation over residues 1–10.
- Uses default parameters for all other settings.

### Including Final Minimization

To also run the final GROMACS minimization pipeline, include the `--run_minimizer` flag:

```bash
lwalkm -conf1 model_01A.pdb -conf2 model_01B.pdb --interpolate --residues "1-10" --run_minimizer
```

### Alternate Command Options

If the `lwalkm` command is not recognized, try one of these alternatives:

- **Run via the Python Module:**  
  You can run the pipeline directly as a module:
  ```bash
  python3 -m lwalkm.pipeline -conf1 model_01A.pdb -conf2 model_01B.pdb --interpolate --residues "1-10" --run_minimizer
  ```

- **Check Your PATH:**  
  If using a virtual environment, ensure its `bin` directory is in your PATH:
  ```bash
  source path/to/your/venv/bin/activate
  lwalkm --help
  ```

### No Interpolation Mode

If you prefer not to perform interpolation, ensure that refined files (named `localwalk_*_refined.pdb`) already exist in your working directory, then run:

```bash
lwalkm -conf1 model_01A.pdb -conf2 model_01B.pdb --run_minimizer
```

In this mode, the pipeline detects the number of images from your existing files (with a fallback default of 16 via the `-nimages` flag).

### Full Example with Additional Parameters

For a complete run with additional customization, try:

```bash
lwalkm -conf1 model_01A.pdb -conf2 model_01B.pdb --interpolate --residues "1-313" --steps 10 --run_minimizer
```

This command:
- Uses `model_01A.pdb` and `model_01B.pdb` as endpoints.
- Performs interpolation over residues 1–313 (generating 11 frames: 10 steps + starting configuration).
- Runs the final GROMACS minimization pipeline.
- Uses default values for other parameters (e.g., pretraining epochs, simulated annealing settings, etc.).

---

## Troubleshooting Tips

- **Command Not Found:**  
  If the `lwalkm` command is not recognized, ensure your package is installed and your virtual environment’s `bin` directory is in your PATH. Alternatively, run the module directly:
  ```bash
  python3 -m lwalkm.pipeline --help
  ```

- **Python Version & Virtual Environment:**  
  Verify that you’re using the correct Python interpreter (e.g., `python3`) and that your virtual environment is activated.

- **Help and Parameters:**  
  To see all available command-line options:
  ```bash
  lwalkm --help
  ```
  or
  ```bash
  python3 -m lwalkm.pipeline --help
  ```

- **Final Minimization:**  
  To include the final minimization step, make sure to add the `--run_minimizer` flag to your command.

---

Let me know if you need any further adjustments or additional help!

## Default Parameters

If you omit any flag, the following defaults are used:

| Flag                             | Default Value  | Description                                                                                   |
|-------------------------------   |---------------:|:----------------------------------------------------------------------------------------------|
| Endpoints                        |                |                                                                                               |
| `-conf1` / `-conf2`              | (Required)     | Protein A and B PDB files (must supply).                                                      |
| Interpolation                    |                |                                                                                               |
| `--interpolate`                  | False          | Whether to perform local interpolation.                                                       |
| `--residues`                     | None           | Global residues to interpolate (required if using `--interpolate`).                           |
| `--chain_residues`               | None           | Chain-specific residues, e.g., "A:1-10,B:20-30".                                              |
| `--steps`                        | 10             | Number of interpolation steps (produces `steps + 1` frames).                                  |
| `--chains`                       | None           | Comma-separated chain IDs (if omitted, uses all common chains).                               |
| `--output_prefix`                | "localwalk"    | Prefix for interpolation output files.                                                        |
| Pipeline                         |                |                                                                                               |
| `-nimages`                       | 16             | Expected number of images if not interpolating (the code counts existing `localwalk` files).  |
| `-pretrain_epochs`               | 200            | CorrectionNet pre-training epochs.                                                            |
| `-sac_timesteps`                 | 50             | Total timesteps for the SAC agent in the NEB environment.                                     |
| `--sa_steps`                     | 1000           | Number of simulated annealing steps in the NEB environment’s refinement routine.              |
| `--max_steps`                    | 50             | Maximum steps per episode in the NEB environment.                                             |
| Cyclic SA (Pre-training)         |                |                                                                                               |
| `--sa_cycles`                    | 3              | Number of heat/cool cycles when cyclic SA is triggered.                                       |
| `--sa_steps_per_cycle`           | 300            | Steps per cycle during cyclic SA.                                                             |
| `--sa_T_high`                    | 400            | High temperature (K) for cyclic SA.                                                           |
| `--sa_T_low`                     | 50             | Low temperature (K) for cyclic SA.                                                            |
| `--sa_update_frequency`          | 5              | Frequency (in epochs) to run cyclic SA during CorrectionNet pre-training.                     |
| CorrectionNet Hyperparameters.   |                |                                                                                               |
| `--lr`                           | 0.0005         | Learning rate for the CorrectionNet Adam optimizer.                                           |
| `--sigma`                        | 0.05           | Standard deviation of noise added during CorrectionNet pre-training.                          |
| L-BFGS-B Minimization            |                |                                                                                               |
| `--lbfgs_maxiter`                | 5000           | Maximum iterations for SciPy’s L‑BFGS‑B minimizer per final image.                            |
| `--lbfgs_disp`                   | False          | If specified, displays L‑BFGS‑B optimizer output.                                             |
| Final GROMACS Minimizer          |                |                                                                                               |
| `--run_minimizer`                | False          | If true, runs the final GROMACS minimizer pipeline on each final structure.                   |

Key Points:
- If you omit a flag, its default is used.
- Endpoints (`-conf1` and `-conf2`) are required.
- If you do not specify `--interpolate`, you must have preexisting `localwalk_*_refined.pdb` files.
- The package is designed so that you can start with a minimal run and then tweak parameters as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you encounter bugs, have feature requests, or want to improve the code, please open an issue or submit a pull request on our GitHub repository.

Repository: https://github.com/simura-works/lwalkm_simura-works

## Contact

For questions or suggestions, please contact Bernard Kwadwo Essuman (mailto:bessuman.academia@gmail.com).

