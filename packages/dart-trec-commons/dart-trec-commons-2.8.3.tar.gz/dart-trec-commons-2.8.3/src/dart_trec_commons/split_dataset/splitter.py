from .splitters.learner_prod_splitter import LearnerProdSplitter
from .splitters.scikit_splitter import ScikitSplitter
from .splitters.split import Split


class SplitterFactory(object):
    """
    This factory finds and return the proper Splitter depending on params passed.
    """

    @staticmethod
    def get_instance(split_type: str) -> Split:
        if split_type is None:
            split_type = "scikit"
        split_type = str(split_type).lower().strip()
        factory = SplitterFactory()
        split = getattr(factory, split_type, SplitterFactory.fallback)
        return split()

    @staticmethod
    def scikit() -> Split:
        return ScikitSplitter

    @staticmethod
    def production() -> Split:
        return LearnerProdSplitter

    @staticmethod
    def fallback() -> Split:
        return ScikitSplitter


def train_test_split(*array, **options):
    isLearnerProd = options.get("label_col", None)
    if (isLearnerProd is not None):
        datasetDivide = SplitterFactory.get_instance("production")
        options.pop("stratify", None)
        options.pop("random_state", None)
        options.update(shuffle=False)
    else:
        datasetDivide = SplitterFactory.get_instance("scikit")

    return datasetDivide.split(*array, **options)
