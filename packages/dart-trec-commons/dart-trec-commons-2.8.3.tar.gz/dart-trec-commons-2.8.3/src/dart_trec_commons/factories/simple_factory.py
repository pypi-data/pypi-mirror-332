from typing import Dict, Callable

from ..exceptions import InvalidKeyException
from ..factories import AbstractFactory


class SimpleFactory(AbstractFactory):
    """
    A simple implementation of a factory that is based on a dictionary.
    """

    def __init__(self, entities: Dict[str, Callable]):
        self.entities: Dict[str, Callable] = entities

    def build(self, key: str, params: Dict = None) -> object:
        if params is None:
            params = dict()

        if key in self.entities:
            return self.entities[key](*params)
        else:
            raise InvalidKeyException()
