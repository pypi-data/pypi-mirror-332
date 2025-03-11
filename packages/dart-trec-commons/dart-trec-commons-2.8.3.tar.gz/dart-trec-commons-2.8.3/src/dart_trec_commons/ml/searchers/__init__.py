from abc import ABC, abstractmethod
from typing import List, Set, Tuple, Union

import numpy as np


class IssueSearcher(ABC):
    """
    An interface from which one can search for similar issues given a seed issue.
    """

    @abstractmethod
    def search(
            self,
            query: Union[str, np.ndarray],
            k: int = 3,
            not_in: Set[str] = None,
            embeddings: bool = False
    ) -> List[Union[Tuple[str, float], Tuple[str, float, np.ndarray]]]:
        """
        Searching for a list of issues similar to *issue*. The elements of the list are tuples composed of the issue id
        and its score according to search method. The list respects the order of similarities, where the first is the
        most similar. It returns an empty list when there is no similar issue to be returned.

        Args:
            query: Seed issue, serving as a query to find similar ones. It can be either an issue id or a vector
                    embedding.
            k: maximum number of similar issues to be returned.
            not_in: a set of issue ids whose elements should not appear in the returned list.
            embeddings: When True, it also returns the embeddings of each issue in the rank. Default is False.

        Returns: A list of tuples of similar issue. When embeddings is False, each tuple has the issue id and the score,
                when embeddings is True, the tuple also contains the embeddings of the issue.
        """

    @abstractmethod
    def load(self, path: str):
        """
        Loading the model from path. It may raise a TRECException.
        """

    @abstractmethod
    def save(self, path: str):
        """
        Saiving the model on path. It may raise a TRECException.
        """
