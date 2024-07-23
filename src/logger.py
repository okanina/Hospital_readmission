import os
import logging
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs") 
os.makedirs(logs_path, exist_ok=True) #creating dir called "logs" in a current working directory.

log_file_path=os.path.join(logs_path, log_file)

logging.basicConfig(level=logging.INFO, 
                    filename=log_file_path, 
                    format='[%(asctime)s]: %(module)s: %(lineno)s: %(message)s.'
                    # handlers=[logging.FileHandler(log_file)]
                    )

