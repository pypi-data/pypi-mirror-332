import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
from azure.core.credentials import AzureSasCredential
from azure.core.exceptions import (
    ResourceNotFoundError,
    ClientAuthenticationError,
    ServiceRequestError,
)
from datetime import datetime, timezone
import regex as re


def _get_credential(target_container="dest"):
    """
    Get Azure credentials using a SAS token

    Args:
        target_container (str): Target container to get credentials for; determines which env variable to use to look for the SAS token
                                Available options are ["src", "dest"]. ["dest"]

    Returns:
        credential (AzureSasCredential): credential used to auth with Azure
    """
    if target_container == "dest":
        sas_token_variable_name = "AZURE_STORAGE_SAS_TOKEN"
    elif target_container == "src":
        sas_token_variable_name = "SOURCE_CONTAINER_SAS_TOKEN"
    else:
        raise SystemExit(
            f"Target container {target_container} must be one of ['dest', 'src']"
        )

    sas_token = os.getenv(sas_token_variable_name, None)

    if sas_token is not None:
        try:
            credential = AzureSasCredential(sas_token)
        except ClientAuthenticationError as e:
            raise SystemExit(f"Encountered an issue when retrieving credentials: {e}")
    else:
        raise SystemExit(
            f"Must set and export the {sas_token_variable_name} env variable"
        )

    # Confirm that the SAS token is not expired
    expiry = re.search(
        r"se=([^&]*)",
        sas_token,
    )
    if expiry is None:
        print("[WARN] Failed when checking if SAS token was expired; proceeding anyway")
    else:
        expiry = datetime.fromisoformat(expiry.group(1))
        if expiry < datetime.now(timezone.utc):
            raise SystemExit(
                f"{sas_token_variable_name} is expired; please contact your administrator to get a new token."
            )

    return credential


def validate_bucket(blob_container):
    """
    Confirm that the target upload container exists

    Args:
        blob_container (str): Storage account, container, and optional path within container to upload data to; format <storage_account>/<container>[/<path_prefix>]

    Returns:
        formatted_container_url (str): Formatted container URL with paths stripped
        path_prefix (str): Path within the container to upload files to
    """
    storage_account = blob_container.split("/")[0]
    container_and_path = blob_container.split("/")[1:]
    formatted_container = container_and_path[0]
    path_prefix = (
        None if len(container_and_path) == 1 else "/".join(container_and_path[1:])
    )
    try:
        credential = _get_credential()
        blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account}.blob.core.windows.net",
            credential=credential,
        )
        container_client = blob_service_client.get_container_client(formatted_container)

        # if we're able to list blobs, it means the container exists and is accessible
        next(container_client.list_blobs())
        print("\t✓ Target container exists and is accessible")
        return f"{storage_account}/{formatted_container}", path_prefix

    except StopIteration:
        # if we're able to list blobs but the container is empty, it's still accessible
        print("\t✓ Target container exists and is accessible")
        return f"{storage_account}/{formatted_container}", path_prefix

    except ClientAuthenticationError as e:
        raise SystemExit(f"✗ Authentication failed: {e}")
    except ServiceRequestError as e:
        raise SystemExit(f"✗ Azure configuration error: {e}")
    except ResourceNotFoundError:
        raise SystemExit(
            f"\t✗ Target container {formatted_container} does not exist in storage account {storage_account}."
        )
    except Exception as e:
        raise SystemExit(
            f"\t✗ Something went wrong when checking if the target container {blob_container} exists.\n\t{e}"
        )


def upload_sample_sync_file(raw_data_bucket, sample_sync_file_path):
    """
    Upload the sample sync file to the raw data bucket if it doesn't exist so that Samples are automatically registered in Workbench

    Args:
        raw_data_bucket (str): Storage account, container to upload data to; format <storage_account>/<container>
        sample_sync_file_path (str): Path to the (local) sample sync file to upload
    """
    expected_remote_path = (
        f"/{raw_data_bucket}/{os.path.basename(sample_sync_file_path)}"
    )

    print("Checking for presence of sample sync file")
    file_exists, _, _ = check_file_exists(
        raw_data_bucket, None, expected_remote_path, None, None
    )
    if file_exists is False:
        upload_files(
            raw_data_bucket,
            {sample_sync_file_path: os.path.basename(sample_sync_file_path)},
        )


