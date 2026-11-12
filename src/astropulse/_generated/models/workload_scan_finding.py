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
from astropulse._generated.models.image_scan_finding import ImageScanFinding
from astropulse._generated.models.scan_finding_owner import ScanFindingOwner
from astropulse._generated.models.scan_findings_severity_counts import ScanFindingsSeverityCounts
from astropulse._generated.models.workload_kind import WorkloadKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class WorkloadScanFinding(BaseModel):
    """
    WorkloadScanFinding
    """ # noqa: E501
    container_count: Optional[StrictInt] = Field(default=None, description="How many scanned containers this workload has — at least len(Images), and more when containers share an image.", alias="containerCount")
    counts: Optional[ScanFindingsSeverityCounts] = Field(default=None, description="Totals over the DISTINCT images in Images, and so equal the sum of their counts exactly. Not a per-container sum: an image running in three containers contributes its findings once.")
    images: Optional[List[ImageScanFinding]] = Field(default=None, description="The per-image breakdown Counts is built from. It is omitted when an image breakdown is unavailable.")
    kind: Optional[WorkloadKind] = Field(default=None, description="The kind of Kubernetes object that runs the workload; absent for one the API does not define.")
    name: Optional[StrictStr] = None
    namespace: Optional[StrictStr] = None
    owner: Optional[ScanFindingOwner] = Field(default=None, description="Identifies the application or add-on associated with this workload. It is absent when no public association is known.")
    __properties: ClassVar[List[str]] = ["containerCount", "counts", "images", "kind", "name", "namespace", "owner"]

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
        """Create an instance of WorkloadScanFinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadScanFinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containerCount": obj.get("containerCount"),
            "counts": ScanFindingsSeverityCounts.from_dict(obj["counts"]) if obj.get("counts") is not None else None,
            "images": [ImageScanFinding.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "owner": ScanFindingOwner.from_dict(obj["owner"]) if obj.get("owner") is not None else None
        })
        return _obj


