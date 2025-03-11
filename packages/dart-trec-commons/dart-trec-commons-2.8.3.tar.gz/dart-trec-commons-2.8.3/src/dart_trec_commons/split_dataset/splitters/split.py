from abc import ABC, abstractmethod


class Split(ABC):
    """
    This interface defines common methods for split datasets.
    """

    @abstractmethod
    def split(self, *arrays: tuple, **options: dict) -> list:
        """
        Splits a arrays or matrices into train and test subsets.
        Args:
            *arrays: Allowed inputs are lists, numpy arrays, scipy-sparse matrices or pandas dataframes.
            **options:
                - test_size: float or int, default=None
                    If float, should be between 0.0 and 1.0 and represent the proportion of the
                    dataset to include in the test split. If int, represents the absolute number
                    of test samples. If None, the value is set to the complement of the train size.
                    If train_size is also None, it will be set to 0.25.
                - train_size: float or int, default=None
                    If float, should be between 0.0 and 1.0 and represent the proportion of the
                    dataset to include in the train split.If int, represents the absolute number
                    of train samples. If None, the value is automatically set to the complement
                    of the test size.
                - random_state: int or RandomState instance, default=None
                    Controls the shuffling applied to the data before applying the split.
                    Pass an int for reproducible output across multiple function calls.
                - shuffle: bool, default=True
                    Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None.
                - stratify: array-like, default=None
                    If not None, data is split in a stratified fashion, using this as the class labels.
                - label_col: string, default=None
                    If not None, the split will be the same of the production T-REC, using this
                    to distinguish classes and get the temporal split.
        Returns:
            list: List containing train-test split of inputs. The output type is the same as the input type.
        """
