import logging
import joblib
import click


import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.entities.params import read_pipeline_params

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.argument("config_path")
def preprocess(config_path: str):
    """Train a machine learning model based on the provided training parameters."""
    config = read_pipeline_params(config_path)
    scaler = StandardScaler()
    train_df = pd.read_csv(config.data_params.train_data_path)
    test_df = pd.read_csv(config.data_params.test_data_path)
    feature_cols = train_df.columns.difference([config.data_params.target_column])
    train_df[feature_cols] = scaler.fit_transform(
        train_df.drop(columns=[config.data_params.target_column])
    )
    test_df[feature_cols] = scaler.transform(
        test_df.drop(columns=[config.data_params.target_column])
    )
    logger.info("Training the model: %s", config.train_params.model_type)
    joblib.dump(scaler, config.data_params.scaler_path)
    logger.info("Model saved to %s.", config.train_params.model_path)
    logger.info(
        "Saving preprocessed train dataset to %s and preprocessed test dataset to %s.",
        config.data_params.train_processed_path,
        config.data_params.test_processed_path,
    )
    train_df.to_csv(config.data_params.train_processed_path, index=False)
    test_df.to_csv(config.data_params.test_processed_path, index=False)
    logger.info("Datasets saved successfully.")


if __name__ == "__main__":
    preprocess()
