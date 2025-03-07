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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class InfoServiceCapabilities(BaseModel):
    """
    InfoServiceCapabilities
    """ # noqa: E501
    list_tcps: StrictBool = Field(description="Is this motion group able to provide a list of all available TCPs.")
    get_active_tcp: StrictBool = Field(description="Is this motion group able to provide the currently active TCP.")
    get_safety_setup: StrictBool = Field(description="Is this motion group able to get the safety setup.")
    get_motion_group_specification: StrictBool = Field(description="Is this motion group able to provide a motion group specification.")
    list_payloads: StrictBool = Field(description="Is this motion group able to provide a list of all available payloads.")
    get_active_payload: StrictBool = Field(description="Is this motion group able to provide the currently active payload.")
    get_mounting: StrictBool = Field(description="Is this motion group able to provide the mounting information.")
    __properties: ClassVar[List[str]] = ["list_tcps", "get_active_tcp", "get_safety_setup", "get_motion_group_specification", "list_payloads", "get_active_payload", "get_mounting"]

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
        """Create an instance of InfoServiceCapabilities from a JSON string"""
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
        """Create an instance of InfoServiceCapabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "list_tcps": obj.get("list_tcps"),
            "get_active_tcp": obj.get("get_active_tcp"),
            "get_safety_setup": obj.get("get_safety_setup"),
            "get_motion_group_specification": obj.get("get_motion_group_specification"),
            "list_payloads": obj.get("list_payloads"),
            "get_active_payload": obj.get("get_active_payload"),
            "get_mounting": obj.get("get_mounting")
        })
        return _obj


