# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wandelbots_api_client.models.collision_contact import CollisionContact
from typing import Optional, Set
from typing_extensions import Self

class Collision(BaseModel):
    """
    Collision
    """ # noqa: E501
    id_of_a: Optional[StrictStr] = None
    id_of_b: Optional[StrictStr] = None
    id_of_world: Optional[StrictStr] = None
    normal_world_on_b: Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=3, max_length=3)]] = Field(default=None, description="Describes a position in 3D space. A three-dimensional vector [x, y, z] with double precision. ")
    position_on_a: Optional[CollisionContact] = None
    position_on_b: Optional[CollisionContact] = None
    __properties: ClassVar[List[str]] = ["id_of_a", "id_of_b", "id_of_world", "normal_world_on_b", "position_on_a", "position_on_b"]

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
        """Create an instance of Collision from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of position_on_a
        if self.position_on_a:
            _dict['position_on_a'] = self.position_on_a.to_dict()
        # override the default output from pydantic by calling `to_dict()` of position_on_b
        if self.position_on_b:
            _dict['position_on_b'] = self.position_on_b.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Collision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id_of_a": obj.get("id_of_a"),
            "id_of_b": obj.get("id_of_b"),
            "id_of_world": obj.get("id_of_world"),
            "normal_world_on_b": obj.get("normal_world_on_b"),
            "position_on_a": CollisionContact.from_dict(obj["position_on_a"]) if obj.get("position_on_a") is not None else None,
            "position_on_b": CollisionContact.from_dict(obj["position_on_b"]) if obj.get("position_on_b") is not None else None
        })
        return _obj


