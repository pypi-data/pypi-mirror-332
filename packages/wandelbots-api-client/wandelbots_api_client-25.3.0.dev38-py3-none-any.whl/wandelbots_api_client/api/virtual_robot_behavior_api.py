# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from furl import furl
import json
import humps
import re
import warnings
import websockets
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, AsyncGenerator, Callable, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from urllib.parse import quote

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from wandelbots_api_client.models.behavior import Behavior
from wandelbots_api_client.models.external_joint_stream_datapoint import ExternalJointStreamDatapoint
from wandelbots_api_client.models.motion_group_behavior_getter import MotionGroupBehaviorGetter
from wandelbots_api_client.models.motion_group_joints import MotionGroupJoints

from wandelbots_api_client.api_client import ApiClient, RequestSerialized
from wandelbots_api_client.api_response import ApiResponse
from wandelbots_api_client.rest import RESTResponseType

class VirtualRobotBehaviorApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def external_joints_stream(self, cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")], controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")], client_request_generator: Callable[[AsyncGenerator[MotionGroupJoints, None]], AsyncGenerator[ExternalJointStreamDatapoint, None]]) -> None:  # noqa: E501
        """Stream Joint Configuration  # noqa: E501

        This stream provides the commanded joint state and sets a motion groups joint configuration, e.g. to move a motion group. The concept is that an application is using the Motion Service to move a motion group. The Motion Service is commanding the desired joint configuration of a motion group.  Physical motion groups move to this joint configuration.  With physical motion groups, this takes some time and only works if possible.  And you have the *actual* joint state - the current real motion group configuration.  Again, this stream is providing *commanded* joint state! It is __not__ providing the *actual* joint state! (Please file a request - if you need a stream of the *actual* joint state)  When the virtual controller receives joint commands the joint configuration is immediately adapted to match the incoming joint configurations. CAUTION: Incoming joint configurations are not visualized and their velocity limits are not checked. we don't even check limits!  Possible use cases are: 1. Creating a robotic application that dynamically adapts to the configured joints on the robot controller, using this stream to feed new joint configurations back to the motion group.  The stream only sends data to the robot controller if a motion is executed.  If the robot controller's joint configuration differs too much from the incoming joint configuration, a following error occurs. Joint configurations that result in following errors are executed only for motions with a low velocity.  2. Mimic Freedrive motions.  <!-- theme: danger -->  > **DANGER** > > If the incoming joint configuration is set to maximum velocity, the movement to reach this incoming joint configuration will be executed with maximum speed regardless > of safety zones and mechanical limits.   # noqa: E501
        :param client_request_generator: An AsyncGenerator that yields request of type ExternalJointsStreamRequest and takes an AsyncGenerator of MotionGroupJoints as an input argument (required)
        :info All responses from the server will be yielded to client_request_generator through the (AsyncGenerator[MotionGroupJoints, None])
        :type AsyncGenerator[ExternalJointsStreamRequest, None]
        """
        def format_path_parameters(path):
            # Find all substrings that are enclosed in brackets
            bracket_contents = re.findall(r'\{(.*?)\}', path)

            # For each found substring, alter it to match the python variable name
            for content in bracket_contents:
                content = "{" + content + "}"
                modified_content = humps.dekebabize(content)
                path = path.replace(content, modified_content)

            return path

        async def iterate_responses(ws) -> AsyncGenerator[MotionGroupJoints, None]:
            async for response in ws:
                if "Cancelled on the server side" in response:
                    break
                response_data = json.loads(response)
                if "result" not in response_data:
                    raise Exception(response_data)
                yield MotionGroupJoints.from_dict(response_data["result"])

        path = format_path_parameters("/cells/{cell}/controllers/{controller}/teach-pendant/motion-groups/externalJointsStream")
        path = path.format(cell=cell,controller=controller,)

        headers = websockets.Headers()
        tmp_host = self.api_client.configuration.host
        if self.api_client.configuration.host.startswith("https://"):
            # Basic Auth
            if self.api_client.configuration.username:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{self.api_client.configuration.username}:{self.api_client.configuration.password}@{tmp_host}"

            # OAuth2
            elif self.api_client.configuration.access_token:
                tmp_host = self.api_client.configuration.host.replace("https://", "")
                tmp_host = f"wss://{tmp_host}"
                headers = websockets.Headers([
                    ("Authorization", f"Bearer {self.api_client.configuration.access_token}")
                ])
        else:
            tmp_host = tmp_host.replace("http://", "ws://")

        full_url = furl(tmp_host + path)

        async with websockets.connect(full_url.url, open_timeout=10, additional_headers=headers) as websocket:
            async for request in client_request_generator(iterate_responses(websocket)):
                await websocket.send(request.to_json())


    @validate_call
    async def get_motion_group_behavior(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MotionGroupBehaviorGetter:
        """Behavior

        Get the current robot motion group behavior - please see the setter [setMotionGroupBehavior](setMotionGroupBehavior) and the enum for details.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MotionGroupBehaviorGetter",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_motion_group_behavior_with_http_info(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MotionGroupBehaviorGetter]:
        """Behavior

        Get the current robot motion group behavior - please see the setter [setMotionGroupBehavior](setMotionGroupBehavior) and the enum for details.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MotionGroupBehaviorGetter",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_motion_group_behavior_without_preload_content(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Behavior

        Get the current robot motion group behavior - please see the setter [setMotionGroupBehavior](setMotionGroupBehavior) and the enum for details.

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MotionGroupBehaviorGetter",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_motion_group_behavior_serialize(
        self,
        cell,
        controller,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cell is not None:
            _path_params['cell'] = cell
        if controller is not None:
            _path_params['controller'] = controller
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'BasicAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/cells/{cell}/controllers/{controller}/teach-pendant/motion-groups/{id}/behavior',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



    @validate_call
    async def set_motion_group_behavior(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        behavior: Optional[Behavior] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Switch Behavior

        Switch robot motion group behavior. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param behavior:
        :type behavior: Behavior
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._set_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            behavior=behavior,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def set_motion_group_behavior_with_http_info(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        behavior: Optional[Behavior] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Switch Behavior

        Switch robot motion group behavior. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param behavior:
        :type behavior: Behavior
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._set_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            behavior=behavior,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def set_motion_group_behavior_without_preload_content(
        self,
        cell: Annotated[StrictStr, Field(description="Unique identifier addressing a cell in all API calls. ")],
        controller: Annotated[StrictStr, Field(description="Unique identifier to address a controller in the cell.")],
        id: Annotated[StrictInt, Field(description="The controller specific motion-group id.")],
        behavior: Optional[Behavior] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Switch Behavior

        Switch robot motion group behavior. 

        :param cell: Unique identifier addressing a cell in all API calls.  (required)
        :type cell: str
        :param controller: Unique identifier to address a controller in the cell. (required)
        :type controller: str
        :param id: The controller specific motion-group id. (required)
        :type id: int
        :param behavior:
        :type behavior: Behavior
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._set_motion_group_behavior_serialize(
            cell=cell,
            controller=controller,
            id=id,
            behavior=behavior,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _set_motion_group_behavior_serialize(
        self,
        cell,
        controller,
        id,
        behavior,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cell is not None:
            _path_params['cell'] = cell
        if controller is not None:
            _path_params['controller'] = controller
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if behavior is not None:
            
            _query_params.append(('behavior', behavior.value))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'BasicAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/cells/{cell}/controllers/{controller}/teach-pendant/motion-groups/{id}/behavior',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


