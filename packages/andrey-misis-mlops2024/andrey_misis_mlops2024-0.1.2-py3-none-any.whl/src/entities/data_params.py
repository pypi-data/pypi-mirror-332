"""
Module for defining data parameters.
"""

from dataclasses import dataclass, field

import marshmallow.validate


@dataclass()
class DataParams:
    """Defines the dataset generation parameters."""

    test_size: float = field(default=0.2, metadata={"validate": marshmallow.validate.Range(min=0)})
    n_features: int = field(default=20, metadata={"validate": marshmallow.validate.Range(min=1)})
    n_samples: int = field(default=100, metadata={"validate": marshmallow.validate.Range(min=1)})
    target_column: str = field(default="target")
    train_data_path: str = field(default="data/raw/train.csv")
    test_data_path: str = field(default="data/raw/test.csv")
    train_processed_path: str = field(default="data/processed/train.csv")
    test_processed_path: str = field(default="data/processed/test.csv")
    scaler_path: str = field(default="models/scaler.pkl")
