import os
from abc import ABC, abstractmethod
from typing import Callable

from .abstract_model_manager import AbstractModelManager
from .simple_model_manager import SimpleModelManager


class ActiveModelManager(AbstractModelManager, ABC):
    """
    This model manager keeps an active thread monitoring the Minio repository to
    find newer versions of published models. It may be associated to a dependency model.
    """

    def __init__(self, host: str, bucket: str, access_key: str,
                 secret_key: str, base_dir: str,
                 dependency_model_manager: SimpleModelManager):
        super().__init__(host, bucket, access_key, secret_key, base_dir)
        self.dependency_model_manager = dependency_model_manager
        self.current: str = self._get_newest_available_local_model()

    def _get_newest_available_local_model(self) -> str:
        content = os.listdir(self.base_model_dir)
        content.sort(reverse=True)
        for c in content:
            if os.path.isdir(os.path.join(self.base_model_dir, c)):
                return f"{c}.tar"
        return None  # type: ignore

    def start_download_thread(self, callback: Callable[[], bool]):
        """
        Starts the download thread. When finding a new version of the model, it downloads, extracts, and callback
        the specified function.
        """

        def _callback(destination: str) -> bool:
            self.current = os.path.basename(destination)
            self._extract(self.current)
            return callback()

        self.downloader.start(_callback)

    def get_dependency(self):
        dep_label: str = self._get_dependency_label()
        if dep_label is not None and self.dependency_model_manager is not None:
            return self.dependency_model_manager.get(dep_label)
        return None

    def get_dependency_dir(self):
        dep_label: str = self._get_dependency_label()
        if dep_label is not None and self.dependency_model_manager is not None:
            return self.dependency_model_manager.get_model_dir(dep_label)
        return None

    def get_current_model_dir(self):
        return os.path.join(self.base_model_dir, self.current[:-4])

    @abstractmethod
    def get_current(self):
        """
        Specified how to construct the current model and returns it.
        """

    @abstractmethod
    def _get_dependency_label(self) -> str:
        """
        Returns the label that defines dependency version.
        """
