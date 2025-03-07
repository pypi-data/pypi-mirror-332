# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way.  > **Note:** API version 2 is experimental and will experience functional changes. 

    The version of the OpenAPI document: 2.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from wandelbots_api_client.v2.models.collider_shape import ColliderShape
from wandelbots_api_client.v2.models.pose2 import Pose2
from typing import Optional, Set
from typing_extensions import Self

class Collider(BaseModel):
    """
    Defines a collider with a single shape.  A collider is an object that is used for collision detection. It defines the `shape` that is attached with the offset of `pose` to a reference frame.  Use colliders to: - Define the shape of a workpiece. The reference frame is the scene origin. - Define the shape of a link in a motion group. The reference frame is the link coordinate system. - Define the shape of a tool. The reference frame is the flange coordinate system. 
    """ # noqa: E501
    shape: ColliderShape
    pose: Optional[Pose2] = None
    margin: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, description="Increases the shape's size in all dimensions. Applied in [mm]. Can be used to keep a safe distance to the shape.")
    __properties: ClassVar[List[str]] = ["shape", "pose", "margin"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True, exclude_none=True))

    def to_json(self) -> str:
        """
        Returns the JSON representation of the model using alias
        
        Do not use pydantic v2 .model_dump_json(by_alias=True, exclude_unset=True) here!
        It is unable to resolve nested types generated by openapi-generator.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Collider from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shape
        if self.shape:
            _dict['shape'] = self.shape.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pose
        if self.pose:
            _dict['pose'] = self.pose.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Collider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shape": ColliderShape.from_dict(obj["shape"]) if obj.get("shape") is not None else None,
            "pose": Pose2.from_dict(obj["pose"]) if obj.get("pose") is not None else None,
            "margin": obj.get("margin") if obj.get("margin") is not None else 0
        })
        return _obj


