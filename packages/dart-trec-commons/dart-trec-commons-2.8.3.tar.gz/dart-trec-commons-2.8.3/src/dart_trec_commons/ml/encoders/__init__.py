from abc import ABC, abstractmethod
from typing import Dict, Union, List

import numpy as np


class IssueEncoder(ABC):
    """
    An encoder that transforms issues into either strings or vector representations.
    """

    def __init__(self, label: str):
        self.label: str = label

    @abstractmethod
    def transform(self, issues: List[Dict]) -> Union[List[str], np.ndarray]:
        """
        Transforming a list of issues into either a list of strings or a n-dim vector representation.
        Args:
            issues: a list of Issues, represented as a list of Dict with a subset of columns from the database.

        Returns:
            A proper representation.
        """

    @abstractmethod
    def vector_size(self) -> int:
        """
        Returns: The size of the vector, when the *transform* method encoder vectors. It raises a NotImplementedError,
        if the encoder returns strings.
        """
