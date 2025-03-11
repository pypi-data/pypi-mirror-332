import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from .split import Split


class LearnerProdSplitter(Split):
    @staticmethod
    def split(*arrays, **options) -> list:
        n_arrays = len(arrays)
        label_col = options.pop("label_col", None)

        if n_arrays == 0:
            raise ValueError("At least one array required as input")
        if (not isinstance(arrays[0], pd.DataFrame) and n_arrays > 1):
            raise ValueError("Only DataFrame is accepted here")
        if (label_col is None):
            raise ValueError(
                "Must have the column label name param. Example: label_col='synthetic'"
            )

        issues = arrays[0]
        labels = issues[label_col].dropna().unique()
        train, test = [], []
        for label in labels:
            each_class = issues.loc[issues[label_col] == label].index
            if (len(each_class) == 1):
                train.append(each_class)
            else:
                train_split, test_split = train_test_split(
                    each_class, **options)
                train.append(train_split)
                test.append(test_split)

        return issues.loc[np.concatenate(train)], issues.loc[np.concatenate(
            test)]
