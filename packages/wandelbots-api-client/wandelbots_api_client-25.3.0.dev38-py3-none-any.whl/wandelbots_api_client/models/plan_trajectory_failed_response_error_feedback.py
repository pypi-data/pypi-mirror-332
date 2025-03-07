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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from wandelbots_api_client.models.feedback_collision import FeedbackCollision
from wandelbots_api_client.models.feedback_joint_limit_exceeded import FeedbackJointLimitExceeded
from wandelbots_api_client.models.feedback_out_of_workspace import FeedbackOutOfWorkspace
from wandelbots_api_client.models.feedback_singularity import FeedbackSingularity
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

PLANTRAJECTORYFAILEDRESPONSEERRORFEEDBACK_ONE_OF_SCHEMAS = ["FeedbackCollision", "FeedbackJointLimitExceeded", "FeedbackOutOfWorkspace", "FeedbackSingularity"]

class PlanTrajectoryFailedResponseErrorFeedback(BaseModel):
    """
    PlanTrajectoryFailedResponseErrorFeedback
    """
    # data type: FeedbackOutOfWorkspace
    oneof_schema_1_validator: Optional[FeedbackOutOfWorkspace] = None
    # data type: FeedbackSingularity
    oneof_schema_2_validator: Optional[FeedbackSingularity] = None
    # data type: FeedbackJointLimitExceeded
    oneof_schema_3_validator: Optional[FeedbackJointLimitExceeded] = None
    # data type: FeedbackCollision
    oneof_schema_4_validator: Optional[FeedbackCollision] = None
    actual_instance: Optional[Union[FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity]] = None
    one_of_schemas: Set[str] = { "FeedbackCollision", "FeedbackJointLimitExceeded", "FeedbackOutOfWorkspace", "FeedbackSingularity" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
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
    def actual_instance_must_validate_oneof(cls, v):
        instance = PlanTrajectoryFailedResponseErrorFeedback.model_construct()
        error_messages = []
        match = 0
        # validate data type: FeedbackOutOfWorkspace
        if not isinstance(v, FeedbackOutOfWorkspace):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeedbackOutOfWorkspace`")
        else:
            match += 1
        # validate data type: FeedbackSingularity
        if not isinstance(v, FeedbackSingularity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeedbackSingularity`")
        else:
            match += 1
        # validate data type: FeedbackJointLimitExceeded
        if not isinstance(v, FeedbackJointLimitExceeded):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeedbackJointLimitExceeded`")
        else:
            match += 1
        # validate data type: FeedbackCollision
        if not isinstance(v, FeedbackCollision):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FeedbackCollision`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PlanTrajectoryFailedResponseErrorFeedback with oneOf schemas: FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PlanTrajectoryFailedResponseErrorFeedback with oneOf schemas: FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity. Details: " + ", ".join(error_messages))
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

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("error_feedback_name")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `error_feedback_name` in the input.")

        # check if data type is `FeedbackCollision`
        if _data_type == "FeedbackCollision":
            instance.actual_instance = FeedbackCollision.from_json(json_str)
            return instance

        # check if data type is `FeedbackJointLimitExceeded`
        if _data_type == "FeedbackJointLimitExceeded":
            instance.actual_instance = FeedbackJointLimitExceeded.from_json(json_str)
            return instance

        # check if data type is `FeedbackOutOfWorkspace`
        if _data_type == "FeedbackOutOfWorkspace":
            instance.actual_instance = FeedbackOutOfWorkspace.from_json(json_str)
            return instance

        # check if data type is `FeedbackSingularity`
        if _data_type == "FeedbackSingularity":
            instance.actual_instance = FeedbackSingularity.from_json(json_str)
            return instance

        # deserialize data into FeedbackOutOfWorkspace
        try:
            instance.actual_instance = FeedbackOutOfWorkspace.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FeedbackSingularity
        try:
            instance.actual_instance = FeedbackSingularity.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FeedbackJointLimitExceeded
        try:
            instance.actual_instance = FeedbackJointLimitExceeded.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FeedbackCollision
        try:
            instance.actual_instance = FeedbackCollision.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PlanTrajectoryFailedResponseErrorFeedback with oneOf schemas: FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PlanTrajectoryFailedResponseErrorFeedback with oneOf schemas: FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], FeedbackCollision, FeedbackJointLimitExceeded, FeedbackOutOfWorkspace, FeedbackSingularity]]:
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


