import os
import tarfile
from datetime import datetime


class ModelUploader:
    def __init__(self, client, bucket):
        self.minio_client = client
        self.bucket = bucket

    def upload(self, model_path):
        output_file = f'{str(int(datetime.now().timestamp()))}.tar'

        with tarfile.open(output_file, "w") as tar:
            tar.add(os.path.join(model_path), arcname=os.path.sep)

        with open(output_file, 'rb') as file_data:
            file_stat = os.stat(output_file)
            self.minio_client.put_object(self.bucket, output_file, file_data,
                                         file_stat.st_size)

        os.remove(output_file)
        return output_file
