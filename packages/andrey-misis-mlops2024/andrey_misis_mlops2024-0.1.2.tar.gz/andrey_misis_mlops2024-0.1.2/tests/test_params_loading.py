"""
Module for test load config.
"""

from src.entities.params import read_pipeline_params


def test_load_config(config_path: str):
    config = read_pipeline_params(config_path)
    assert config.train_params.n_estimators == 100
    assert config.train_params.model_type == "LogReg"
    assert config.data_params.test_size == 0.2
    assert config.random_state == 42
