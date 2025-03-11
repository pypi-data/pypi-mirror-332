import os
import tarfile
from abc import ABC

from minio import Minio

from dart_trec_commons.model_manager.downloader import ModelDownloader


class AbstractModelManager(ABC):
    def __init__(self, host: str, bucket: str, access_key: str,
                 secret_key: str, base_dir: str):
        self.minio_client = Minio(host,
                                  access_key=access_key,
                                  secret_key=secret_key,
                                  secure=False)
        self.base_model_dir = os.path.join(base_dir, bucket)
        os.makedirs(self.base_model_dir, exist_ok=True)
        self.downloader = ModelDownloader(self.minio_client, bucket,
                                          self.base_model_dir)

    def _extract(self, model_label: str):
        local_model_tar = os.path.join(self.base_model_dir, model_label)
        dir_destination = model_label[:model_label.rfind(
            ".")]  # removes ".tar" from the label to create the dir name
        with tarfile.open(local_model_tar) as f:
            f.extractall(os.path.join(self.base_model_dir, dir_destination))
        os.remove(local_model_tar)
