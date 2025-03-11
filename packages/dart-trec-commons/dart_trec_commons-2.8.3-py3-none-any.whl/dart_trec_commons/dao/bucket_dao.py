import abc


class BucketDao(abc.ABC):
    @abc.abstractmethod
    def find_buckets_by_date(self, start_date, end_date):
        pass
