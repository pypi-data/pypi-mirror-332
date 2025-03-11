import os
import logging
from minio import Minio, ResponseError
from minio.error import NoSuchKey

from .downloader import ModelDownloader
from .uploader import ModelUploader

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)s) %(message)s",
)
logger = logging.getLogger("ModelDownloader")


class ModelManager:
    def __init__(self, host, bucket, access_key, secret_key):
        self.minio_client = Minio(host,
                                  access_key=access_key,
                                  secret_key=secret_key,
                                  secure=False)
        self.bucket = bucket
        found = self.minio_client.bucket_exists(bucket)
        if not found:
            self.minio_client.make_bucket(bucket)
        else:
            logger.debug("Bucket already exists")

    def delete_old_files(self, keep_n_files=5):
        """ Add models to a tarfile and sends it to the directory configured in self.output_path_recommender
        """
        logger.debug('delete_old_to_remote')

        # List all object paths in bucket that begin with my-prefixname.
        recommender_files = self.minio_client.list_objects(self.bucket)

        files_list = []
        for rec_file in recommender_files:
            files_list.append(rec_file.object_name)

        files_list = sorted(files_list, reverse=True)

        if len(files_list) > keep_n_files:
            delete_errors = self.minio_client.remove_objects(
                self.bucket, files_list[keep_n_files:])

            if delete_errors:
                for del_error in delete_errors:
                    logger.error(del_error)

        logger.info(f'Removed files:{files_list[keep_n_files:]}')

        recommender_files = self.minio_client.list_objects(self.bucket)

        logger.debug('Files list:')
        for rec_file in recommender_files:
            print(rec_file.object_name)

    def upload(self, model_path):
        uploader = ModelUploader(self.minio_client, self.bucket)
        uploader.upload(model_path)

    def download(self, download_path, callback=None):
        downloader = ModelDownloader(self.minio_client, self.bucket,
                                     download_path)
        downloader.start(callback)

    def download_by_name(self, file_name, destination):
        if not os.path.exists(destination):
            downloader = ModelDownloader(self.minio_client, self.bucket)
            downloader.download(file_name, destination)

    def check_file_exist(self, file_path):
        try:
            self.minio_client.stat_object(self.bucket, file_path)
            return True
        except Exception as err:
            if isinstance(err, NoSuchKey):
                return False
            else:
                raise ResponseError(err)
