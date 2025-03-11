import os


class EnvUtils:
    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

    @staticmethod
    def get_bool(key, default=False):
        value = os.getenv(key, default)
        return value in [True, "True", "true", "TRUE", "yes", "y", "ok"]

    @staticmethod
    def get_int(key, default=0):
        value = os.getenv(key, default)
        return int(value)

    @staticmethod
    def get_float(key, default=0.0):
        value = os.getenv(key, default)
        return float(value)
