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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.models.pose2 import Pose2
from typing import Optional, Set
from typing_extensions import Self

class FeedbackOutOfWorkspace(BaseModel):
    """
    Requested TCP pose is outside of motion group's workspace.
    """ # noqa: E501
    invalid_tcp_pose: Optional[Pose2] = None
    error_feedback_name: StrictStr
    __properties: ClassVar[List[str]] = ["invalid_tcp_pose", "error_feedback_name"]

    @field_validator('error_feedback_name')
    def error_feedback_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FeedbackOutOfWorkspace']):
            raise ValueError("must be one of enum values ('FeedbackOutOfWorkspace')")
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
        """Create an instance of FeedbackOutOfWorkspace from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invalid_tcp_pose
        if self.invalid_tcp_pose:
            _dict['invalid_tcp_pose'] = self.invalid_tcp_pose.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedbackOutOfWorkspace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invalid_tcp_pose": Pose2.from_dict(obj["invalid_tcp_pose"]) if obj.get("invalid_tcp_pose") is not None else None,
            "error_feedback_name": obj.get("error_feedback_name")
        })
        return _obj


