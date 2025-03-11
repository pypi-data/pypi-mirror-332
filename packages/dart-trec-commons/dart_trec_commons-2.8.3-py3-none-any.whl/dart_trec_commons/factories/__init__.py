from abc import ABC, abstractmethod
from typing import Dict


class AbstractFactory(ABC):
    """
    A factory to build different objects based on both a key and a dict of parameters.
    """

    @abstractmethod
    def build(self, key: str, params: Dict = None) -> object:
        """
        Build an object from the *key*
        Args:
            key: criterion to create an object.
            params: the parameters required to instantiate the selected object.

        Returns:
            The required object.
        """
