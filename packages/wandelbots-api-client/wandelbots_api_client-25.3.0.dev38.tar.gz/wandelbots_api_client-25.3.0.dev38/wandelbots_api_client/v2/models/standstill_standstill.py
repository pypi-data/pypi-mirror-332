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
from wandelbots_api_client.v2.models.robot_controller_state import RobotControllerState
from wandelbots_api_client.v2.models.standstill_reason import StandstillReason
from typing import Optional, Set
from typing_extensions import Self

class StandstillStandstill(BaseModel):
    """
    StandstillStandstill
    """ # noqa: E501
    reason: StandstillReason
    location: Union[StrictFloat, StrictInt]
    state: RobotControllerState = Field(description="Current state of the controller and motion group which came to a standstill.")
    __properties: ClassVar[List[str]] = ["reason", "location", "state"]

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
        """Create an instance of StandstillStandstill from a JSON string"""
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
        """Create an instance of StandstillStandstill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reason": obj.get("reason"),
            "location": obj.get("location"),
            "state": RobotControllerState.from_dict(obj["state"]) if obj.get("state") is not None else None
        })
        return _obj


