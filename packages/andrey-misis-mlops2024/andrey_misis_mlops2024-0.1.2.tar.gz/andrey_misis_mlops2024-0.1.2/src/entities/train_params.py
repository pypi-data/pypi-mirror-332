"""
Module for defining training parameters.
"""

from dataclasses import dataclass, field

import marshmallow.validate


@dataclass()
class TrainParams:
    """Defines the model training parameters."""

    model_type: str = field(
        default="LogReg",
        metadata={
            "validate": marshmallow.validate.OneOf(["LogReg", "DecisionTree", "RandomForest"])
        },
    )
    n_estimators: int = field(
        default=100, metadata={"validate": marshmallow.validate.Range(min=1)}
    )
    max_depth: int = field(default=5, metadata={"validate": marshmallow.validate.Range(min=1)})
    C: float = field(default=1.0, metadata={"validate": marshmallow.validate.Range(min=0)})
    tol: float = field(default=1e-4, metadata={"validate": marshmallow.validate.Range(min=0)})
    model_path: str = field(default="models/model.pkl")
    metrics_path: str = field(default="reports/metrics.json")
