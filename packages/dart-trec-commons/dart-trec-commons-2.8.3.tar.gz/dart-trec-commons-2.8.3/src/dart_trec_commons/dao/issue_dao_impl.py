import sys
import logging
from datetime import datetime

import pandas as pd

from dart_trec_commons.exceptions import NotFoundException
from .issue_dao import IssueDao

logger = logging.getLogger('DataProcessed')

ISSUE_COLLECTION = "issue_document"


class IssueDaoImpl(IssueDao):
    """
        Issues DAO Mongo class to provide data access to issues document in a mongo db.
        @author arthur.b
    """

    def __init__(self, db_conn):
        self.db = db_conn.get_default_database()

    @staticmethod
    def __skip_page(current_page, page_size):
        return (current_page - 1) * page_size

    def __find_issues_by_filter(self, filter, process_type='stemmed_tokens', page=1, limit=sys.maxsize):
        collection = self.db[ISSUE_COLLECTION]
        results = collection.aggregate([
            filter, {
                '$project': {
                    '_id': 1,
                    'create_date': 1,
                    'defect_type': 1,
                    'title_tags': '$title.tags',
                    'title': f'$title.tokens.{process_type}' if process_type != "flat" else '$title.text',
                    'description': f'$description.tokens.{process_type}' if process_type != "flat" else '$description.text',
                    'steps_to_reproduce': f'$steps_to_reproduce.tokens.{process_type}' if process_type != "flat" else '$steps_to_reproduce.text',
                    'module_detail': 1,
                    'module_name': 1,
                    'reg_open_yn': 1,
                    'reporter_department': '$reporter.department',
                    'tg_solver_id': '$solver.master_tg.id',
                    'tg_solver_name': '$solver.master_tg.name',
                    'tg_solver_full_name': '$solver.master_tg.path',
                    'status': 1,
                    'test_item': 1,
                    'update_date': 1,
                    'document_lang': '$lang'
                }
            },  {"$skip": self.__skip_page(page, limit)},{"$limit": limit},
        ])

        return results

    def find_issues_by_date_and_status(self,
                                       start_date,
                                       end_date,
                                       status='close',
                                       process_type='stemmed_tokens',
                                       page=1,
                                       limit=sys.maxsize):
        """ Find issues by status and between specified dates
        Args:
            start_date (datetime): start date
            end_date (datetime): end date
            status (str): issues status
            process_type (str): stemmed_tokens | stemmed_tokens_without_stopwords
                                tokens | tokens_without_stopwords
        Returns:
            pd.DataFrame : DataFrame with issue data as defined in MongoDB
            :param limit:
            :param page:
        """
        start_date = 1000 * start_date.timestamp()
        end_date = 1000 * end_date.timestamp()

        filter = {
            '$match': {
                '$and': [{
                    'create_date': {
                        '$gte': start_date,
                        '$lte': end_date
                    }
                }, {
                    'status': {
                        '$eq': status
                    }
                }]
            }
        }

        results = self.__find_issues_by_filter(filter, process_type, page=page, limit=limit)

        issue_df = pd.DataFrame(list(results))

        logger.debug(
            f'get_issue_dataset | {issue_df.shape[0]} issues were retrieved')
        if issue_df.shape[0] > 0:
            issue_df['create_date'] = issue_df['create_date'].apply(
                lambda x: datetime.fromtimestamp(x / 1000))
            issue_df['update_date'] = issue_df['update_date'].apply(
                lambda x: datetime.fromtimestamp(x / 1000))
        else:
            raise Exception('Given interval did not retrieve issues.')

        return issue_df

    def find_issues_by_date(self,
                            start_date,
                            end_date,
                            process_type='stemmed_tokens',
                            page=1,
                            limit=sys.maxsize):
        """ Find issues by status and between specified dates
        Args:
            start_date (datetime): start date
            end_date (datetime): end date
            process_type (str): stemmed_tokens | stemmed_tokens_without_stopwords
                                tokens | tokens_without_stopwords
        Returns:
            pd.DataFrame : List with issue data as defined in MongoDB
        """
        start_date = 1000 * start_date.timestamp()
        end_date = 1000 * end_date.timestamp()

        filter = {
            '$match': {
                '$and': [{
                    'create_date': {
                        '$gte': start_date,
                        '$lte': end_date
                    }
                }]
            }
        }

        results = list(self.__find_issues_by_filter(filter, process_type, page=page, limit=limit))

        logger.debug(
            f'get_issue_dataset | {len(results)} issues were retrieved')

        if len(results) > 0:
            for issue in results:
                issue['create_date'] = datetime.fromtimestamp(
                    issue['create_date'] / 1000)
                issue['update_date'] = datetime.fromtimestamp(
                    issue['update_date'] / 1000)
        else:
            raise Exception('Given interval did not retrieve issues.')

        return results

    def load_issue(self, issue_id, process_type='stemmed_tokens',page=1 ,limit=sys.maxsize):
        """ Find issues by status and between specified dates
        Args:
            issue_id (str): issues id
        Returns:
           issue : dict
        """
        filter = {'$match': {'_id': issue_id}}

        results = list(self.__find_issues_by_filter(filter, process_type, page=page, limit=limit))

        if not results:
            raise NotFoundException()

        return results[0]

    def find_issues_by_ids(self, issues_ids, process_type='stemmed_tokens', page=1 ,limit=sys.maxsize):
        """ Find issues by status and between specified dates
        Args:
            issue_id (str): issues id
        Returns:
           issue : dict
        """
        filter = {'$match': {'_id': {'$in': issues_ids}}}

        return list(self.__find_issues_by_filter(filter, process_type, page=page, limit=limit))
