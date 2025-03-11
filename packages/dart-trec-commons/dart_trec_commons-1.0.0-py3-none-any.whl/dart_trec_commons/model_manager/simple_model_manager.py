import os
from abc import ABC, abstractmethod

from .abstract_model_manager import AbstractModelManager


class SimpleModelManager(AbstractModelManager, ABC):
    """
    Model manager that allows simple download (label specific or newer) of remote models from Minio.
    """

    def _get_defined_model(self, model_label: str = None) -> str:
        """
        Downloads (blocking) and extracts the model_label if it's not already available locally.
        If no model_label is specified, it downloads the newest available in the MINIO remote bucket.

        Args:
            model_label: defined model to be downloaded. If none, take the newest.

        Returns:
            downloaded model label.

        """
        if model_label is None:
            model_label = self.downloader.get_newest_remote()

        model_dir = self.get_model_dir(model_label)
        if not os.path.exists(model_dir):
            # if it exists, don't need to download again
            self.downloader.download(model_label)
            self._extract(model_label)

        return model_label

    def get_model_dir(self, model_label: str):
        return os.path.join(
            self.base_model_dir, model_label[:-4]
        )  # removes ".tar" from model_label to form the dir

    @abstractmethod
    def get(self, model_label) -> (object, str):
        """
        Returns: The model object and the model label.
        """
