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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OpenPGPKeyringResponse(BaseModel):
    """
    Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.")
    versions_href: Optional[StrictStr] = None
    pulp_labels: Optional[Dict[str, Optional[StrictStr]]] = None
    latest_version_href: Optional[StrictStr] = None
    name: StrictStr = Field(description="A unique name for this repository.")
    description: Optional[StrictStr] = Field(default=None, description="An optional description.")
    retain_repo_versions: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Retain X versions of the repository. Default is null which retains all versions.")
    remote: Optional[StrictStr] = Field(default=None, description="An optional remote to use by default when syncing.")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "versions_href", "pulp_labels", "latest_version_href", "name", "description", "retain_repo_versions", "remote"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OpenPGPKeyringResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
            "versions_href",
            "latest_version_href",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if retain_repo_versions (nullable) is None
        # and model_fields_set contains the field
        if self.retain_repo_versions is None and "retain_repo_versions" in self.model_fields_set:
            _dict['retain_repo_versions'] = None

        # set to None if remote (nullable) is None
        # and model_fields_set contains the field
        if self.remote is None and "remote" in self.model_fields_set:
            _dict['remote'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenPGPKeyringResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "versions_href": obj.get("versions_href"),
            "pulp_labels": obj.get("pulp_labels"),
            "latest_version_href": obj.get("latest_version_href"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "retain_repo_versions": obj.get("retain_repo_versions"),
            "remote": obj.get("remote")
        })
        return _obj


