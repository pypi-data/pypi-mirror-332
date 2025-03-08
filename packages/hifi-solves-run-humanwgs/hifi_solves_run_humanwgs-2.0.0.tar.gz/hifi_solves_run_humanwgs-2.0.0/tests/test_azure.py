import unittest
from unittest.mock import patch
from io import StringIO
import os
import re
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from hifi_solves_run_humanwgs.backends.azure import (
    _get_credential,
    validate_bucket,
    check_file_exists,
    check_file_exists_remote_src,
    transfer_files,
    upload_files,
)

# dest container
storage_account = "bioscoastorage"
container_name = "hifi-solves-humanwgs-test-bucket"
blob_container = f"{storage_account}/{container_name}"

# src container
src_storage_account = "iceberg"
src_container_name = "hifi-solves-humanwgs-test-src-bucket"
blob_src_container = f"{src_storage_account}/{src_container_name}"

credential = _get_credential()
blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account}.blob.core.windows.net",
    credential=credential,
)


class TestGetCredential(unittest.TestCase):
    def test_get_credential_dest(self):
        _ = _get_credential()

    def test_get_credential_src(self):
        _ = _get_credential(target_container="src")

    def test_get_credential_missing_dest_variable(self):
        with patch.dict(os.environ, clear=True):
            with self.assertRaisesRegex(
                SystemExit,
                f"Must set and export the AZURE_STORAGE_SAS_TOKEN env variable",
            ):
                _ = _get_credential(target_container="dest")

    def test_get_credential_missing_src_variable(self):
        with patch.dict(os.environ, clear=True):
            with self.assertRaisesRegex(
                SystemExit,
                f"Must set and export the SOURCE_CONTAINER_SAS_TOKEN env variable",
            ):
                _ = _get_credential(target_container="src")

    def test_credential_expired(self):
        epoch_iso = "1970-01-01T00:00:00Z"
        expired_sas_token = re.sub(
            "se=[^&]*", f"se={epoch_iso}", os.getenv("AZURE_STORAGE_SAS_TOKEN")
        )
        with patch.dict(
            os.environ, {"AZURE_STORAGE_SAS_TOKEN": expired_sas_token}, clear=True
        ):
            with self.assertRaisesRegex(
                SystemExit,
                f"AZURE_STORAGE_SAS_TOKEN is expired; please contact your administrator to get a new token.",
            ):
                _ = _get_credential(target_container="dest")


class TestValidateContainer(unittest.TestCase):
    def test_container_exists(self):
        formatted_container, path_prefix = validate_bucket(blob_container)
        self.assertEqual(formatted_container, blob_container)
        self.assertEqual(path_prefix, None)

    def test_container_does_not_exist(self):
        container = "hifi-solves-test-container"
        with self.assertRaisesRegex(SystemExit, "Authentication failed") as context:
            _, _ = validate_bucket(f"{storage_account}/{container}")

    def test_container_exists_with_path(self):
        formatted_container, path_prefix = validate_bucket(
            f"{blob_container}/hifi-uploads/my_path"
        )
        self.assertEqual(formatted_container, blob_container)
        self.assertEqual(path_prefix, "hifi-uploads/my_path")


class TestCheckFileExists(unittest.TestCase):
    bam_file = "HG002.bam"
    sample_id = "HG002"
    file_type = "bam"
    file_size_bytes = 12

    def setUp(self):
        with open(self.bam_file, "a") as f:
            # 12 bytes
            f.write("hello world\n")

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="my-custom-path/HG002.bam",
        )
        with open(self.bam_file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="hifi-uploads/HG002/bam/HG002.bam",
        )
        with open(self.bam_file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="HG002/bam/HG002.bam",
        )
        with open(self.bam_file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

    def tearDown(self):
        os.remove(self.bam_file)
        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="my-custom-path/HG002.bam",
        )
        blob_client.delete_blob()

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="hifi-uploads/HG002/bam/HG002.bam",
        )
        blob_client.delete_blob()

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob="HG002/bam/HG002.bam",
        )
        blob_client.delete_blob()

    def test_blob_path_files_exist(self):
        path_prefix = None
        remote_file = f"/{blob_container}/my-custom-path/HG002.bam"
        file_exists, remote_path, file_size_bytes = check_file_exists(
            blob_container,
            path_prefix,
            remote_file,
            self.sample_id,
            self.file_type,
        )
        self.assertEqual(file_exists, True)
        self.assertEqual(remote_path, "my-custom-path/HG002.bam")
        self.assertEqual(file_size_bytes, self.file_size_bytes)

    def test_blob_path_files_dont_exist(self):
        path_prefix = "hifi-uploads"
        remote_file = f"/{blob_container}/hifi-uploads/nonexistent/HG002.bam"
        file_exists, remote_path, file_size_bytes = check_file_exists(
            blob_container, path_prefix, remote_file, self.sample_id, self.file_type
        )
        self.assertEqual(file_exists, False)
        self.assertEqual(remote_path, "hifi-uploads/nonexistent/HG002.bam")
        self.assertEqual(file_size_bytes, None)

    def test_blob_path_wrong_container(self):
        path_prefix = "hifi-uploads"
        remote_file = f"/{storage_account}/wrong_container/hifi-uploads/HG002.bam"
        with self.assertRaisesRegex(SystemExit, "is outside of the target container."):
            _, _, _ = check_file_exists(
                blob_container, path_prefix, remote_file, self.sample_id, self.file_type
            )

    def test_local_path_files_exist_with_path_prefix(self):
        path_prefix = "hifi-uploads"
        file_exists, remote_path, file_size_bytes = check_file_exists(
            blob_container, path_prefix, self.bam_file, self.sample_id, self.file_type
        )
        self.assertEqual(file_exists, True)
        self.assertEqual(
            remote_path,
            "hifi-uploads/HG002/bam/HG002.bam",
        )
        self.assertEqual(file_size_bytes, self.file_size_bytes)

    def test_local_path_files_exist_no_path_prefix(self):
        path_prefix = None
        file_exists, remote_path, file_size_bytes = check_file_exists(
            blob_container, path_prefix, self.bam_file, self.sample_id, self.file_type
        )
        self.assertEqual(file_exists, True)
        self.assertEqual(remote_path, "HG002/bam/HG002.bam")
        self.assertEqual(file_size_bytes, self.file_size_bytes)

    def test_local_path_files_dont_exist(self):
        path_prefix = "nonexistent"
        file_exists, remote_path, file_size_bytes = check_file_exists(
            blob_container, path_prefix, self.bam_file, self.sample_id, self.file_type
        )
        self.assertEqual(file_exists, False)
        self.assertEqual(remote_path, "nonexistent/HG002/bam/HG002.bam")
        self.assertEqual(file_size_bytes, None)


