# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from wandelbots_api_client.models.pyriphery_etcd_etcd_configuration import PyripheryEtcdETCDConfiguration
from wandelbots_api_client.models.pyriphery_hardware_isaac_isaac_configuration import PyripheryHardwareIsaacIsaacConfiguration
from wandelbots_api_client.models.pyriphery_opcua_opcua_configuration import PyripheryOpcuaOPCUAConfiguration
from wandelbots_api_client.models.pyriphery_pyrae_controller_controller_configuration import PyripheryPyraeControllerControllerConfiguration
from wandelbots_api_client.models.pyriphery_pyrae_robot_robot_configuration import PyripheryPyraeRobotRobotConfiguration
from wandelbots_api_client.models.pyriphery_robotics_configurable_collision_scene_configurable_collision_scene_configuration_output import PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput
from wandelbots_api_client.models.pyriphery_robotics_robotcell_timer_configuration import PyripheryRoboticsRobotcellTimerConfiguration
from wandelbots_api_client.models.pyriphery_robotics_simulation_robot_with_view_open3d_configuration import PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration
from wandelbots_api_client.models.pyriphery_robotics_simulation_simulated_io_configuration import PyripheryRoboticsSimulationSimulatedIOConfiguration
from wandelbots_api_client.models.pyriphery_robotics_simulation_simulated_opcua_configuration import PyripheryRoboticsSimulationSimulatedOPCUAConfiguration
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

LISTDEVICES200RESPONSEINNER_ANY_OF_SCHEMAS = ["PyripheryEtcdETCDConfiguration", "PyripheryHardwareIsaacIsaacConfiguration", "PyripheryOpcuaOPCUAConfiguration", "PyripheryPyraeControllerControllerConfiguration", "PyripheryPyraeRobotRobotConfiguration", "PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput", "PyripheryRoboticsRobotcellTimerConfiguration", "PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration", "PyripheryRoboticsSimulationSimulatedIOConfiguration", "PyripheryRoboticsSimulationSimulatedOPCUAConfiguration"]

