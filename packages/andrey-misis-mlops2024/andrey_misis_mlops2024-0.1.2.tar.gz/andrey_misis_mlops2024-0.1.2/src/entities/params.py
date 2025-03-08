"""
Module for defining pipeline parameters.
"""

from dataclasses import dataclass, field

import yaml
from marshmallow_dataclass import class_schema

from .data_params import DataParams
from .train_params import TrainParams


@dataclass
class PipelineParams:
    """Defines the parameters for the machine learning pipeline."""

    train_params: TrainParams
    data_params: DataParams
    random_state: int = field(default=42)


PipelineParamsSchema = class_schema(PipelineParams)


def read_pipeline_params(path: str) -> PipelineParams:
    """read params from config file

    Args:
        path (str): path to config file

    Returns:
        PipelineParams: params from config file
    """
    with open(path, "r", encoding="utf-8") as input_stream:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
