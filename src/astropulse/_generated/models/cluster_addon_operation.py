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
from astropulse._generated.models.cluster_addon_accelerator_readiness import ClusterAddonAcceleratorReadiness
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration
from astropulse._generated.models.cluster_addon_operation_metadata import ClusterAddonOperationMetadata
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus
from astropulse._generated.models.cluster_addon_tls_readiness import ClusterAddonTLSReadiness
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonOperation(BaseModel):
    """
    ClusterAddonOperation
    """ # noqa: E501
    accelerator: Optional[ClusterAddonAcceleratorReadiness] = Field(default=None, description="Accompanies an accelerator-metrics apply: what this cluster has for the exporter to measure. See ClusterAddonAcceleratorReadiness.")
    configuration: Optional[ClusterAddonConfiguration] = Field(default=None, description="The settings the apply would run with, every one left out filled in as a read of the add-on shows it; present on a dry run only.")
    message: Optional[StrictStr] = Field(default=None, description="Says what happened, in words to show a person.")
    metadata: Optional[ClusterAddonOperationMetadata] = Field(default=None, description="Carries anything the operation wants to say beyond its status.")
    notices: Optional[List[Notice]] = Field(default=None, description="What an apply, or its dry run, tells you about it, including why it started nothing.")
    outcome: Optional[Outcome] = Field(default=None, description="The decision on the apply: proceed, or blocked when a notice blocks it.")
    status: Optional[ClusterAddonStatus] = Field(default=None, description="Where the operation got to.")
    title: Optional[StrictStr] = Field(default=None, description="The result as a headline to show; for a dry run, whether it passed.")
    tls: Optional[ClusterAddonTLSReadiness] = Field(default=None, description="Accompanies a cert-manager apply: what the applied configuration can mint on this cluster. See ClusterAddonTLSReadiness.")
    __properties: ClassVar[List[str]] = ["accelerator", "configuration", "message", "metadata", "notices", "outcome", "status", "title", "tls"]

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
        """Create an instance of ClusterAddonOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accelerator
        if self.accelerator:
            _dict['accelerator'] = self.accelerator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": ClusterAddonAcceleratorReadiness.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "configuration": ClusterAddonConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "message": obj.get("message"),
            "metadata": ClusterAddonOperationMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "outcome": obj.get("outcome"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "tls": ClusterAddonTLSReadiness.from_dict(obj["tls"]) if obj.get("tls") is not None else None
        })
        return _obj


