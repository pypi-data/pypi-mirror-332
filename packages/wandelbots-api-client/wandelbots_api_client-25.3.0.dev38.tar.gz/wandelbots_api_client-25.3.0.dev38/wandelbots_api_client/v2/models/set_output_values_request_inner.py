# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way.  > **Note:** API version 2 is experimental and will experience functional changes. 

    The version of the OpenAPI document: 2.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from wandelbots_api_client.v2.models.io_boolean_value import IOBooleanValue
from wandelbots_api_client.v2.models.io_float_value import IOFloatValue
from wandelbots_api_client.v2.models.io_integer_value import IOIntegerValue
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SETOUTPUTVALUESREQUESTINNER_ONE_OF_SCHEMAS = ["IOBooleanValue", "IOFloatValue", "IOIntegerValue"]

class SetOutputValuesRequestInner(BaseModel):
    """
    SetOutputValuesRequestInner
    """
    # data type: IOBooleanValue
    oneof_schema_1_validator: Optional[IOBooleanValue] = None
    # data type: IOIntegerValue
    oneof_schema_2_validator: Optional[IOIntegerValue] = None
    # data type: IOFloatValue
    oneof_schema_3_validator: Optional[IOFloatValue] = None
    actual_instance: Optional[Union[IOBooleanValue, IOFloatValue, IOIntegerValue]] = None
    one_of_schemas: Set[str] = { "IOBooleanValue", "IOFloatValue", "IOIntegerValue" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SetOutputValuesRequestInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: IOBooleanValue
        if not isinstance(v, IOBooleanValue):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IOBooleanValue`")
        else:
            match += 1
        # validate data type: IOIntegerValue
        if not isinstance(v, IOIntegerValue):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IOIntegerValue`")
        else:
            match += 1
        # validate data type: IOFloatValue
        if not isinstance(v, IOFloatValue):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IOFloatValue`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SetOutputValuesRequestInner with oneOf schemas: IOBooleanValue, IOFloatValue, IOIntegerValue. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SetOutputValuesRequestInner with oneOf schemas: IOBooleanValue, IOFloatValue, IOIntegerValue. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into IOBooleanValue
        try:
            instance.actual_instance = IOBooleanValue.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IOIntegerValue
        try:
            instance.actual_instance = IOIntegerValue.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IOFloatValue
        try:
            instance.actual_instance = IOFloatValue.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SetOutputValuesRequestInner with oneOf schemas: IOBooleanValue, IOFloatValue, IOIntegerValue. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SetOutputValuesRequestInner with oneOf schemas: IOBooleanValue, IOFloatValue, IOIntegerValue. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], IOBooleanValue, IOFloatValue, IOIntegerValue]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


