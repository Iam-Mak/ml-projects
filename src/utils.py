import os
import sys

import numpy as np
import pandas as pd

import dill
import pickle

from src.exception import CustomException
from src.logger import logger

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path: str, obj) -> None:

    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logger.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict) -> dict:
    try:
        report = {}

        for model_name, model in models.items():
            logger.info(f"Training and tuning model: {model_name}")

            param_grid = params.get(model_name, {})
            gs = GridSearchCV(model, param_grid, cv=3)
            gs.fit(X_train, y_train)

            # Set the best parameters
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score
            logger.info(f"{model_name}: Train R2 = {train_score:.4f}, Test R2 = {test_score:.4f}")

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        logger.info(f"Object loaded successfully from: {file_path}")
        return obj
    except Exception as e:
        raise CustomException(e, sys)