def check_file_exists(
    blob_container,
    path_prefix,
    file_path,
    sample_id,
    file_type,
):
    """
    Check if a file exists in the container; determine the expected path for remote files
    Args:
        blob_container (str): Storage account, container to upload data to; format <storage_account>/<container>
        path_prefix (str): Path within the container to upload files to
        file_path (str): Local path to the file
        sample_id (str): Unique identifier for sample
        file_type (str): File type (e.g., bam)

    Returns:
        file_exists (bool): True if the file exists at remote; False if it does not
        remote_path (str): Expected path to the file in target container
        file_size_bytes (int): If the file exists, the size of the file in bytes
    """
    storage_account, container = blob_container.split("/")

    file_basename = os.path.basename(file_path)
    file_size_bytes = None

    # File is located in Azure Blob Storage and in the target container
    ## These files can be at different paths within the container than the expected one
    expected_prefix = f"/{storage_account}/{container}/"
    if file_path.startswith(expected_prefix):
        remote_path = file_path.removeprefix(expected_prefix)
    elif file_path.startswith(f"/{storage_account}/") and not file_path.startswith(
        expected_prefix
    ):
        raise SystemExit(
            f"\t✗ Remote file path [{file_path}] is outside of the target container. Please download this file to local storage to allow it to be reuploaded to the target container."
        )
    # File is local; we'll upload to {path_prefix}/{sample_id}/{file_type}/{file_basename}
    else:
        remote_path = f"{path_prefix + '/' if path_prefix else ''}{sample_id}/{file_type}/{file_basename}"

    # Get the file's size if it exists
    try:
        credential = _get_credential()
        blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account}.blob.core.windows.net",
            credential=credential,
        )
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=remote_path
        )
        object_metadata = blob_client.get_blob_properties()
        file_size_bytes = object_metadata["size"]
        print(f"\t✓ {file_basename}")
        return True, remote_path, file_size_bytes
    except (ClientAuthenticationError, ServiceRequestError) as e:
        raise SystemExit(f"✗ Azure configuration error: {e}")
    except ResourceNotFoundError:
        print(f"\t✗ {file_basename}")
        return False, remote_path, file_size_bytes
    except Exception as e:
        raise SystemExit(
            f"\t✗ Something went wrong when checking if the remote file {container}/{remote_path} in storage account {storage_account} exists.\n{e}"
        )


def check_file_exists_remote_src(file_path):
    """
    Check if a file exists in a remote src container
    Args:
        file_path (str): Path of the file in the remote src container

    Returns:
        file_exists (bool): True if the file exists at remote; False if it does not
        file_size_bytes (int): If the file exists, the size of the file in bytes
    """
    split_file_path = file_path.split("/")
    if len(split_file_path) < 4:
        raise SystemExit(
            f"File path shorter than expected; should be in the format [/<storage_account>/<storage_container>/path/to/file.bam]. Got {file_path}"
        )

    storage_account = split_file_path[1]
    container = split_file_path[2]
    file_size_bytes = None

    remote_path = "/".join(split_file_path[3:])

    # Get the file's size if it exists
    try:
        credential = _get_credential(target_container="src")
        blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account}.blob.core.windows.net",
            credential=credential,
        )
        blob_client = blob_service_client.get_blob_client(
            container=container, blob=remote_path
        )
        object_metadata = blob_client.get_blob_properties()
        file_size_bytes = object_metadata["size"]
        return True, file_size_bytes
    except (ClientAuthenticationError, ServiceRequestError) as e:
        raise SystemExit(f"✗ Azure configuration error: {e}")
    except ResourceNotFoundError:
        return False, file_size_bytes
    except Exception as e:
        raise SystemExit(
            f"\t✗ Something went wrong when checking if the remote file {container}/{remote_path} in storage account {storage_account} exists.\n{e}"
        )


def transfer_files(dest_blob_container, files_to_transfer):
    """
    Transfer files from one Azure storage account to another

    Args:
        dest_blob_container (str): Storage account, container to upload data to; format <storage_account>/<container>
        files_to_transfer (dict): Dictionary of files to upload with keys=remote source path to the file (including the /<storage_account>/<container> prefix), values=destination remote path
    """
    if len(files_to_transfer) > 0:
        print("Transferring files from src to target container")
        dest_storage_account, dest_container = dest_blob_container.split("/")

        # Confirm that there is only one source storage account, container
        src_blob_containers = list(
            set(
                [
                    "/".join(prefix.split("/")[1:3])
                    for prefix in files_to_transfer.keys()
                ]
            )
        )
        if len(src_blob_containers) > 1:
            raise SystemExit(
                f"Expected a single source blob container; got {src_blob_containers}"
            )
        else:
            src_blob_container = src_blob_containers[0]

        src_storage_account, src_container = src_blob_container.split("/")

        dest_credential = _get_credential(target_container="dest")

        dest_service_client = BlobServiceClient(
            account_url=f"https://{dest_storage_account}.blob.core.windows.net",
            credential=dest_credential,
            max_single_put_size=4 * 1024 * 1024,
            connection_timeout=600,
        )

        src_sas_token = os.getenv("SOURCE_CONTAINER_SAS_TOKEN", None)
        if src_sas_token is None:
            raise SystemExit(
                "Must define SOURCE_CONTAINER_SAS_TOKEN to transfer from Azure <> Azure"
            )

        for src_remote_path, dest_remote_path in files_to_transfer.items():
            src_blob_name = src_remote_path.removeprefix(f"/{src_blob_container}/")

            source_blob_url = f"https://{src_storage_account}.blob.core.windows.net/{src_container}/{src_blob_name}?{src_sas_token}"

            dest_blob_client = dest_service_client.get_blob_client(
                container=dest_container, blob=dest_remote_path
            )

            try:
                copy_props = dest_blob_client.start_copy_from_url(source_blob_url)
                print(
                    f"\t✓ {os.path.basename(src_blob_name)} - {copy_props['copy_status']}"
                )
            except ClientAuthenticationError:
                raise SystemExit(
                    "Authentication failed; do src and dest containers exist?"
                )
            except ResourceNotFoundError:
                raise SystemExit(f"Failed to find remote src file {src_remote_path}")


