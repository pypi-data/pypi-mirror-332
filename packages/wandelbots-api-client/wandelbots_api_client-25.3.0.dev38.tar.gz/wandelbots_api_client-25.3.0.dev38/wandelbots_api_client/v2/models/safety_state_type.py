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


class SafetyStateType(str, Enum):
    """
    Current safety state of the configured robot controller. Operation modes in which the attached motion groups can be moved are: - SAFETY_STATE_NORMAL - SAFETY_STATE_REDUCED All other modes are considered as non-operational. 
    """

    """
    allowed enum values
    """
    SAFETY_STATE_UNKNOWN = 'SAFETY_STATE_UNKNOWN'
    SAFETY_STATE_FAULT = 'SAFETY_STATE_FAULT'
    SAFETY_STATE_NORMAL = 'SAFETY_STATE_NORMAL'
    SAFETY_STATE_MASTERING = 'SAFETY_STATE_MASTERING'
    SAFETY_STATE_CONFIRM_SAFETY = 'SAFETY_STATE_CONFIRM_SAFETY'
    SAFETY_STATE_OPERATOR_SAFETY = 'SAFETY_STATE_OPERATOR_SAFETY'
    SAFETY_STATE_PROTECTIVE_STOP = 'SAFETY_STATE_PROTECTIVE_STOP'
    SAFETY_STATE_REDUCED = 'SAFETY_STATE_REDUCED'
    SAFETY_STATE_STOP = 'SAFETY_STATE_STOP'
    SAFETY_STATE_STOP_0 = 'SAFETY_STATE_STOP_0'
    SAFETY_STATE_STOP_1 = 'SAFETY_STATE_STOP_1'
    SAFETY_STATE_STOP_2 = 'SAFETY_STATE_STOP_2'
    SAFETY_STATE_RECOVERY = 'SAFETY_STATE_RECOVERY'
    SAFETY_STATE_DEVICE_EMERGENCY_STOP = 'SAFETY_STATE_DEVICE_EMERGENCY_STOP'
    SAFETY_STATE_ROBOT_EMERGENCY_STOP = 'SAFETY_STATE_ROBOT_EMERGENCY_STOP'
    SAFETY_STATE_VIOLATION = 'SAFETY_STATE_VIOLATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SafetyStateType from a JSON string"""
        return cls(json.loads(json_str))


