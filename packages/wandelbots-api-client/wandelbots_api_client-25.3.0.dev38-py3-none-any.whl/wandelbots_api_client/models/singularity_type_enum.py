# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SingularityTypeEnum(str, Enum):
    """
    SingularityTypeEnum
    """

    """
    allowed enum values
    """
    WRIST = 'WRIST'
    ELBOW = 'ELBOW'
    SHOULDER = 'SHOULDER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SingularityTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


