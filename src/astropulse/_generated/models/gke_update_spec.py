# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.gke_image_type import GKEImageType
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel
from astropulse._generated.models.maintenance_window import MaintenanceWindow
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GKEUpdateSpec(BaseModel):
    """
    GKEUpdateSpec
    """ # noqa: E501
    authorized_networks: Optional[Annotated[List[StrictStr], Field(max_length=50)]] = Field(default=None, description="CIDR blocks allowed to access the Kubernetes API server (optional, max 50 entries). Each entry must be a valid CIDR block. Pass empty array to allow unrestricted access.", alias="authorizedNetworks")
    credentials: Optional[Credentials] = Field(default=None, description="Replaces the cluster's stored static credentials when it carries data; omitted, or with the type and no data, it keeps them.")
    image_type: Optional[GKEImageType] = Field(default=None, description="The operating system image of the node pools. Omitted keeps it; changing it replaces the nodes.", alias="imageType")
    maintenance_window: Optional[MaintenanceWindow] = Field(default=None, description="The daily window GKE runs automatic maintenance in. Omitted keeps it.", alias="maintenanceWindow")
    release_channel: Optional[GKEReleaseChannel] = Field(default=None, description="The release channel the cluster takes its Kubernetes versions from. Omitted keeps it.", alias="releaseChannel")
    __properties: ClassVar[List[str]] = ["authorizedNetworks", "credentials", "imageType", "maintenanceWindow", "releaseChannel"]

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
        """Create an instance of GKEUpdateSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maintenance_window
        if self.maintenance_window:
            _dict['maintenanceWindow'] = self.maintenance_window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GKEUpdateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorizedNetworks": obj.get("authorizedNetworks"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "imageType": obj.get("imageType"),
            "maintenanceWindow": MaintenanceWindow.from_dict(obj["maintenanceWindow"]) if obj.get("maintenanceWindow") is not None else None,
            "releaseChannel": obj.get("releaseChannel")
        })
        return _obj


