from abc import ABC, abstractmethod
from typing import Dict, Iterable

from ..ml.encoders import IssueEncoder

DEFAULT_SUFFIX = "_index"


class IssueIndexer(ABC):
    """
    Indexing issues into a data structure able to associate similar issues to each other.
    """

    def __init__(self, encoder: IssueEncoder):
        """
        The indexer depends on an encoder, which will transform the issues into
        Args:
            encoder:
        """
        self.encoder: IssueEncoder = encoder

    @abstractmethod
    def index(self, issues: Iterable[Dict]) -> bool:
        pass
