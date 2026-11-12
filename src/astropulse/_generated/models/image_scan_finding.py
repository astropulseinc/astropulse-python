# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.scan_findings_severity_counts import ScanFindingsSeverityCounts
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ImageScanFinding(BaseModel):
    """
    ImageScanFinding
    """ # noqa: E501
    container_count: Optional[StrictInt] = Field(default=None, description="How many containers in this workload run this image. Blast radius, never a multiplier on Counts.", alias="containerCount")
    counts: Optional[ScanFindingsSeverityCounts] = Field(default=None, description="The distinct findings in this image, deduplicated by vulnerability, package, and installed version.")
    fixable: Optional[StrictInt] = Field(default=None, description="How many of Counts have a published fixed version — the difference between \"bump the tag\" and \"accept or replace\".")
    image: Optional[StrictStr] = Field(default=None, description="The repository and tag or digest to update when remediating a finding.")
    __properties: ClassVar[List[str]] = ["containerCount", "counts", "fixable", "image"]

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
        """Create an instance of ImageScanFinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of counts
        if self.counts:
            _dict['counts'] = self.counts.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageScanFinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containerCount": obj.get("containerCount"),
            "counts": ScanFindingsSeverityCounts.from_dict(obj["counts"]) if obj.get("counts") is not None else None,
            "fixable": obj.get("fixable"),
            "image": obj.get("image")
        })
        return _obj


