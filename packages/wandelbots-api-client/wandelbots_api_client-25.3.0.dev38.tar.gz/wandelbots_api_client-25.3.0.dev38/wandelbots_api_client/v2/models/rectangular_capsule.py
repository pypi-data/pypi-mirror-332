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
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class RectangularCapsule(BaseModel):
    """
    A convex hull around four spheres. Sphere center points in x-y-plane, offset by either combination +-sizeX/+-sizeY. Alternative description: Rectangle in x-y-plane with a 3D padding. 
    """ # noqa: E501
    radius: Union[StrictFloat, StrictInt] = Field(description="The radius of the inner spheres in [mm].")
    sphere_center_distance_x: Union[StrictFloat, StrictInt] = Field(description="The distance of the sphere center in x direction in [mm].")
    sphere_center_distance_y: Union[StrictFloat, StrictInt] = Field(description="The distance of the sphere center in y direction in [mm].")
    __properties: ClassVar[List[str]] = ["radius", "sphere_center_distance_x", "sphere_center_distance_y"]

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
        """Create an instance of RectangularCapsule from a JSON string"""
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
        """Create an instance of RectangularCapsule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "radius": obj.get("radius"),
            "sphere_center_distance_x": obj.get("sphere_center_distance_x"),
            "sphere_center_distance_y": obj.get("sphere_center_distance_y")
        })
        return _obj


