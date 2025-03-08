WORKBENCH_URL = "workbench.omics.ai"
WORKFLOW_NAME = "Human Whole Genome Sequencing (HiFi Solves)"
WORKFLOW_VERSION = "v2.1.1"
WORKFLOW_SUB_VERSION = "v0.0.1"
DERIVED_WORKFLOW_VERSION = f"{WORKFLOW_VERSION}_{WORKFLOW_SUB_VERSION}"

# AWS account where containers are hosted
AWS_CONTAINER_REGISTRY_ACCOUNT = "635186400088"

# States from https://github.com/DNAstack/dnastack-client/blob/main/dnastack/client/workbench/ewes/models.py
WORKFLOW_STATES = {
    "PREPROCESSING": "RUNNING",
    "UNKNOWN": "RUNNING",
    "QUEUED": "RUNNING",
    "INITIALIZING": "RUNNING",
    "RUNNING": "RUNNING",
    "PAUSED": "RUNNING",
    "CANCELING": "FAILED",
    "COMPLETE": "SUCCEEDED",
    "EXECUTOR_ERROR": "FAILED",
    "SYSTEM_ERROR": "FAILED",
    "CANCELED": "FAILED",
    "COMPLETE_WITH_ERRORS": "FAILED",
    "PREPROCESSING_ERROR": "FAILED",
}
