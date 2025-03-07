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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from wandelbots_api_client.models.collider import Collider
from wandelbots_api_client.models.collision_motion_group import CollisionMotionGroup
from wandelbots_api_client.models.motion_command import MotionCommand
from wandelbots_api_client.models.optimizer_setup import OptimizerSetup
from typing import Optional, Set
from typing_extensions import Self

class PlanTrajectoryRequest(BaseModel):
    """
    PlanTrajectoryRequest
    """ # noqa: E501
    robot_setup: OptimizerSetup = Field(description="The robot setup as returned from [getOptimizerConfiguration](getOptimizerConfiguration) endpoint.")
    start_joint_position: List[Union[StrictFloat, StrictInt]]
    motion_commands: List[MotionCommand] = Field(description="List of motion commands. A command consists of a path definition (line, circle, joint_ptp, cartesian_ptp, cubic_spline), blending, and limits override. ")
    static_colliders: Optional[Dict[str, Collider]] = Field(default=None, description="A collection of identifiable colliders.")
    collision_motion_group: Optional[CollisionMotionGroup] = Field(default=None, description="Collision motion group considered during the motion planning. ")
    __properties: ClassVar[List[str]] = ["robot_setup", "start_joint_position", "motion_commands", "static_colliders", "collision_motion_group"]

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
        """Create an instance of PlanTrajectoryRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of robot_setup
        if self.robot_setup:
            _dict['robot_setup'] = self.robot_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in motion_commands (list)
        _items = []
        if self.motion_commands:
            for _item in self.motion_commands:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['motion_commands'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in static_colliders (dict)
        _field_dict = {}
        if self.static_colliders:
            for _key in self.static_colliders:
                if self.static_colliders[_key]:
                    _field_dict[_key] = self.static_colliders[_key].to_dict()
            _dict['static_colliders'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of collision_motion_group
        if self.collision_motion_group:
            _dict['collision_motion_group'] = self.collision_motion_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanTrajectoryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "robot_setup": OptimizerSetup.from_dict(obj["robot_setup"]) if obj.get("robot_setup") is not None else None,
            "start_joint_position": obj.get("start_joint_position"),
            "motion_commands": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                MotionCommand.from_dict(_item) if hasattr(MotionCommand, 'from_dict') else _item
                # <<< End modification
                for _item in obj["motion_commands"]
            ] if obj.get("motion_commands") is not None else None,
            "static_colliders": dict(
                (_k, Collider.from_dict(_v))
                for _k, _v in obj["static_colliders"].items()
            )
            if obj.get("static_colliders") is not None
            else None,
            "collision_motion_group": CollisionMotionGroup.from_dict(obj["collision_motion_group"]) if obj.get("collision_motion_group") is not None else None
        })
        return _obj


