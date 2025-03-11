import logging

from .bucket_dao import BucketDao

logger = logging.getLogger('BucketDaoImpl')

BUCKET_COLLECTION = "bucket_document"


class BucketDaoImpl(BucketDao):
    '''
        Bucket DAO Mongo class to provide data access to bucket document in a mongo db.
        @author arthur.b
    '''

    def __init__(self, db_conn):
        self.db = db_conn.get_default_database()

    def find_buckets_by_date(self, start_date, end_date):
        collection = self.db[BUCKET_COLLECTION]

        results = collection.find(
            {
                'oldest_date': {
                    '$gte': start_date,
                    '$lte': end_date
                },
                'length': {
                    '$gte': 2
                }
            }, {
                '_id': 1,
                'oldest_date': 1,
                'issues': 1,
                'positive_pairs': 1
            }).sort('oldest_date')

        return list(results)
