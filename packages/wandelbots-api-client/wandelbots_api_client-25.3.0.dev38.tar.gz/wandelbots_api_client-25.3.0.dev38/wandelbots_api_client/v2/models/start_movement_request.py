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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.v2.models.direction import Direction
from wandelbots_api_client.v2.models.pause_on_io import PauseOnIO
from wandelbots_api_client.v2.models.set_io import SetIO
from wandelbots_api_client.v2.models.start_on_io import StartOnIO
from typing import Optional, Set
from typing_extensions import Self

class StartMovementRequest(BaseModel):
    """
    Moves the motion group along a trajectory, added via [planTrajectory](planTrajectory) or [planMotion](planMotion). Trajectories can be executed forwards or backwards(\"in reverse\").  Pause the execution with PauseMovementRequest. Resume execution with StartMovementRequest.  Precondition: To start execution, the motion group must be located at the trajectory's start location specified in InitializeMovementRequest. 
    """ # noqa: E501
    message_type: Optional[StrictStr] = Field(default=None, description="Type specifier for server, set automatically. ")
    direction: Direction
    set_ios: Optional[List[SetIO]] = Field(default=None, description="Attaches a list of input/output commands to the trajectory. The inputs/outputs are set to the specified values right after the specified location was reached. If the specified location is located before the start location (forward direction: value is smaller, backward direction: value is bigger), the input/output is not set. ")
    start_on_io: Optional[StartOnIO] = Field(default=None, description="Defines an input/output that is listened to before the movement. Execution starts if the defined comparator evaluates to `true`. ")
    pause_on_io: Optional[PauseOnIO] = Field(default=None, description="Defines an input/output that is listened to during the movement. Execution pauses if the defined comparator evaluates to `true`. ")
    __properties: ClassVar[List[str]] = ["message_type", "direction", "set_ios", "start_on_io", "pause_on_io"]

    @field_validator('message_type')
    def message_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['StartMovementRequest']):
            raise ValueError("must be one of enum values ('StartMovementRequest')")
        return value

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
        """Create an instance of StartMovementRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in set_ios (list)
        _items = []
        if self.set_ios:
            for _item in self.set_ios:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['set_ios'] = _items
        # override the default output from pydantic by calling `to_dict()` of start_on_io
        if self.start_on_io:
            _dict['start_on_io'] = self.start_on_io.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pause_on_io
        if self.pause_on_io:
            _dict['pause_on_io'] = self.pause_on_io.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StartMovementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message_type": obj.get("message_type"),
            "direction": obj.get("direction"),
            "set_ios": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                SetIO.from_dict(_item) if hasattr(SetIO, 'from_dict') else _item
                # <<< End modification
                for _item in obj["set_ios"]
            ] if obj.get("set_ios") is not None else None,
            "start_on_io": StartOnIO.from_dict(obj["start_on_io"]) if obj.get("start_on_io") is not None else None,
            "pause_on_io": PauseOnIO.from_dict(obj["pause_on_io"]) if obj.get("pause_on_io") is not None else None
        })
        return _obj


