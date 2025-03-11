import os
from typing import Tuple

from google.cloud import storage

from gitlab_mlops.provider.gcp.base import BaseGCPClient


class GCSClient(BaseGCPClient):
    """
    Client for Google Cloud Storage operations.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = storage.Client(
            project=self.project_id, credentials=self.credentials_obj
        )

    def download_from_gcs(self, gcs_uri: str, local_path: str) -> str:
        """
        Download files from GCS location.
        :param gcs_uri: GCS URI to download from
        :param local_path: Local path to download to
        :return: Local path
        """
        bucket_name, prefix = self._parse_gcs_uri(gcs_uri)
        bucket = self.client.bucket(bucket_name)

        blobs = bucket.list_blobs(prefix=prefix)
        for blob in blobs:
            relative_path = blob.name[len(prefix) :].lstrip("/")
            if not relative_path:
                continue

            file_path = os.path.join(local_path, relative_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if os.path.isdir(file_path):
                blob.download_to_file(file_path)
            else:
                blob.download_to_filename(file_path)

        return local_path

    @staticmethod
    def _parse_gcs_uri(uri: str) -> Tuple[str, str]:
        """
        Parse a GCS URI into bucket name and blob path.
        :param uri: GCS URI
        :return: Tuple of bucket name and blob path
        """
        if not uri.startswith("gs://"):
            raise ValueError("URI must start with 'gs://'")

        path = uri[5:]
        bucket_name = path.split("/")[0]
        blob_path = "/".join(path.split("/")[1:])

        return bucket_name, blob_path
