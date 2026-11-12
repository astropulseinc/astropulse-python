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
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_connect_step import SelfHostedConnectStep
from astropulse._generated.models.self_hosted_credential_status import SelfHostedCredentialStatus
from astropulse._generated.models.self_hosted_setup_state import SelfHostedSetupState
from astropulse._generated.models.setup_step import SetupStep
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedSetup(BaseModel):
    """
    SelfHostedSetup
    """ # noqa: E501
    account_hint: Optional[StrictStr] = Field(default=None, description="The email address of the Google account the setup was started for; omitted when none was given.", alias="accountHint")
    account_id: Optional[StrictStr] = Field(default=None, description="The AWS account or GCP project.", alias="accountId")
    bucket_name: Optional[StrictStr] = Field(default=None, description="The bucket that holds the cluster's state, the one to name when creating the cluster.", alias="bucketName")
    cleanup_commands: Optional[List[StrictStr]] = Field(default=None, description="The shell commands that remove what the setup creates once no cluster uses it, in order. On GCP they keep a service account or bucket the setup did not create.", alias="cleanupCommands")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster the resources are for.", alias="clusterName")
    commands: Optional[List[StrictStr]] = Field(default=None, description="The shell commands that create the resources, in order (GCP).")
    connect: Optional[SelfHostedConnectStep] = Field(default=None, description="The command that sends the setup's credentials to the vault, or replaces the stored ones once they are there; omitted before the resources can exist.")
    credential_status: Optional[SelfHostedCredentialStatus] = Field(default=None, description="How the cluster's credentials stored in AstroPulse stand; omitted when credential storage is not configured.", alias="credentialStatus")
    note: Optional[StrictStr] = Field(default=None, description="Says what the setup creates, what it costs and how to remove it.")
    notice: Optional[Notice] = Field(default=None, description="Says where the setup stands and the next step to take.")
    outcome: Optional[Outcome] = Field(default=None, description="Blocked when the setup failed, and proceed otherwise.")
    provider: Optional[Provider] = Field(default=None, description="The cloud the resources are in.")
    region: Optional[StrictStr] = Field(default=None, description="Where the resources are created.")
    resources: Optional[Dict[str, StrictStr]] = Field(default=None, description="Names what setup creates, by kind (stack, user, bucket, serviceAccount, ...).")
    shell: Optional[StrictStr] = Field(default=None, description="Where to run `commands` and `cleanupCommands`, such as Cloud Shell.")
    stack_name: Optional[StrictStr] = Field(default=None, description="The CloudFormation stack the setup creates (AWS).", alias="stackName")
    state: Optional[SelfHostedSetupState] = Field(default=None, description="Where the setup stands as a whole.")
    steps: Optional[List[SetupStep]] = Field(default=None, description="The recorded steps, in order.")
    summary: Optional[StrictStr] = Field(default=None, description="Says in one sentence where the setup stands now.")
    __properties: ClassVar[List[str]] = ["accountHint", "accountId", "bucketName", "cleanupCommands", "clusterName", "commands", "connect", "credentialStatus", "note", "notice", "outcome", "provider", "region", "resources", "shell", "stackName", "state", "steps", "summary"]

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
        """Create an instance of SelfHostedSetup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connect
        if self.connect:
            _dict['connect'] = self.connect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_status
        if self.credential_status:
            _dict['credentialStatus'] = self.credential_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notice
        if self.notice:
            _dict['notice'] = self.notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelfHostedSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountHint": obj.get("accountHint"),
            "accountId": obj.get("accountId"),
            "bucketName": obj.get("bucketName"),
            "cleanupCommands": obj.get("cleanupCommands"),
            "clusterName": obj.get("clusterName"),
            "commands": obj.get("commands"),
            "connect": SelfHostedConnectStep.from_dict(obj["connect"]) if obj.get("connect") is not None else None,
            "credentialStatus": SelfHostedCredentialStatus.from_dict(obj["credentialStatus"]) if obj.get("credentialStatus") is not None else None,
            "note": obj.get("note"),
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None,
            "outcome": obj.get("outcome"),
            "provider": obj.get("provider"),
            "region": obj.get("region"),
            "resources": obj.get("resources"),
            "shell": obj.get("shell"),
            "stackName": obj.get("stackName"),
            "state": obj.get("state"),
            "steps": [SetupStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "summary": obj.get("summary")
        })
        return _obj


