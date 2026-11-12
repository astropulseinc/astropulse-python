# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.source_type import SourceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterApplication(BaseModel):
    """
    ClusterApplication
    """ # noqa: E501
    created_timestamp: Optional[datetime] = Field(default=None, description="The timestamp when the application was created", alias="createdTimestamp")
    dns_endpoint: Optional[StrictStr] = Field(default=None, description="The DNS endpoint for accessing the application", alias="dnsEndpoint")
    last_updated_timestamp: Optional[datetime] = Field(default=None, description="The timestamp of the last update to the application", alias="lastUpdatedTimestamp")
    name: Optional[StrictStr] = Field(default=None, description="The name of the application")
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace where the application is running in the cluster")
    resource_name: Optional[StrictStr] = Field(default=None, description="The resource name within the cluster", alias="resourceName")
    source_type: Optional[SourceType] = Field(default=None, description="The kind of source the application is deployed from.", alias="sourceType")
    __properties: ClassVar[List[str]] = ["createdTimestamp", "dnsEndpoint", "lastUpdatedTimestamp", "name", "namespace", "resourceName", "sourceType"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClusterApplication from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdTimestamp": obj.get("createdTimestamp"),
            "dnsEndpoint": obj.get("dnsEndpoint"),
            "lastUpdatedTimestamp": obj.get("lastUpdatedTimestamp"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "resourceName": obj.get("resourceName"),
            "sourceType": obj.get("sourceType")
        })
        return _obj


