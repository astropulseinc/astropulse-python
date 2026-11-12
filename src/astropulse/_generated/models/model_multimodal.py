# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelMultimodal(BaseModel):
    """
    ModelMultimodal
    """ # noqa: E501
    max_audio_clips_per_prompt: Optional[StrictInt] = Field(default=None, description="How many audio clips one request may carry. Named for clips rather than for audio because that is what the runtime counts: one item is one attached clip, whatever its length.", alias="maxAudioClipsPerPrompt")
    max_images_per_prompt: Optional[StrictInt] = Field(default=None, description="How many images one request may carry. The field most vision models need: document and chart understanding routinely sends several pages in one message, and one image is a common runtime default.", alias="maxImagesPerPrompt")
    max_videos_per_prompt: Optional[StrictInt] = Field(default=None, description="How many video clips one request may carry. A clip costs far more than an image -- the runtime samples frames from it and each frame is an image -- so this is the limit to keep small.", alias="maxVideosPerPrompt")
    __properties: ClassVar[List[str]] = ["maxAudioClipsPerPrompt", "maxImagesPerPrompt", "maxVideosPerPrompt"]

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
        """Create an instance of ModelMultimodal from a JSON string"""
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
        """Create an instance of ModelMultimodal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxAudioClipsPerPrompt": obj.get("maxAudioClipsPerPrompt"),
            "maxImagesPerPrompt": obj.get("maxImagesPerPrompt"),
            "maxVideosPerPrompt": obj.get("maxVideosPerPrompt")
        })
        return _obj


