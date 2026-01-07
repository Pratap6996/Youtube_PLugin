import logging 
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from  my_root.root import root_name

LOG_DIR='Logs'
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE=5*1024*1024
MAX_LOG_COUNT=3

log_dir_path=os.path.join(root_name(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path=os.path.join(log_dir_path,LOG_FILE)
# print(log_file_path)

def configure_logger():
        """
         Docstring for configure_logger
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        
        # Define formatter
        formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

        # File handler with rotation
        file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=MAX_LOG_COUNT)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

         # Configure the logger
configure_logger()