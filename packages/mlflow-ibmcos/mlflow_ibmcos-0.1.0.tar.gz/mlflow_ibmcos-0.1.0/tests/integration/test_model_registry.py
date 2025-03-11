from mlflow_ibmcos.model_registry import COSModelRegistry
import pytest
import os


@pytest.fixture
def bucket_name():
    return os.getenv("COS_BUCKET_NAME")


def test_registry(bucket_name: str, tmp_path):
    registry = COSModelRegistry(
        bucket=bucket_name,
        model_name="SIMPL",
        model_version="1.0.0",
    )
    path = registry.download_artifacts(
        dst_path=tmp_path,
        delete_other_versions=True
    )
    pass