# Azure <> Azure - check if files exist at src remote
# Our src storage account doesn't have write, so we can't setup/teardown automatically
# Just using files that are already hosted in this bucket
class TestCheckFileExistsRemoteSrc(unittest.TestCase):
    def test_remote_src_file_exists(self):
        file_path = f"/{blob_src_container}/my/bam/path/_HG002.bam"
        file_exists, file_size_bytes = check_file_exists_remote_src(file_path)
        self.assertEqual(file_exists, True)
        self.assertEqual(file_size_bytes, 23)

    def test_remote_src_files_dont_exist(self):
        file_path = f"/{blob_src_container}/nonexistent/_HG002.bam"
        file_exists, file_size_bytes = check_file_exists_remote_src(file_path)
        self.assertEqual(file_exists, False)
        self.assertEqual(file_size_bytes, None)

    def test_blob_path_wrong_container(self):
        file_path = f"/{src_storage_account}/wrong_container/my/bam/path/_HG002.bam"
        with self.assertRaisesRegex(SystemExit, "✗ Azure configuration error: "):
            _, _ = check_file_exists_remote_src(file_path)


# Azure <> Azure - transfer files from one storage account to another
class TestTransferFiles(unittest.TestCase):
    remote_path = "test/hifi-uploads/HG002.bam"

    def tearDown(self):
        try:
            blob_client = blob_service_client.get_blob_client(
                container=container_name, blob=self.remote_path
            )
            blob_client.delete_blob()
        except ResourceNotFoundError:
            # If the blob or container doesn't exist, ignore the error
            pass

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_succeeded(self, mock_stdout):
        files_to_transfer = {
            f"/{blob_src_container}/my/bam/path/_HG002.bam": self.remote_path
        }
        transfer_files(blob_container, files_to_transfer)
        stdout = mock_stdout.getvalue().strip()
        self.assertRegex(
            stdout,
            "Transferring files from src to target container\n\t✓ _HG002.bam - .*",
        )

    def test_dest_container_does_not_exist(self):
        files_to_transfer = {
            f"/{blob_src_container}/my/bam/path/_HG002.bam": self.remote_path
        }
        with self.assertRaisesRegex(
            SystemExit,
            f"Authentication failed; do src and dest containers exist?",
        ):
            transfer_files(
                f"{storage_account}/nonexistent_container", files_to_transfer
            )

    def test_src_file_does_not_exist(self):
        files_to_transfer = {
            f"/{blob_src_container}/my/nonexistent/path/_HG002.bam": self.remote_path
        }
        with self.assertRaisesRegex(
            SystemExit,
            f"Failed to find remote src file",
        ):
            transfer_files(blob_container, files_to_transfer)


class TestUploadFiles(unittest.TestCase):
    bam_file = "HG002.bam"
    remote_path = "test/hifi-uploads/HG002.bam"

    def setUp(self):
        with open(self.bam_file, "a"):
            pass

    def tearDown(self):
        try:
            os.remove(self.bam_file)
            blob_client = blob_service_client.get_blob_client(
                container=container_name, blob=self.remote_path
            )
            blob_client.delete_blob()
        except ResourceNotFoundError:
            # If the blob or container doesn't exist, ignore the error
            pass

    @patch("sys.stdout", new_callable=StringIO)
    def test_upload_succeeded(self, mock_stdout):
        files_to_upload = {self.bam_file: self.remote_path}
        upload_files(blob_container, files_to_upload)
        stdout = mock_stdout.getvalue().strip()
        self.assertEqual(
            stdout,
            f"Uploading files to target container\n\t✓ {os.path.basename(self.bam_file)}",
        )

    def test_upload_failed(self):
        nonexistent_container = "nonexistent-container"
        files_to_upload = {self.bam_file: self.remote_path}
        with self.assertRaisesRegex(
            SystemExit,
            f"Authentication failed",
        ):
            upload_files(f"{storage_account}/{nonexistent_container}", files_to_upload)


if __name__ == "__main__":
    unittest.main()
