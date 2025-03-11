# -*- coding: utf-8 -*-
"""
Copyright 2021-2031 SIDIA. All rights reserved.

Machine Learning classes and interfaces.

@author fabricio.dm
"""
import abc


class MLModelStore:
    """
    Interface defining a Memory Object Store made specifically to load, share and serve distributed Machine Learning
    models during prediction time. Each model instance is supposed to live in a different process allowing distributed
    execution. Traditional model store implementations rel on Python Proxy Objects and Ray Framework.

    @see https://ray.io
    @see https://docs.python.org/3/library/multiprocessing.html#proxy-objects
    """

    @abc.abstractmethod
    def start(self):
        """
        Initializes the store. Eg: create connections, proxies, processes, etc.
        """

    @abc.abstractmethod
    def get_light_model(self):
        """
        Serves a model by load balancing the replicas based on a resource criteria. Eg: returns the model with less
        memory or processor usage.
        Returns:
            MLModel: The next model.
        """

    @abc.abstractmethod
    def get_next_model(self):
        """
        Serves a model by load balancing the replicas based on a cycle criteria. Eg: returns the model based on a
        round-robin cycle.
        Returns:
            MLModel: The next model.
        """

    @abc.abstractmethod
    def load(self, path: str):
        """
        Load model from path and initialize the replicas.
        """

    @abc.abstractmethod
    def clear(self):
        """
        Clear resources currently not used by each models. It does not close or finish the store.
        """
