def test_import_pipeline():
    from lwalkm import pipeline
    assert hasattr(pipeline, "main")
