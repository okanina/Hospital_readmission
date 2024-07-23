import os
import urllib.request as request
from pathlib import Path
from zipfile import ZipFile
from src.logger import logging
from src.utils.common import get_size
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if (not os.path.exists(self.config.local_data_file)):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} download! with the following info \n{headers}")
        else:
            logging.info(f"File already exist of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zipfile(self):

        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, "r") as zip_file:
            zip_file.extractall(unzip_path)