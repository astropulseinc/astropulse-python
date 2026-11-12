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
from astropulse._generated.models.cloud_account_status import CloudAccountStatus
from astropulse._generated.models.cloud_connect_attempt_error import CloudConnectAttemptError
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from astropulse._generated.models.provisioner_type import ProvisionerType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AzureConnectStatus(BaseModel):
    """
    AzureConnectStatus
    """ # noqa: E501
    error: Optional[Failure] = Field(default=None, description="Contains any error message if the request failed")
    id: Optional[StrictStr] = Field(default=None, description="The cloud connection ID -- the same value POST /api/v1/cloud/azure/connect returned. Echoed so a client polling several connections can tell responses apart.")
    last_error: Optional[CloudConnectAttemptError] = Field(default=None, description="Why the latest check of the account failed, while one has.", alias="lastError")
    notice: Optional[Notice] = Field(default=None, description="Says where the connection stands and the next step to finish it.")
    outcome: Optional[Outcome] = Field(default=None, description="Blocked when connecting stopped and must be started again, and proceed otherwise.")
    provisioner: Optional[ProvisionerType] = Field(default=None, description="The kind of cluster the connection is for.")
    provisioner_name: Optional[StrictStr] = Field(default=None, description="The provisioner's name for people, such as Amazon EKS.", alias="provisionerName", json_schema_extra={"examples": ["Amazon EKS"]})
    setup_script: Optional[StrictStr] = Field(default=None, description="The generated Azure Cloud Shell setup script", alias="setupScript")
    setup_script_url: Optional[StrictStr] = Field(default=None, description="An optional pre-signed URL for the setup script", alias="setupScriptURL")
    status: Optional[CloudAccountStatus] = Field(default=None, description="How far connecting the cloud account has got. It is `Ready` once connected, and `Failed` or `Denied` when the attempt stopped.")
    tenant_id: Optional[StrictStr] = Field(default=None, description="The Microsoft Entra directory (tenant) ID that owns the subscription, where Azure Cloud Shell must be signed in to run the setup. Empty when it could not be determined.", alias="tenantId")
    __properties: ClassVar[List[str]] = ["error", "id", "lastError", "notice", "outcome", "provisioner", "provisionerName", "setupScript", "setupScriptURL", "status", "tenantId"]

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
        """Create an instance of AzureConnectStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_error
        if self.last_error:
            _dict['lastError'] = self.last_error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notice
        if self.notice:
            _dict['notice'] = self.notice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureConnectStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "id": obj.get("id"),
            "lastError": CloudConnectAttemptError.from_dict(obj["lastError"]) if obj.get("lastError") is not None else None,
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None,
            "outcome": obj.get("outcome"),
            "provisioner": obj.get("provisioner"),
            "provisionerName": obj.get("provisionerName"),
            "setupScript": obj.get("setupScript"),
            "setupScriptURL": obj.get("setupScriptURL"),
            "status": obj.get("status"),
            "tenantId": obj.get("tenantId")
        })
        return _obj


