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
from enum import Enum
from typing_extensions import Self


class IOValueType(str, Enum):
    """
    Data type of the input/output.
    """

    """
    allowed enum values
    """
    IO_VALUE_BOOLEAN = 'IO_VALUE_BOOLEAN'
    IO_VALUE_ANALOG_FLOAT = 'IO_VALUE_ANALOG_FLOAT'
    IO_VALUE_ANALOG_INTEGER = 'IO_VALUE_ANALOG_INTEGER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IOValueType from a JSON string"""
        return cls(json.loads(json_str))


