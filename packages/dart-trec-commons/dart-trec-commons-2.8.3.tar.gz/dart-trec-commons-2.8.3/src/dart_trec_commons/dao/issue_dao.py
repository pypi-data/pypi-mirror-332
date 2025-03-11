import abc


class IssueDao(abc.ABC):
    @abc.abstractmethod
    def find_issues_by_date_and_status(self,
                                       start_date,
                                       end_date,
                                       status='close',
                                       process_type='stemmed_tokens'):
        pass

    @abc.abstractmethod
    def find_issues_by_date(self,
                            start_date,
                            end_date,
                            process_type='stemmed_tokens'):
        pass

    @abc.abstractmethod
    def load_issue(self, issue_id, process_type='stemmed_tokens'):
        pass

    @abc.abstractmethod
    def find_issues_by_ids(self, issues_ids, process_type='stemmed_tokens'):
        pass
