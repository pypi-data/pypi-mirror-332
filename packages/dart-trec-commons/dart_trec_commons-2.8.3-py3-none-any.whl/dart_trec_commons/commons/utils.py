import logging
from collections import Counter
from typing import Union, List

import numpy as np
import pandas as pd
from pandas import DataFrame

from dart_trec_commons.exceptions import InvalidValueException, UnexpectedException, \
    NotFoundException

logger = logging.getLogger("Utils")


class Utils:
    """
        Util class to support transformation, auxiliary tasks and other proposes.
        Wiki: https://github.sec.samsung.net/SOL/dart-trec-commons/wiki/Utils

        @author thiago.m
    """

    COLUMNS_TEXTUAL = [
        'title', 'description', 'steps_to_reproduce', 'comment', 'title_tags',
        'description_tags'
    ]
    """
        Possible values for tokens:
        - stemmed_tokens
        - stemmed_tokens_without_stopwords
        - tokens_without_stopwords
        - tokens
    """
    TOKEN_TYPE_TEXTUAL: dict[str, str] = {
        'title': 'stemmed_tokens',
        'description': 'stemmed_tokens',
        'steps_to_reproduce': 'stemmed_tokens',
        'comment': 'stemmed_tokens',
        'title_tags': 'tokens',
        'description_tags': 'tokens'
    }

    NOT_INFORMED = 'N/I'
    LABEL = 'tg_solver_id'

    @staticmethod
    def concat(df, columns):
        """
            Concat columns in a dataframe

            Parameters
            ----------
            df: pandas.Dataframe
                a pandas dataframe.
            columns: list
                a list of columns to be concatenated as str

            Returns
            -------
            df: pandas.Dataframe
        """
        df = Utils.get_dataframe(df)
        try:
            return df[columns].agg(' '.join, axis=1)
        except Exception:
            raise UnexpectedException(
                f'An unexpected error happened. The columns {columns}' +
                ' can not be in a flatten format. Check the columns and use flatten() method.'
            )

    @staticmethod
    def fill(df, columns, default_value=''):
        """
            Fill invalid values of categorical columns

            Parameters
            ----------
            df: pandas.Dataframe
                a pandas dataframe.
            columns: list
                a list of columns to replace missing values
            default_value: str
                value default to be replaced when detected missing values

            Returns
            -------
            df: pandas.Dataframe
        """
        df = Utils.get_dataframe(df)
        columns_to_fill = [col for col in columns if col in df.columns]
        for col in columns_to_fill:
            df[col].fillna(value=default_value, inplace=True)
        return df

    @staticmethod
    def get_language_from_flatten_text(df, columns):
        """
            Set main language, set Chinese as Korean and Assign all other languages as English

            Parameters
            ----------
            df: pandas.Dataframe
                a pandas dataframe.
            columns: list
                a list of columns to be detected the language.
            Returns
            -------
            df: pandas.Dataframe
        """
        df = Utils.get_dataframe(df)
        for col in columns:
            len_col = '{}_len'.format(col)
            lang_col = '{}_lang'.format(col)
            if len_col not in df.columns or lang_col not in df.columns:
                raise NotFoundException(
                    'Call flatten() method to generate' +
                    f' length and lang for available columns {Utils.COLUMNS_TEXTUAL}'
                )

        def get_main_language(row, columns):
            feature_lengths = [(row[col + '_len'], row[col + '_lang'])
                               for col in columns]
            main_language = sorted(feature_lengths, key=lambda x: x[0])[-1]
            return main_language[1]

        for col in columns:
            if col not in Utils.COLUMNS_TEXTUAL:
                raise InvalidValueException('columns', col,
                                            Utils.COLUMNS_TEXTUAL)

        document_lang = df.apply(lambda row: get_main_language(row, columns),
                                 axis=1)
        document_lang.mask(document_lang == 'zh', 'ko', inplace=True)
        document_lang.mask(document_lang != 'ko', 'en', inplace=True)
        return document_lang

    @staticmethod
    def flatten(issues: Union[List, DataFrame], token_type=None, label=LABEL):
        """
            Flatten a processed data in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents
            token_type: list
                a dict of textual columns and their tokens to be used.
            label: str
            Returns
            -------
            issues: list
        """
        if not token_type:
            token_type = Utils.TOKEN_TYPE_TEXTUAL

        issues = Utils.get_dataframe(issues)
        # Flatten master tg
        issues = Utils.flatten_master_tg(issues, label)
        # Flatten tags
        issues = Utils.flatten_textual_tags_attributes(issues)
        # Flatten comments
        issues = Utils.flatten_comments_attributes(issues, token_type)
        # Flatten textual columns
        issues = Utils.flatten_textual_attributes(issues, token_type)
        # Flatten reporter
        issues = Utils.flatten_reporter(issues)

        return issues

    @staticmethod
    def flatten_reporter(issues):
        """
            Flatten the reporter attribute in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents

            Returns
            -------
            issues: list
        """
        issues = issues.copy()

        def fill_reporter_info(field, issues, df):
            df.fillna('', inplace=True)
            issues['reporter_{}'.format(field)] = df

        # Flatten reporter column
        if 'reporter' in issues.columns:
            reporter_df = issues['reporter'].apply(pd.Series)
            if 'department' in reporter_df.columns:
                fill_reporter_info('department', issues,
                                   reporter_df['department'])

            if 'master_tg' in reporter_df.columns:
                reporter_tg_df = reporter_df['master_tg'].apply(pd.Series)
                fill_reporter_info('tg', issues, reporter_tg_df['name'])
        return issues

    @staticmethod
    def flatten_comments_attributes(issues, token_type):
        """
            Flatten the comments in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents
            token_type: list
                a dict of textual columns and their tokens to be used.

            Returns
            -------
            issues: list
        """
        issues = issues.copy()

        def get_comment_tokens(comments, token_type):
            tokens = [
                comment['tokens'][token_type] for comment in comments
                if 'tokens' in comment
            ]
            if len(tokens) > 0:
                tokens = np.concatenate(tokens)
            return tokens

        def get_lang_comment_most_frequent(comments):
            if len(comments) > 0:
                occurence_count = Counter(
                    [comment['lang'] for comment in comments])
                comment_lang = occurence_count.most_common(1)[0][0]
            else:
                comment_lang = Utils.NOT_INFORMED
            return comment_lang

        comments_merged = []
        if 'comments' in issues.columns:
            # Flatten comment column
            for comments in issues['comments']:
                comment_lang = get_lang_comment_most_frequent(comments)
                stemmed_tokens = get_comment_tokens(
                    comments, token_type='stemmed_tokens')
                stemmed_tokens_without_stopwords = get_comment_tokens(
                    comments, token_type='stemmed_tokens_without_stopwords')
                tokens_without_stopwords = get_comment_tokens(
                    comments, token_type='tokens_without_stopwords')
                tokens = get_comment_tokens(comments, token_type='tokens')
                comments_merged.append({
                    'lang': comment_lang,
                    'tokens': {
                        'stemmed_tokens': stemmed_tokens,
                        'stemmed_tokens_without_stopwords':
                            stemmed_tokens_without_stopwords,
                        'tokens_without_stopwords': tokens_without_stopwords,
                        'tokens': tokens
                    }
                })
            issues['comment'] = comments_merged
        return issues

    @staticmethod
    def flatten_textual_attributes(issues, token_type):
        """
            Flatten the texutal attributes (title, description, etc.)
            in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents
            token_type: list
                a dict of textual columns and their tokens to be used.

            Returns
            -------
            issues: list
        """
        issues = issues.copy()
        columns_exist = []
        columns = Utils.COLUMNS_TEXTUAL
        df_features = pd.DataFrame()
        for col in columns:
            token_type_name = token_type[col] if col in token_type else Utils.TOKEN_TYPE_TEXTUAL[
                col]
            columns_exist.append(col)
            if col in issues.columns:
                df_features = issues[col].apply(pd.Series)
                issues[col] = df_features['tokens'].apply(
                    lambda row, c: ' '.join(row[c]), c=token_type_name)
                issues[col + '_len'] = df_features['tokens'].apply(
                    lambda row, c: len(row[c]), c=token_type_name)
                issues[col + '_lang'] = df_features['lang']
                issues[col].fillna('', inplace=True)

        return issues

    @staticmethod
    def flatten_textual_tags_attributes(issues):
        """
            Flatten the texutal tags (title, description)
            in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents
            token_type: list
                a dict of textual columns and their tokens to be used.

            Returns
            -------
            issues: list
        """
        issues = issues.copy()
        for col in ['title', 'description']:
            if col in issues.columns:
                df_features = issues[col].apply(pd.Series)
                if 'tags' in df_features.columns:
                    tags_tokens = []
                    lang_df = df_features['lang']
                    tags_df = df_features['tags']
                    for lang, tags in zip(lang_df, tags_df):
                        tags_tokens.append({
                            'lang': lang,
                            'tokens': {
                                'stemmed_tokens': tags,
                                'stemmed_tokens_without_stopwords': tags,
                                'tokens_without_stopwords': tags,
                                'tokens': tags
                            }
                        })
                    issues['{}_tags'.format(col)] = tags_tokens
        return issues

    @staticmethod
    def flatten_master_tg(issues, label):
        """
            Flatten the master tg in proper way to uses in general.

            Parameters
            ----------
            issues: list
                a list of issue documents
            label: str
                a label string to be used as pivot in processing.

            Returns
            -------
            issues: list
        """
        issues = issues.copy()

        def get_field_dict_in_row(row, field):
            if isinstance(row, dict):
                return row.get(field)
            else:
                return Utils.NOT_INFORMED

        def get_list_from_dict_in_row(row, field):
            if isinstance(row, dict):
                if isinstance(row.get(field), list):
                    return row.get(field)
            return [Utils.NOT_INFORMED]

        if 'solver' in issues.columns:
            # Flatten solution column
            solver_df = issues['solver'].apply(pd.Series)

            if 'master_tg' in solver_df.columns:
                solver_df['master_tg'].fillna('', inplace=True)
                issues[label] = solver_df['master_tg'].apply(
                    lambda row: get_field_dict_in_row(row, 'id'))
                issues['tg_solver_name'] = solver_df['master_tg'].apply(
                    lambda row: get_field_dict_in_row(row, 'name'))
                issues['tg_solver_full_name'] = solver_df['master_tg'].apply(
                    lambda row: '->'.join(
                        get_list_from_dict_in_row(row, 'path')))
                issues.drop(issues[issues[label] == Utils.NOT_INFORMED].index,
                            inplace=True)

        return issues

    @staticmethod
    def get_dataframe(value):
        """
            Get a dataframe instance.

            Parameters
            ----------
            value: object
                an object to be checked and convert to dataframe.

            Returns
            -------
            dataframe: pd.DataFrame
        """
        if isinstance(value, pd.DataFrame):
            return value
        return pd.DataFrame.from_dict(value)
