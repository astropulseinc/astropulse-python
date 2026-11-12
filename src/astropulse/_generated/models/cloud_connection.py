# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.account_setup import AccountSetup
from astropulse._generated.models.cloud_connection_state import CloudConnectionState
from astropulse._generated.models.next_step import NextStep
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_type import ProvisionerType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CloudConnection(BaseModel):
    """
    CloudConnection
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, description="The cloud account connected; omitted for callers who are not organization admins.", alias="accountId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster the connection was made for.", alias="clusterName")
    connected_at: Optional[StrictStr] = Field(default=None, description="When the connection's setup first finished; set in the connections listing.", alias="connectedAt")
    connection_id: Optional[StrictStr] = Field(default=None, description="The same ID the connect endpoint returns for this connection; omitted for callers who are not organization admins.", alias="connectionId")
    created_at: Optional[StrictStr] = Field(default=None, description="When the connection's setup started; set in the connections listing.", alias="createdAt")
    development_credentials: Optional[StrictBool] = Field(default=None, description="True on a local development platform that can use this account with its own credentials, so a cluster can be created here without connecting it. State still says whether the account is connected.", alias="developmentCredentials")
    message: Optional[StrictStr] = Field(default=None, description="Says what the state means.")
    next_step: Optional[NextStep] = Field(default=None, description="What to do in the cloud account to reach connected, when there is a step to take; for callers who are not organization admins, it asks an admin.", alias="nextStep")
    provider: Optional[Provider] = Field(default=None, description="The cloud the connection is to.")
    provisioner: Optional[ProvisionerType] = Field(default=None, description="The kind of cluster the connection is for; omitted when unknown.")
    provisioner_name: Optional[StrictStr] = Field(default=None, description="The provisioner's name for people, such as Amazon EKS; omitted when unknown.", alias="provisionerName", json_schema_extra={"examples": ["Amazon EKS"]})
    region: Optional[StrictStr] = Field(default=None, description="The region the connection was made in; omitted for callers who are not organization admins.")
    required_template_version: Optional[StrictInt] = Field(default=None, description="The setup template version AstroPulse needs.", alias="requiredTemplateVersion")
    resource_group: Optional[StrictStr] = Field(default=None, description="The Azure resource group the connection was made for.", alias="resourceGroup")
    setup: Optional[AccountSetup] = Field(default=None, description="The one-time setup this connection comes from.")
    state: Optional[CloudConnectionState] = Field(default=None, description="How the connection stands now.")
    template_version: Optional[StrictInt] = Field(default=None, description="The setup template version the account runs; omitted when unknown.", alias="templateVersion")
    verified_at: Optional[StrictStr] = Field(default=None, description="When a connection check last reached the account and got an answer.", alias="verifiedAt")
    __properties: ClassVar[List[str]] = ["accountId", "clusterName", "connectedAt", "connectionId", "createdAt", "developmentCredentials", "message", "nextStep", "provider", "provisioner", "provisionerName", "region", "requiredTemplateVersion", "resourceGroup", "setup", "state", "templateVersion", "verifiedAt"]

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
        """Create an instance of CloudConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of next_step
        if self.next_step:
            _dict['nextStep'] = self.next_step.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "clusterName": obj.get("clusterName"),
            "connectedAt": obj.get("connectedAt"),
            "connectionId": obj.get("connectionId"),
            "createdAt": obj.get("createdAt"),
            "developmentCredentials": obj.get("developmentCredentials"),
            "message": obj.get("message"),
            "nextStep": NextStep.from_dict(obj["nextStep"]) if obj.get("nextStep") is not None else None,
            "provider": obj.get("provider"),
            "provisioner": obj.get("provisioner"),
            "provisionerName": obj.get("provisionerName"),
            "region": obj.get("region"),
            "requiredTemplateVersion": obj.get("requiredTemplateVersion"),
            "resourceGroup": obj.get("resourceGroup"),
            "setup": obj.get("setup"),
            "state": obj.get("state"),
            "templateVersion": obj.get("templateVersion"),
            "verifiedAt": obj.get("verifiedAt")
        })
        return _obj


