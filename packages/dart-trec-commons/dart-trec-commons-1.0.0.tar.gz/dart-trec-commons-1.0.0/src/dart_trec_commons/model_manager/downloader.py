import os
import re
import logging

from threading import Thread
from minio.error import ResponseError, NoSuchKey

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)s) %(message)s",
)
logger = logging.getLogger("ModelDownloader")


class ModelDownloader(object):
    CHUNK_SIZE = 32 * 1024  # 32 MB

    def __init__(self, client, bucket, download_path="data"):
        self.client = client
        self.bucket = bucket
        self.path = download_path

    def start(self, callback=None):
        self.callback = callback
        self.thread = Thread(target=self.download_thread)
        self.thread.daemon = True
        self.thread.start()

    def download_thread(self):
        logger.debug("Download thread start")
        # Before listening to new events, search bucket for newer files
        newest_remote = self.get_newest_remote()
        if newest_remote:
            newest_local = self.get_newest_local()
            if self.compare_versions(newest_remote, newest_local) > 0:
                logger.info(
                    f"Found a newer file in server [{newest_remote}]. Downloading..."
                )
                self.download(newest_remote, callback=self.callback)

        events = self.client \
            .listen_bucket_notification(self.bucket,
                                        "", "", ["s3:ObjectCreated:*"])
        for event in events:
            logger.debug(event)
            for record in event["Records"]:
                if record["s3"]["bucket"]["name"] != self.bucket:
                    continue
                obj = record["s3"]["object"]
                logger.debug(f"New object: {obj}")
                self.download(obj["key"], callback=self.callback)
        logger.debug("Download thread finished")

    def download(self, filename, destination=None, callback=None):
        if not destination:
            destination = os.path.join(self.path, filename)
        try:
            data = self.client.get_object(self.bucket, filename)
            with open(destination, "wb") as filedata:
                for d in data.stream(self.CHUNK_SIZE):
                    filedata.write(d)
            if callback:
                callback(destination)
        except NoSuchKey as error:
            logger.error(f"Failed to download file {filename} [{error}]")

    def get_newest_remote(self):
        objects = self.client.list_objects_v2(self.bucket, recursive=True)
        name_order = [c.object_name for c in objects]
        if len(name_order) == 0:
            return None
        return sorted(name_order)[-1]

    def get_newest_local(self):
        try:
            taronly = re.compile('.*\\.tar$')
            filelist = os.listdir(self.path)
            return sorted(list(filter(taronly.match, filelist)))[-1]
        except (FileNotFoundError, IndexError):
            return None

    def compare_versions(self, filename1: str, filename2: str):
        def get_version(filename):
            if not filename:
                return 0
            try:
                return int(filename.split(".")[0])  # Format is <timestamp>.tar
            except ValueError:
                return False

        return get_version(filename1) - get_version(filename2)
