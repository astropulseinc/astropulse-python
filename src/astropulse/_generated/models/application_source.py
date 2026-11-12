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
from astropulse._generated.models.helm import Helm
from astropulse._generated.models.image import Image
from astropulse._generated.models.model import Model
from astropulse._generated.models.repository import Repository
from astropulse._generated.models.source_type import SourceType
from astropulse._generated.models.yaml import YAML
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationSource(BaseModel):
    """
    ApplicationSource
    """ # noqa: E501
    helm: Optional[Helm] = Field(default=None, description="Configuration, used when type is Helm")
    image: Optional[Image] = Field(default=None, description="Configuration, used when type is Image")
    model: Optional[Model] = Field(default=None, description="Configuration, used when type is Model")
    repository: Optional[Repository] = Field(default=None, description="Configuration, used when type is Repository")
    type: Optional[SourceType] = Field(default=None, description="Specifies the type of source (Image, Helm, YAML, Repository, Model)")
    yaml: Optional[YAML] = Field(default=None, description="Configuration, used when type is YAML")
    __properties: ClassVar[List[str]] = ["helm", "image", "model", "repository", "type", "yaml"]

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
        """Create an instance of ApplicationSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of helm
        if self.helm:
            _dict['helm'] = self.helm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yaml
        if self.yaml:
            _dict['yaml'] = self.yaml.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "helm": Helm.from_dict(obj["helm"]) if obj.get("helm") is not None else None,
            "image": Image.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "model": Model.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "repository": Repository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "type": obj.get("type"),
            "yaml": YAML.from_dict(obj["yaml"]) if obj.get("yaml") is not None else None
        })
        return _obj


