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

class FileFileAlternateContentSource(BaseModel):
    """
    Serializer for File alternate content source.
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of Alternate Content Source.")
    last_refreshed: Optional[datetime] = Field(default=None, description="Date of last refresh of AlternateContentSource.")
    paths: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = Field(default=None, description="List of paths that will be appended to the Remote url when searching for content.")
    remote: StrictStr = Field(description="The remote to provide alternate content source.")
    __properties: ClassVar[List[str]] = ["name", "last_refreshed", "paths", "remote"]

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
        """Create an instance of FileFileAlternateContentSource from a JSON string"""
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
        # set to None if last_refreshed (nullable) is None
        # and model_fields_set contains the field
        if self.last_refreshed is None and "last_refreshed" in self.model_fields_set:
            _dict['last_refreshed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileFileAlternateContentSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "last_refreshed": obj.get("last_refreshed"),
            "paths": obj.get("paths"),
            "remote": obj.get("remote")
        })
        return _obj


