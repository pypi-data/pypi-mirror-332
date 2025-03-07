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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class IOValue(BaseModel):
    """
    I/O value representation. Depending on the I/O type, only one of the value fields will be set.
    """ # noqa: E501
    io: StrictStr = Field(description="Unique identifier of the I/O.")
    boolean_value: Optional[StrictBool] = Field(default=None, description="Value of a digital I/O. This field is only set if the I/O is of type IO_VALUE_DIGITAL. ")
    integer_value: Optional[StrictStr] = Field(default=None, description="Value of an analog I/O with integer representation. This field is only set if the I/O is of type IO_VALUE_ANALOG_INTEGER.  > The integral value is transmitted as a string to avoid precision loss in conversion to JSON. > We recommend to use int64 for implementation. If you want to interact with int64 in numbers, > there are some JS bigint libraries availible to parse the string into an integral value. ")
    floating_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Value of an analog I/O with floating number representation. This field is only set if the I/O is of type IO_VALUE_ANALOG_FLOATING. ")
    __properties: ClassVar[List[str]] = ["io", "boolean_value", "integer_value", "floating_value"]

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
        """Create an instance of IOValue from a JSON string"""
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
        """Create an instance of IOValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "io": obj.get("io"),
            "boolean_value": obj.get("boolean_value"),
            "integer_value": obj.get("integer_value"),
            "floating_value": obj.get("floating_value")
        })
        return _obj


