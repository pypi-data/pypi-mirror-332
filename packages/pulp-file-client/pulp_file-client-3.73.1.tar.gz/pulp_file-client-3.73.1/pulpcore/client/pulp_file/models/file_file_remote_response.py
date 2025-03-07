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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pulpcore.client.pulp_file.models.file_file_remote_response_hidden_fields_inner import FileFileRemoteResponseHiddenFieldsInner
from pulpcore.client.pulp_file.models.policy_enum import PolicyEnum
from typing import Optional, Set
from typing_extensions import Self

class FileFileRemoteResponse(BaseModel):
    """
    Serializer for File Remotes.
    """ # noqa: E501
    pulp_href: Optional[StrictStr] = None
    prn: Optional[StrictStr] = Field(default=None, description="The Pulp Resource Name (PRN).")
    pulp_created: Optional[datetime] = Field(default=None, description="Timestamp of creation.")
    pulp_last_updated: Optional[datetime] = Field(default=None, description="Timestamp of the most recent update of the remote.")
    name: StrictStr = Field(description="A unique name for this remote.")
    url: StrictStr = Field(description="The URL of an external content source.")
    ca_cert: Optional[StrictStr] = Field(default=None, description="A PEM encoded CA certificate used to validate the server certificate presented by the remote server.")
    client_cert: Optional[StrictStr] = Field(default=None, description="A PEM encoded client certificate used for authentication.")
    tls_validation: Optional[StrictBool] = Field(default=None, description="If True, TLS peer validation must be performed.")
    proxy_url: Optional[StrictStr] = Field(default=None, description="The proxy URL. Format: scheme://host:port")
    pulp_labels: Optional[Dict[str, Optional[StrictStr]]] = None
    download_concurrency: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Total number of simultaneous connections. If not set then the default value will be used.")
    max_retries: Optional[StrictInt] = Field(default=None, description="Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.")
    policy: Optional[PolicyEnum] = Field(default=None, description="The policy to use when downloading content. The possible values include: 'immediate', 'on_demand', and 'streamed'. 'immediate' is the default.  * `immediate` - When syncing, download all metadata and content now. * `on_demand` - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * `streamed` - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.")
    total_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    connect_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    sock_connect_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    sock_read_timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.")
    headers: Optional[List[Dict[str, Any]]] = Field(default=None, description="Headers for aiohttp.Clientsession")
    rate_limit: Optional[StrictInt] = Field(default=None, description="Limits requests per second for each concurrent downloader")
    hidden_fields: Optional[List[FileFileRemoteResponseHiddenFieldsInner]] = Field(default=None, description="List of hidden (write only) fields")
    __properties: ClassVar[List[str]] = ["pulp_href", "prn", "pulp_created", "pulp_last_updated", "name", "url", "ca_cert", "client_cert", "tls_validation", "proxy_url", "pulp_labels", "download_concurrency", "max_retries", "policy", "total_timeout", "connect_timeout", "sock_connect_timeout", "sock_read_timeout", "headers", "rate_limit", "hidden_fields"]

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
        """Create an instance of FileFileRemoteResponse from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pulp_href",
            "prn",
            "pulp_created",
            "pulp_last_updated",
            "hidden_fields",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in hidden_fields (list)
        _items = []
        if self.hidden_fields:
            for _item_hidden_fields in self.hidden_fields:
                if _item_hidden_fields:
                    _items.append(_item_hidden_fields.to_dict())
            _dict['hidden_fields'] = _items
        # set to None if ca_cert (nullable) is None
        # and model_fields_set contains the field
        if self.ca_cert is None and "ca_cert" in self.model_fields_set:
            _dict['ca_cert'] = None

        # set to None if client_cert (nullable) is None
        # and model_fields_set contains the field
        if self.client_cert is None and "client_cert" in self.model_fields_set:
            _dict['client_cert'] = None

        # set to None if proxy_url (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_url is None and "proxy_url" in self.model_fields_set:
            _dict['proxy_url'] = None

        # set to None if download_concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.download_concurrency is None and "download_concurrency" in self.model_fields_set:
            _dict['download_concurrency'] = None

        # set to None if max_retries (nullable) is None
        # and model_fields_set contains the field
        if self.max_retries is None and "max_retries" in self.model_fields_set:
            _dict['max_retries'] = None

        # set to None if total_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.total_timeout is None and "total_timeout" in self.model_fields_set:
            _dict['total_timeout'] = None

        # set to None if connect_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.connect_timeout is None and "connect_timeout" in self.model_fields_set:
            _dict['connect_timeout'] = None

        # set to None if sock_connect_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.sock_connect_timeout is None and "sock_connect_timeout" in self.model_fields_set:
            _dict['sock_connect_timeout'] = None

        # set to None if sock_read_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.sock_read_timeout is None and "sock_read_timeout" in self.model_fields_set:
            _dict['sock_read_timeout'] = None

        # set to None if rate_limit (nullable) is None
        # and model_fields_set contains the field
        if self.rate_limit is None and "rate_limit" in self.model_fields_set:
            _dict['rate_limit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileFileRemoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pulp_href": obj.get("pulp_href"),
            "prn": obj.get("prn"),
            "pulp_created": obj.get("pulp_created"),
            "pulp_last_updated": obj.get("pulp_last_updated"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "ca_cert": obj.get("ca_cert"),
            "client_cert": obj.get("client_cert"),
            "tls_validation": obj.get("tls_validation"),
            "proxy_url": obj.get("proxy_url"),
            "pulp_labels": obj.get("pulp_labels"),
            "download_concurrency": obj.get("download_concurrency"),
            "max_retries": obj.get("max_retries"),
            "policy": obj.get("policy"),
            "total_timeout": obj.get("total_timeout"),
            "connect_timeout": obj.get("connect_timeout"),
            "sock_connect_timeout": obj.get("sock_connect_timeout"),
            "sock_read_timeout": obj.get("sock_read_timeout"),
            "headers": obj.get("headers"),
            "rate_limit": obj.get("rate_limit"),
            "hidden_fields": [FileFileRemoteResponseHiddenFieldsInner.from_dict(_item) for _item in obj["hidden_fields"]] if obj.get("hidden_fields") is not None else None
        })
        return _obj


