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
from wandelbots_api_client.v2.models.initialize_jogging_response import InitializeJoggingResponse
from wandelbots_api_client.v2.models.jogging_error_response import JoggingErrorResponse
from wandelbots_api_client.v2.models.jogging_response import JoggingResponse
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

EXECUTEJOGGINGRESPONSE_ONE_OF_SCHEMAS = ["InitializeJoggingResponse", "JoggingErrorResponse", "JoggingResponse"]

class ExecuteJoggingResponse(BaseModel):
    """
    ExecuteJoggingResponse
    """
    # data type: InitializeJoggingResponse
    oneof_schema_1_validator: Optional[InitializeJoggingResponse] = None
    # data type: JoggingResponse
    oneof_schema_2_validator: Optional[JoggingResponse] = None
    # data type: JoggingErrorResponse
    oneof_schema_3_validator: Optional[JoggingErrorResponse] = None
    actual_instance: Optional[Union[InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse]] = None
    one_of_schemas: Set[str] = { "InitializeJoggingResponse", "JoggingErrorResponse", "JoggingResponse" }

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
        instance = ExecuteJoggingResponse.model_construct()
        error_messages = []
        match = 0
        # validate data type: InitializeJoggingResponse
        if not isinstance(v, InitializeJoggingResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InitializeJoggingResponse`")
        else:
            match += 1
        # validate data type: JoggingResponse
        if not isinstance(v, JoggingResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JoggingResponse`")
        else:
            match += 1
        # validate data type: JoggingErrorResponse
        if not isinstance(v, JoggingErrorResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JoggingErrorResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ExecuteJoggingResponse with oneOf schemas: InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ExecuteJoggingResponse with oneOf schemas: InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse. Details: " + ", ".join(error_messages))
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

        # deserialize data into InitializeJoggingResponse
        try:
            instance.actual_instance = InitializeJoggingResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JoggingResponse
        try:
            instance.actual_instance = JoggingResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JoggingErrorResponse
        try:
            instance.actual_instance = JoggingErrorResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ExecuteJoggingResponse with oneOf schemas: InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ExecuteJoggingResponse with oneOf schemas: InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], InitializeJoggingResponse, JoggingErrorResponse, JoggingResponse]]:
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


