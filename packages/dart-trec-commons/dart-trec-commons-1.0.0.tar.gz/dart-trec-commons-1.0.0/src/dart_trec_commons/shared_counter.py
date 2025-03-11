import sys

from multiprocessing import Value


class SharedCounter:
    def __init__(self, init_value=0, max_value=sys.maxsize):
        self.counter = Value('i', init_value)
        self.max_value = max_value if max_value >= 1 else 1

    def increment(self, incr=1):
        with self.counter.get_lock():
            value = self.counter.value
            self.counter.value = (value + incr) % self.max_value
            return value
