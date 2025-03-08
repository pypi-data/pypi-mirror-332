import logging
import json
import joblib
import click

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

from src.entities.params import read_pipeline_params

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.argument("config_path")
def train_model(config_path: str):
    """Train a machine learning model based on the provided training parameters."""
    config = read_pipeline_params(config_path)
    logger.info("Reading pipeline parameters from %s.", config_path)

    if config.train_params.model_type == "LogReg":
        model = LogisticRegression(
            C=config.train_params.C, tol=config.train_params.tol, random_state=config.random_state
        )
    elif config.train_params.model_type == "DecisionTree":
        model = DecisionTreeClassifier(
            max_depth=config.train_params.max_depth, random_state=config.random_state
        )
    elif config.train_params.model_type == "RandomForest":
        model = RandomForestClassifier(
            n_estimators=config.train_params.n_estimators,
            max_depth=config.train_params.max_depth,
            random_state=config.random_state,
        )
    else:
        logger.error("Unknown model type: %s", config.train_params.model_type)
        raise ValueError("Unknown model type")

    logger.info("Loading training and testing datasets.")
    train_df = pd.read_csv(config.data_params.train_processed_path)
    X_train = train_df.drop(columns=[config.data_params.target_column])
    y_train = train_df[config.data_params.target_column]
    logger.info("Training the model: %s", config.train_params.model_type)
    model.fit(X_train, y_train)
    joblib.dump(model, config.train_params.model_path)
    logger.info("Model saved to %s.", config.train_params.model_path)


if __name__ == "__main__":
    train_model()
