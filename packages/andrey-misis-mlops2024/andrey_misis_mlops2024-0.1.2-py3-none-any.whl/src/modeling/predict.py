"""
Module for eval models.
"""

import logging
import json
import joblib
import click

from sklearn.metrics import accuracy_score
import pandas as pd

from src.entities.params import read_pipeline_params

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@click.command()
@click.argument("config_path")
def eval_model(config_path: str):
    """Evaluate a machine learning model based on the provided parameters."""
    logger.info("Reading pipeline parameters from %s.", config_path)
    config = read_pipeline_params(config_path)

    logger.info("Loading testing dataset from %s.", config.data_params.test_data_path)
    test_df = pd.read_csv(config.data_params.test_processed_path)
    X_test = test_df.drop(columns=[config.data_params.target_column])
    y_test = test_df[config.data_params.target_column]

    logger.info("Loading the model from %s.", config.train_params.model_path)
    model = joblib.load(config.train_params.model_path)

    logger.info("Evaluating the model.")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    logger.info("Model evaluated successfully with accuracy: %.2f%%", accuracy * 100)

    metrics = {"accuracy": accuracy}
    with open(config.train_params.metrics_path, "w") as metrics_file:
        json.dump(metrics, metrics_file)
    logger.info("Metrics saved successfully to %s.", config.train_params.metrics_path)


if __name__ == "__main__":
    eval_model()
