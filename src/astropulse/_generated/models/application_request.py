# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.application_source import ApplicationSource
from astropulse._generated.models.external_access import ExternalAccess
from astropulse._generated.models.sync_type import SyncType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationRequest(BaseModel):
    """
    ApplicationRequest
    """ # noqa: E501
    external_access: Optional[ExternalAccess] = Field(default=None, description="How the application is reached from outside the cluster (optional). For image and model applications, omit it for an internal-only app, or set domain to a verified domain (served at <app>.<domain>) or hostname to an exact hostname under one.", alias="externalAccess")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The application name (required, 1-50 characters, valid DNS name). Must be unique within the organization. Format: lowercase alphanumeric and hyphens.")
    namespace: Optional[Annotated[str, Field(strict=True, max_length=63)]] = Field(default=None, description="The Kubernetes namespace for deployment (optional, max 63 characters). Must be a valid Kubernetes namespace name. If omitted, a namespace named after the application instance is generated and belongs to that one application. A namespace you name here is yours: AstroPulse creates it if it does not exist, deploys into it beside whatever else lives there, and never deletes it or labels it with one application's identity -- several applications may share it. Immutable once set.")
    profile_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The application profile name (required, 1-50 characters, valid DNS name). Immutable once set — cannot be changed after application creation.", alias="profileName")
    source: ApplicationSource = Field(description="Defines where the application artifact is fetched from (required, immutable once set). Must include a valid source type (Image, Helm, Repository, YAML or Model). The source.type presence invariant is enforced by the struct-level validateApplicationRequest in pkg/validator.")
    sync_type: Optional[SyncType] = Field(default=None, description="How the application is kept in sync with its spec. Use Manual only for testing on a live cluster.", alias="syncType")
    __properties: ClassVar[List[str]] = ["externalAccess", "name", "namespace", "profileName", "source", "syncType"]

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
        """Create an instance of ApplicationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of external_access
        if self.external_access:
            _dict['externalAccess'] = self.external_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "externalAccess": ExternalAccess.from_dict(obj["externalAccess"]) if obj.get("externalAccess") is not None else None,
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "profileName": obj.get("profileName"),
            "source": ApplicationSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "syncType": obj.get("syncType")
        })
        return _obj


