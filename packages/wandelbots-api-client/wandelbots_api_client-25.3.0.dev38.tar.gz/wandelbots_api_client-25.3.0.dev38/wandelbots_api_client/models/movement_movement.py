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
from typing import Any, ClassVar, Dict, List, Union
from wandelbots_api_client.models.robot_controller_state import RobotControllerState
from typing import Optional, Set
from typing_extensions import Self

class MovementMovement(BaseModel):
    """
    MovementMovement
    """ # noqa: E501
    time_to_end: StrictInt = Field(description="Remaining time in milliseconds (ms) to reach the end of the motion.")
    current_location: Union[StrictFloat, StrictInt] = Field(description="Current location of motion group on the trajectory.")
    state: RobotControllerState = Field(description="Current state of the robot controller and moving motion group.")
    __properties: ClassVar[List[str]] = ["time_to_end", "current_location", "state"]

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
        """Create an instance of MovementMovement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovementMovement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time_to_end": obj.get("time_to_end"),
            "current_location": obj.get("current_location"),
            "state": RobotControllerState.from_dict(obj["state"]) if obj.get("state") is not None else None
        })
        return _obj


