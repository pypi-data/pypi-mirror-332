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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PatchedUser(BaseModel):
    """
    Serializer for User.
    """ # noqa: E501
    username: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=150)]] = Field(default=None, description="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    password: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Users password. Set to ``null`` to disable password authentication.")
    first_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="First name")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="Last name")
    email: Optional[StrictStr] = Field(default=None, description="Email address")
    is_staff: Optional[StrictBool] = Field(default=False, description="Designates whether the user can log into this admin site.")
    is_active: Optional[StrictBool] = Field(default=True, description="Designates whether this user should be treated as active.")
    __properties: ClassVar[List[str]] = ["username", "password", "first_name", "last_name", "email", "is_staff", "is_active"]

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
        """Create an instance of PatchedUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "username": obj.get("username"),
            "password": obj.get("password"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "email": obj.get("email"),
            "is_staff": obj.get("is_staff") if obj.get("is_staff") is not None else False,
            "is_active": obj.get("is_active") if obj.get("is_active") is not None else True
        })
        return _obj


