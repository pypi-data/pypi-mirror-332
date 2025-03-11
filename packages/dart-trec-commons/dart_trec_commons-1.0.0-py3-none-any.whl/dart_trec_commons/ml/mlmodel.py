# -*- coding: utf-8 -*-
"""
Copyright 2021-2031 SIDIA. All rights reserved.

Machine Learning classes and interfaces.

@author fabricio.dm
"""
import abc


class MLModel(metaclass=abc.ABCMeta):
    """
    Interface for Machine Learning algorithms that create binary models, which can predict, train, and store themselves
    in a model repository.
    """

    @abc.abstractmethod
    def predict(self, x, k=1):
        """
        Predicts the target labels.
        Args:
            x: the features as an array, dict, string, etc.
            k: the number of predicted items. Default: 1.
        Returns:
            list: A rank of items like {label: 'foo', score: 0.937}
        """

    @abc.abstractmethod
    def fit(self, x, y, **args):
        """
        Predicts the target labels.
        Args:
            x: the features as an array, dict, string, etc.
            y: the target labels.
            args: specific parameters depending on the implemented algorithm.
        """

    @abc.abstractmethod
    def load(self, path: str):
        """
        Loads a pre-trained model that was previously fitted and saved.
        Args:
            path: The path or key used to locate the model.
        """

    @abc.abstractmethod
    def save(self, path: str):
        """
        Saves the current trained model to the disk, database or model repository.
        Args:
            path: The path or key used to locate the model.
        """

    @abc.abstractmethod
    def get_memory_usage(self):
        """
        Collects info about memory usage.
        Returns:
            float: the percentage of memory usage.
        """

    @abc.abstractmethod
    def clear(self):
        """
        Releases unnecessary resources when closing the model or just to keep the model healthy.
        """
