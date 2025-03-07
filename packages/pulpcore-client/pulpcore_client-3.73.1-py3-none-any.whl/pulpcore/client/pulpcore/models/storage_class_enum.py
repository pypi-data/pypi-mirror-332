# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StorageClassEnum(str, Enum):
    """
    * `pulpcore.app.models.storage.FileSystem` - Use local filesystem as storage * `storages.backends.s3boto3.S3Boto3Storage` - Use Amazon S3 as storage * `storages.backends.azure_storage.AzureStorage` - Use Azure Blob as storage
    """

    """
    allowed enum values
    """
    PULPCORE_DOT_APP_DOT_MODELS_DOT_STORAGE_DOT_FILE_SYSTEM = 'pulpcore.app.models.storage.FileSystem'
    STORAGES_DOT_BACKENDS_DOT_S3BOTO3_DOT_S3_BOTO3_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STORAGES_DOT_BACKENDS_DOT_AZURE_STORAGE_DOT_AZURE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StorageClassEnum from a JSON string"""
        return cls(json.loads(json_str))


