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
from astropulse._generated.models.source_type import SourceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SourceIdentity(BaseModel):
    """
    SourceIdentity
    """ # noqa: E501
    chart_digest: Optional[StrictStr] = Field(default=None, description="The resolved Helm chart digest for helm sources, when available.", alias="chartDigest")
    chart_provenance: Optional[StrictStr] = Field(default=None, description="The Helm chart provenance reference for helm sources, when available.", alias="chartProvenance")
    configured_ref: Optional[StrictStr] = Field(default=None, description="The user-configured branch/tag for git sources (e.g. \"main\"), or the artifact URI for model sources.", alias="configuredRef")
    display: Optional[StrictStr] = Field(default=None, description="The one user-facing identity string: an image reference, a chart's name@version, or a repository source's repository//path@revision.")
    effective_revision: Optional[StrictStr] = Field(default=None, description="The immutable revision actually deployed (the pinned SHA after rollback).", alias="effectiveRevision")
    git_commit_sha: Optional[StrictStr] = Field(default=None, description="The source commit this version came from.", alias="gitCommitSha")
    image_digest: Optional[StrictStr] = Field(default=None, description="The resolved image digest (repository@sha256:...) for image sources.", alias="imageDigest")
    path: Optional[StrictStr] = Field(default=None, description="The directory within the repository the application is deployed from, for repository and yaml sources.")
    source_repository: Optional[StrictStr] = Field(default=None, description="The URL of the repository that commit belongs to.", alias="sourceRepository")
    type: Optional[SourceType] = Field(default=None, description="The kind of source.")
    __properties: ClassVar[List[str]] = ["chartDigest", "chartProvenance", "configuredRef", "display", "effectiveRevision", "gitCommitSha", "imageDigest", "path", "sourceRepository", "type"]

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
        """Create an instance of SourceIdentity from a JSON string"""
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
        """Create an instance of SourceIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chartDigest": obj.get("chartDigest"),
            "chartProvenance": obj.get("chartProvenance"),
            "configuredRef": obj.get("configuredRef"),
            "display": obj.get("display"),
            "effectiveRevision": obj.get("effectiveRevision"),
            "gitCommitSha": obj.get("gitCommitSha"),
            "imageDigest": obj.get("imageDigest"),
            "path": obj.get("path"),
            "sourceRepository": obj.get("sourceRepository"),
            "type": obj.get("type")
        })
        return _obj


