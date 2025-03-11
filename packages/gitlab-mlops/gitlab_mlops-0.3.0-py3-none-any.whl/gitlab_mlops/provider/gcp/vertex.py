import os
import tempfile
from typing import List, Optional

from google.cloud import aiplatform

from gitlab_mlops.provider.gcp.base import BaseGCPClient
from gitlab_mlops.provider.gcp.storage import GCSClient


class VertexAIClient(BaseGCPClient):
    def __init__(
        self,
        client,
        location: str = "us-central1",
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.location = location
        self.gcs_client = GCSClient(project_id=self.project_id)

        aiplatform.init(
            project=self.project_id,
            location=self.location,
            credentials=self.credentials_obj,
        )
        self.gitlab = client

    @staticmethod
    def list_models(
        filter_expr: Optional[str] = None, order_by: Optional[str] = None
    ) -> List[aiplatform.Model]:
        """
        List all models in Vertex AI.
        :param filter_expr:
        :param order_by:
        :return:
        """
        return aiplatform.Model.list(filter=filter_expr, order_by=order_by)

    @staticmethod
    def get_model(
        model_id: str,
    ) -> aiplatform.Model:
        """
        Get a model by ID.
        :param model_id: Model ID
        :return: Model object
        """
        return aiplatform.Model(model_name=model_id)

    def download_model_artifacts(
        self,
        model: aiplatform.Model,
        output_dir: Optional[str] = None,
    ) -> str:
        """
        Download model artifacts from GCS.
        :param model: Model object
        :param output_dir: Output directory
        :return: Output directory
        """

        if not model.uri:
            raise ValueError(f"No artifact URI found for model {model.resource_name}")

        if output_dir is None:
            output_dir = tempfile.mkdtemp()
        else:
            os.makedirs(output_dir, exist_ok=True)

        return self.gcs_client.download_from_gcs(model.uri, output_dir)

    def export_model_to_gitlab(
        self,
        model_id: str,
        model_name: Optional[str] = None,
        description: Optional[str] = None,
        download_artifacts: bool = True,
        local_artifacts_dir: Optional[str] = None,
    ):
        """
        Export a model from Vertex AI to GitLab Model Registry.
        :param model_id: Vertex AI model ID
        :param model_name: GitLab model name
        :param description: GitLab model description
        :param download_artifacts: Boolean flag to download model artifacts
        :param local_artifacts_dir: Local directory to download model artifacts
        :return: None
        """
        model = self.get_model(model_id=model_id)

        if not model_name:
            print(f"Model name not provided, defaulting to model name: {model_name}")
        model_name = model_name or model.display_name

        if not description:
            print(
                f"Model description not provided, defaulting to model description: {description}"
            )
        description = description or model.description

        gl_model = self.gitlab.create_model(
            name=model_name,
            description=description,
        )
        print(f"Model {model_name} created in GitLab")

        gl_model_version = gl_model.create_version(
            description=model.version_description,
        )

        print(f"Model version {gl_model_version.version} created in GitLab")

        if not download_artifacts:
            return

        directory = self.download_model_artifacts(
            model=model, output_dir=local_artifacts_dir
        )
        print(f"Model artifacts downloaded to {directory}")

        gl_model_version.log_artifacts(
            local_path=directory,
        )