class ListDevices200ResponseInner(BaseModel):
    """
    ListDevices200ResponseInner
    """

    # data type: PyripheryRoboticsRobotcellTimerConfiguration
    anyof_schema_1_validator: Optional[PyripheryRoboticsRobotcellTimerConfiguration] = None
    # data type: PyripheryEtcdETCDConfiguration
    anyof_schema_2_validator: Optional[PyripheryEtcdETCDConfiguration] = None
    # data type: PyripheryHardwareIsaacIsaacConfiguration
    anyof_schema_3_validator: Optional[PyripheryHardwareIsaacIsaacConfiguration] = None
    # data type: PyripheryPyraeRobotRobotConfiguration
    anyof_schema_4_validator: Optional[PyripheryPyraeRobotRobotConfiguration] = None
    # data type: PyripheryPyraeControllerControllerConfiguration
    anyof_schema_5_validator: Optional[PyripheryPyraeControllerControllerConfiguration] = None
    # data type: PyripheryOpcuaOPCUAConfiguration
    anyof_schema_6_validator: Optional[PyripheryOpcuaOPCUAConfiguration] = None
    # data type: PyripheryRoboticsSimulationSimulatedOPCUAConfiguration
    anyof_schema_7_validator: Optional[PyripheryRoboticsSimulationSimulatedOPCUAConfiguration] = None
    # data type: PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration
    anyof_schema_8_validator: Optional[PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration] = None
    # data type: PyripheryRoboticsSimulationSimulatedIOConfiguration
    anyof_schema_9_validator: Optional[PyripheryRoboticsSimulationSimulatedIOConfiguration] = None
    # data type: PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput
    anyof_schema_10_validator: Optional[PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[PyripheryEtcdETCDConfiguration, PyripheryHardwareIsaacIsaacConfiguration, PyripheryOpcuaOPCUAConfiguration, PyripheryPyraeControllerControllerConfiguration, PyripheryPyraeRobotRobotConfiguration, PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput, PyripheryRoboticsRobotcellTimerConfiguration, PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration, PyripheryRoboticsSimulationSimulatedIOConfiguration, PyripheryRoboticsSimulationSimulatedOPCUAConfiguration]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "PyripheryEtcdETCDConfiguration", "PyripheryHardwareIsaacIsaacConfiguration", "PyripheryOpcuaOPCUAConfiguration", "PyripheryPyraeControllerControllerConfiguration", "PyripheryPyraeRobotRobotConfiguration", "PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput", "PyripheryRoboticsRobotcellTimerConfiguration", "PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration", "PyripheryRoboticsSimulationSimulatedIOConfiguration", "PyripheryRoboticsSimulationSimulatedOPCUAConfiguration" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

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
    def actual_instance_must_validate_anyof(cls, v):
        instance = ListDevices200ResponseInner.model_construct()
        error_messages = []
        # validate data type: PyripheryRoboticsRobotcellTimerConfiguration
        if not isinstance(v, PyripheryRoboticsRobotcellTimerConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryRoboticsRobotcellTimerConfiguration`")
        else:
            return v

        # validate data type: PyripheryEtcdETCDConfiguration
        if not isinstance(v, PyripheryEtcdETCDConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryEtcdETCDConfiguration`")
        else:
            return v

        # validate data type: PyripheryHardwareIsaacIsaacConfiguration
        if not isinstance(v, PyripheryHardwareIsaacIsaacConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryHardwareIsaacIsaacConfiguration`")
        else:
            return v

        # validate data type: PyripheryPyraeRobotRobotConfiguration
        if not isinstance(v, PyripheryPyraeRobotRobotConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryPyraeRobotRobotConfiguration`")
        else:
            return v

        # validate data type: PyripheryPyraeControllerControllerConfiguration
        if not isinstance(v, PyripheryPyraeControllerControllerConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryPyraeControllerControllerConfiguration`")
        else:
            return v

        # validate data type: PyripheryOpcuaOPCUAConfiguration
        if not isinstance(v, PyripheryOpcuaOPCUAConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryOpcuaOPCUAConfiguration`")
        else:
            return v

        # validate data type: PyripheryRoboticsSimulationSimulatedOPCUAConfiguration
        if not isinstance(v, PyripheryRoboticsSimulationSimulatedOPCUAConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryRoboticsSimulationSimulatedOPCUAConfiguration`")
        else:
            return v

        # validate data type: PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration
        if not isinstance(v, PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration`")
        else:
            return v

        # validate data type: PyripheryRoboticsSimulationSimulatedIOConfiguration
        if not isinstance(v, PyripheryRoboticsSimulationSimulatedIOConfiguration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryRoboticsSimulationSimulatedIOConfiguration`")
        else:
            return v

        # validate data type: PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput
        if not isinstance(v, PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ListDevices200ResponseInner with anyOf schemas: PyripheryEtcdETCDConfiguration, PyripheryHardwareIsaacIsaacConfiguration, PyripheryOpcuaOPCUAConfiguration, PyripheryPyraeControllerControllerConfiguration, PyripheryPyraeRobotRobotConfiguration, PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput, PyripheryRoboticsRobotcellTimerConfiguration, PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration, PyripheryRoboticsSimulationSimulatedIOConfiguration, PyripheryRoboticsSimulationSimulatedOPCUAConfiguration. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[PyripheryRoboticsRobotcellTimerConfiguration] = None
        try:
            instance.actual_instance = PyripheryRoboticsRobotcellTimerConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PyripheryEtcdETCDConfiguration] = None
        try:
            instance.actual_instance = PyripheryEtcdETCDConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[PyripheryHardwareIsaacIsaacConfiguration] = None
        try:
            instance.actual_instance = PyripheryHardwareIsaacIsaacConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[PyripheryPyraeRobotRobotConfiguration] = None
        try:
            instance.actual_instance = PyripheryPyraeRobotRobotConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[PyripheryPyraeControllerControllerConfiguration] = None
        try:
            instance.actual_instance = PyripheryPyraeControllerControllerConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[PyripheryOpcuaOPCUAConfiguration] = None
        try:
            instance.actual_instance = PyripheryOpcuaOPCUAConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[PyripheryRoboticsSimulationSimulatedOPCUAConfiguration] = None
        try:
            instance.actual_instance = PyripheryRoboticsSimulationSimulatedOPCUAConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_8_validator: Optional[PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration] = None
        try:
            instance.actual_instance = PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_9_validator: Optional[PyripheryRoboticsSimulationSimulatedIOConfiguration] = None
        try:
            instance.actual_instance = PyripheryRoboticsSimulationSimulatedIOConfiguration.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_10_validator: Optional[PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput] = None
        try:
            instance.actual_instance = PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListDevices200ResponseInner with anyOf schemas: PyripheryEtcdETCDConfiguration, PyripheryHardwareIsaacIsaacConfiguration, PyripheryOpcuaOPCUAConfiguration, PyripheryPyraeControllerControllerConfiguration, PyripheryPyraeRobotRobotConfiguration, PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput, PyripheryRoboticsRobotcellTimerConfiguration, PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration, PyripheryRoboticsSimulationSimulatedIOConfiguration, PyripheryRoboticsSimulationSimulatedOPCUAConfiguration. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], PyripheryEtcdETCDConfiguration, PyripheryHardwareIsaacIsaacConfiguration, PyripheryOpcuaOPCUAConfiguration, PyripheryPyraeControllerControllerConfiguration, PyripheryPyraeRobotRobotConfiguration, PyripheryRoboticsConfigurableCollisionSceneConfigurableCollisionSceneConfigurationOutput, PyripheryRoboticsRobotcellTimerConfiguration, PyripheryRoboticsSimulationRobotWithViewOpen3dConfiguration, PyripheryRoboticsSimulationSimulatedIOConfiguration, PyripheryRoboticsSimulationSimulatedOPCUAConfiguration]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


