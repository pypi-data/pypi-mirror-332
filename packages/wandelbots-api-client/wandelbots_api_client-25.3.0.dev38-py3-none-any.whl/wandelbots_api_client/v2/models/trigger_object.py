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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.v2.models.create_trigger_request_config import CreateTriggerRequestConfig
from wandelbots_api_client.v2.models.trigger_type import TriggerType
from typing import Optional, Set
from typing_extensions import Self

class TriggerObject(BaseModel):
    """
    TriggerObject
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The identifier of the trigger.")
    program_id: StrictStr = Field(description="The identifier of the program to run when the trigger condition is met.")
    enabled: StrictBool = Field(description="Indicates whether the trigger is enabled or not.")
    type: TriggerType
    config: CreateTriggerRequestConfig
    created_at: datetime = Field(description="ISO 8601 date-time format when the trigger was created.")
    last_updated_at: datetime = Field(description="ISO 8601 date-time format when the trigger was last updated.")
    program_runs: Optional[List[StrictStr]] = Field(default=None, description="The program runs that were triggered by this trigger.")
    __properties: ClassVar[List[str]] = ["id", "program_id", "enabled", "type", "config", "created_at", "last_updated_at", "program_runs"]

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
        """Create an instance of TriggerObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TriggerObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "program_id": obj.get("program_id"),
            "enabled": obj.get("enabled"),
            "type": obj.get("type"),
            "config": CreateTriggerRequestConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "created_at": obj.get("created_at"),
            "last_updated_at": obj.get("last_updated_at"),
            "program_runs": obj.get("program_runs")
        })
        return _obj


