import logging
import os
from datetime import datetime

# Create log folder
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create log file with timestamp per day
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Create logger
logger = logging.getLogger()   # Root logger
logger.setLevel(logging.DEBUG) # Capture all levels in file

# IMPORTANT: prevent duplicate handlers
if not logger.handlers:

    # File handler
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console logging
    console_handler = logging.StreamHandler()  # Logs to terminal
    console_handler.setLevel(logging.INFO)     # Only INFO and above appear on screen
    formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)


''' 
if __name__=="__main__":
    logging.info("Logging has started")
'''