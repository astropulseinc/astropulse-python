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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AgentCertificateBundle(BaseModel):
    """
    AgentCertificateBundle
    """ # noqa: E501
    ca_certificate: Optional[StrictStr] = Field(default=None, description="The PEM-encoded certificate authority the agent trusts.", alias="caCertificate")
    certificate: Optional[StrictStr] = Field(default=None, description="The PEM-encoded certificate.")
    expires_at: Optional[StrictStr] = Field(default=None, description="The RFC 3339 time the certificate expires.", alias="expiresAt")
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace of the agent's TLS Secret.")
    previous_certificate_accepted_until: Optional[StrictStr] = Field(default=None, description="The RFC 3339 time the agent's current certificate stops being accepted, unless the agent connects with this one first; empty when the agent had none.", alias="previousCertificateAcceptedUntil")
    secret_name: Optional[StrictStr] = Field(default=None, description="The name of the agent's TLS Secret.", alias="secretName")
    __properties: ClassVar[List[str]] = ["caCertificate", "certificate", "expiresAt", "namespace", "previousCertificateAcceptedUntil", "secretName"]

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
        """Create an instance of AgentCertificateBundle from a JSON string"""
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
        """Create an instance of AgentCertificateBundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "caCertificate": obj.get("caCertificate"),
            "certificate": obj.get("certificate"),
            "expiresAt": obj.get("expiresAt"),
            "namespace": obj.get("namespace"),
            "previousCertificateAcceptedUntil": obj.get("previousCertificateAcceptedUntil"),
            "secretName": obj.get("secretName")
        })
        return _obj


