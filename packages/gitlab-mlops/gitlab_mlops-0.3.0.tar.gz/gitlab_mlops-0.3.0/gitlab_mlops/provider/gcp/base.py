import abc
import json
import os
from typing import Dict, Optional

import google.auth
from google.oauth2 import service_account


class BaseGCPClient(abc.ABC):
    """
    Base class for GCP clients handling authentication and common utilities.
    """

    def __init__(
        self,
        project_id: str,
        credentials: Optional[Dict] = None,
        credentials_path: Optional[str] = None,
    ):
        self.project_id = project_id
        self.credentials_obj = self._initialize_credentials(
            credentials=credentials, credentials_path=credentials_path
        )

    @staticmethod
    def _initialize_credentials(
        credentials: Optional[Dict], credentials_path: Optional[str]
    ) -> Optional[service_account.Credentials]:
        """
        Initialize GCP credentials from various sources.

        The order of precedence is:
        1. Explicit credentials dict
        2. Credentials file path
        3. GOOGLE_APPLICATION_CREDENTIALS environment variable
        4. Default credentials

        :param credentials: Credentials json dictionary
        :param credentials_path: Path to credentials file
        :return: Credentials object or None for default credentials
        """
        if credentials:
            print(f"Using credentials from dict: {credentials}")
            return service_account.Credentials.from_service_account_info(credentials)

        if credentials_path:
            print(f"Using credentials from file: {credentials_path}")
            return service_account.Credentials.from_service_account_file(
                credentials_path
            )

        if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            print("Using credentials from GOOGLE_APPLICATION_CREDENTIALS")
            return None

        try:
            print("Using default credentials")
            creds, _ = google.auth.default()
            return creds
        except Exception as e:
            print(f"Error loading default credentials: {e}")
            return None

    @staticmethod
    def load_credentials_from_file(file_path: str) -> Dict:
        """
        Load credentials from a JSON file.
        :param file_path: Path to credentials file.
        :return: Credentials dictionary.
        """
        with open(file_path, "r") as f:
            return json.load(f)
