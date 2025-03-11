from sklearn.model_selection import train_test_split

from .split import Split


class ScikitSplitter(Split):
    @staticmethod
    def split(*arrays, **options) -> list:
        n_arrays = len(arrays)
        if n_arrays == 0:
            raise ValueError("At least one array required as input")
        return train_test_split(*arrays, **options)