def upload_files(blob_container, files_to_upload):
    """
    Upload files to the target container

    Args:
        blob_container (str): Storage account, container to upload data to; format <storage_account>/<container>
        files_to_upload (dict): Dictionary of files to upload with keys=local path to file, values=remote path
    """
    if len(files_to_upload) > 0:
        print("Uploading files to target container")
        storage_account, container = blob_container.split("/")

        credential = _get_credential()
        blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account}.blob.core.windows.net",
            credential=credential,
            max_single_put_size=4 * 1024 * 1024,
            connection_timeout=600,
        )
        container_client = blob_service_client.get_container_client(container)

        for local_path, remote_path in files_to_upload.items():
            try:
                blob_client = container_client.get_blob_client(remote_path)
                with open(local_path, "rb") as data:
                    blob_client.upload_blob(data)
                print(f"\t✓ {os.path.basename(local_path)}")
            except ClientAuthenticationError as e:
                raise SystemExit(f"✗ Authentication failed: {e}")
            except ServiceRequestError as e:
                raise SystemExit(f"✗ Azure configuration error: {e}")
            except ResourceNotFoundError:
                raise SystemExit(
                    f"\t✗ Error uploading file {local_path}: The specified container {container} does not exist."
                )
            except Exception as e:
                raise SystemExit(f"\t✗ Error uploading file {local_path}: {e}")


def get_static_workflow_inputs(
    reference_inputs_bucket,
    workflow_file_outputs_bucket,
    region=None,
    container_registry=None,
):
    """
    Generate the set of static workflow inputs

    Args:
        reference_inputs_bucket (str): Bucket where reference files are located
        workflow_file_outputs_bucket (str): Bucket where workflow output files will be written
        region (str): Region to run the workflow in; does not need to be specified when backend is Azure
        container_registry (str): Alternate container registry to pull workflow images from; defaults to [PacBio's public Quay.io](https://quay.io/organization/pacbio)

    Returns:
        static_inputs (dict): The set of static inputs for the workflow
    """
    reference_inputs_bucket = f"/{reference_inputs_bucket}"
    workflow_file_outputs_bucket = f"/{workflow_file_outputs_bucket}"

    static_inputs = {
        "HumanWGS_wrapper.ref_map_file": f"{reference_inputs_bucket}/dataset/map_files/GRCh38.ref_map.v2p0p0.azure.tsv",
        "HumanWGS_wrapper.backend": "Azure",
        "HumanWGS_wrapper.preemptible": True,
        "HumanWGS_wrapper.workflow_outputs_bucket": workflow_file_outputs_bucket,
    }

    if container_registry is not None:
        static_inputs["HumanWGS_wrapper.container_registry"] = container_registry

    return static_inputs


def generate_inputs_json(
    sample_info,
    reference_inputs_bucket,
    workflow_file_outputs_bucket,
    region=None,
    container_registry=None,
    **kwargs,
):
    """
    Generate the inputs JSON needed to execute a workflow run

    Args:
        sample_info (pd.DataFrame): Sample information
        reference_inputs_bucket (str): Bucket where reference files are located
        workflow_file_outputs_bucket (str): Bucket where workflow output files will be written
        region (str): Region to run the workflow in; does not need to be specified when backend is Azure
        container_registry (str): Alternate container registry to pull workflow images from; defaults to [PacBio's public Quay.io](https://quay.io/organization/pacbio)

    Returns:
        humanwgs_inputs (dict): Inputs JSON with all values filled out
        engine_params (dict): Configuration parameters for the engine
    """
    engine_params = {}

    samples = sample_info.drop(columns=["family_id", "total_file_size_bytes"]).to_dict(
        orient="records"
    )
    samples_no_null_values = [
        {
            key: value
            for key, value in sample.items()
            if isinstance(value, list) or pd.notnull(value)
        }
        for sample in samples
    ]

    family = {
        "family_id": sample_info["family_id"].unique()[0],
        "samples": samples_no_null_values,
    }

    humanwgs_inputs = {
        "HumanWGS_wrapper.family": family,
    }

    static_inputs = get_static_workflow_inputs(
        reference_inputs_bucket,
        workflow_file_outputs_bucket,
        region,
        container_registry,
    )

    humanwgs_inputs.update(static_inputs)

    return humanwgs_inputs, engine_params
