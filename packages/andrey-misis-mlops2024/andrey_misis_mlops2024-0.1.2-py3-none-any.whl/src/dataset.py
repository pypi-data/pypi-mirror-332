import click
from typing import Tuple
import logging
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entities.params import read_pipeline_params

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.argument("config_path")
def generate_dataset(config_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Generate a synthetic dataset, save as CSV, and split it into training and testing sets."""
    config = read_pipeline_params(config_path)
    logger.info(
        "Generating synthetic dataset with %d samples and %d features.",
        config.data_params.n_samples,
        config.data_params.n_features,
    )
    X, y = make_classification(
        n_samples=config.data_params.n_samples,
        n_features=config.data_params.n_features,
        random_state=config.random_state,
    )
    feature_names = [f"feature_{i}" for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=feature_names)
    df[config.data_params.target_column] = y
    logger.info("Dataset generated successfully. Splitting into train and test sets.")
    train_df, test_df = train_test_split(
        df, test_size=config.data_params.test_size, random_state=config.random_state
    )
    logger.info(
        "Saving train dataset to %s and test dataset to %s.",
        config.data_params.train_data_path,
        config.data_params.test_data_path,
    )
    train_df.to_csv(config.data_params.train_data_path, index=False)
    test_df.to_csv(config.data_params.test_data_path, index=False)
    logger.info("Datasets saved successfully.")
    return train_df, test_df


if __name__ == "__main__":
    generate_dataset()
