from pymongo import MongoClient

from dart_trec_commons.singleton import Singleton


class DBConnection(metaclass=Singleton):
    def __init__(self, db_uri):
        self.db_uri = db_uri
        self.conn = None

    def get_connection(self):
        if not self.conn:
            self.conn = MongoClient(self.db_uri)
        return self.conn
