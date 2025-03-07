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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from wandelbots_api_client.models.robot_system_mode import RobotSystemMode
from typing import Optional, Set
from typing_extensions import Self

class ModeChangeResponse(BaseModel):
    """
    Mode change example: * Client sends [jointJogging](jointJogging)](cell=\"..\",...) * Server responds with *current_robot_mode: ROBOT_SYSTEM_MODE_UNDEFINED, by_client_request: true* at the beginning of the transition. * Server responds with *current_robot_mode: ROBOT_SYSTEM_MODE_CONTROL, by_client_request: true* when transition is done.  In case an error happens during execution, e.g. a path would lead to a joint limit violation: * Server responds with *current_robot_mode: ROBOT_SYSTEM_MODE_UNDEFINED, by_client_request: false* * Server responds with *current_robot_mode: ROBOT_SYSTEM_MODE_MONITOR, by_client_request: false*  In case an error happens during connection, e.g. the robot is not reachable: * Client sends [setDefaultMode](setDefaultMode)(mode: MODE_CONTROL) * Server responds with *current_robot_mode:ROBOT_SYSTEM_MODE_UNDEFINED, by_client_request: true* * Server responds with *current_robot_mode:ROBOT_SYSTEM_MODE_DISCONNECT, by_client_request: false* 
    """ # noqa: E501
    current_robot_mode: RobotSystemMode
    by_client_request: StrictBool = Field(description="True if mode change was requested by client.")
    previous_robot_mode: RobotSystemMode
    cause_of_change: StrictStr = Field(description="Details about cause of mode change.")
    __properties: ClassVar[List[str]] = ["current_robot_mode", "by_client_request", "previous_robot_mode", "cause_of_change"]

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
        """Create an instance of ModeChangeResponse from a JSON string"""
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
        """Create an instance of ModeChangeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_robot_mode": obj.get("current_robot_mode"),
            "by_client_request": obj.get("by_client_request"),
            "previous_robot_mode": obj.get("previous_robot_mode"),
            "cause_of_change": obj.get("cause_of_change")
        })
        return _obj


