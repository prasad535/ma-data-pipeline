import os
from datetime import datetime
import logging

LOG_DIR = "logs"

def get_log_file_name():
    return f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_FILE_NAME, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s^; %(levelname)s^; %(filename)s^;%(funcname)s^] - %(message)s',
    filemode='w',
    level=logging.INFO
    
)