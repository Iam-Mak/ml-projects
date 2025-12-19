import sys
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.exception import CustomException
from src.logger import logger

class ModelEvaluation:
    """
    Class to evaluate trained regression models.
    """

    def __init__(self, model, X_test, y_test):
        """
        Initialize with a trained model and test dataset.
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def evaluate(self):
        """
        Evaluate the model on test data and return metrics as a dictionary.
        """
        try:
            logger.info("Starting model evaluation")

            predictions = self.model.predict(self.X_test)

            r2 = r2_score(self.y_test, predictions)
            rmse = mean_squared_error(self.y_test, predictions, squared=False)
            mae = mean_absolute_error(self.y_test, predictions)

            metrics = {
                "R2_Score": r2,
                "RMSE": rmse,
                "MAE": mae
            }

            logger.info(f"Model evaluation completed: {metrics}")

            return metrics

        except Exception as e:
            raise CustomException(e, sys)