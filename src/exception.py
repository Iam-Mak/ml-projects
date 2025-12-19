import sys
from src.logger import logger  # ensures logger config is active

def error_message_detail(error, error_details: sys) -> str:
    """
    Build a detailed error message including file name, line number, and the error.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Exception in [{file_name}] at line [{line_number}]: {error}"


class CustomException(Exception):
    """
    Custom exception class that automatically logs errors
    with detailed messages and full traceback.
    """
    def __init__(self, error_message, error_details: sys):

        self.error_message = error_message_detail(error_message, error_details)
        # Initialize parent Exception
        super().__init__(self.error_message)

        logger.error(f"{self.error_message}", exc_info=True)


''' 
if __name__ == "__main__":
    try:
        x = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)
'''