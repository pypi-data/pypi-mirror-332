import os, json

from .avachain import BaseTool
from typing import List, Optional, Type
from pydantic import BaseModel, Field  # , Type
from typing import Any, Dict, get_type_hints
from pydantic_core import PydanticUndefined
from print_color import print
import requests

# Either import your tools or create right here all upto you
# from ai_tools import CalendarTool, MusicPlayerTool
import inspect
import textwrap

"""This script provides two easy method to quicly create, update and delete a plugin
Its very convient than usual ui, and just have to pass the tool object and then feed the basic
required datas and then finally call the makeRequest with desired action! Boom!
"""


class MusicPlayerInput(BaseModel):
    query: str = Field(
        description="Should be the complete song query in details to be played"
    )
    songType: str = Field(
        description="what type of song, audio or video",
        enumerate=["audio", "video"],
        default="audio",
    )


def map_type_to_json(type_info):
    type_mappings = {
        int: "number",
        float: "number",
        str: "string",
        bool: "boolean",
        # Add more type mappings as needed i guess
    }
    return type_mappings.get(type_info, str(type_info))


def convert_tool_to_json(
    tool: BaseTool,
    tool_id: str,
    human_description: str,
    public_name: str,
    logo: str = None,
    isAnonymous: bool = False,
    authentication_required: Optional[bool] = False,
    connection_url: Optional[str] = "",
    isAuthenticated: bool = False,
    isPublic: bool = True,
    isMain: bool = False,
    tags: list = [],
    supports_android: bool = False,
    supports_windows: bool = True,
) -> Dict[str, Any]:
    """
    Convert a tool object into a JSON representation.

    Args:
        tool (BaseTool): The tool object.

    Returns:
        Dict[str, Any]: JSON representation of the tool.
    """
    json_representation = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    }
    run_method_source = inspect.getsource(tool._run)
    run_method_source = textwrap.dedent(run_method_source)
    print(run_method_source)

    if not supports_android and not supports_windows:
        raise ValueError(
            "You must specify at least one of 'android', 'windows' as the os"
        )
    os_support = []
    if supports_windows:
        os_support.append(os.name)
    if supports_android:
        os_support = ["android"]

    json_representation_2 = {
        "title": tool_id,
        "os": os_support,
        "human_description": human_description,
        "name": public_name,
        "ai_description": tool.description,
        "logo": logo,
        "isAnonymous": isAnonymous,
        "authentication_required": authentication_required,
        "connection_url": connection_url,
        "isAuthenticated": isAuthenticated,
        "isPublic": isPublic,
        "tags": tags,
        "func_run": run_method_source,
        "func_schema": {},
        "parameters": {
            "tool_extras": {
                "isMain": isMain,
                "isDirect": tool.return_direct,
                "name": tool.name,
            },
            "tool_parameters": {},
        },
    }
    # Add parameters from args_schema to the JSON representation
    required_args = []

    if tool.args_schema:
        for field_name, field_info in tool.args_schema.__annotations__.items():
            field_description = getattr(
                tool.args_schema.model_fields[field_name],
                "description",
                "No description available",
            )

            field_properties = {
                "type": map_type_to_json(field_info),
                "description": field_description,
            }
            if tool.args_schema.model_fields[field_name].repr:
                required_args.append(str(field_name))
            # Include default value if available
            # print("checking :", tool.args_schema.model_fields[field_name])
            # Include default value if available
            default_value = tool.args_schema.model_fields[field_name].default
            field_properties["default"] = ""
            if default_value is not None and default_value is not PydanticUndefined:
                field_properties["default"] = default_value

            # Include enum values if available
            enums_present = tool.args_schema.model_fields[field_name].json_schema_extra

            # enum_values = getattr(tool.args_schema.model_fields[field_name].json_schema_extra, 'enumerate', None)

            # this done to include the blank enum since backend needs it
            field_properties["enum"] = []
            if enums_present:
                enum_values = enums_present.get("enumerate", None)
                # print("Enum values: ", enum_values)
                if enum_values is not None:
                    field_properties["enum"] = enum_values

            json_representation_2["parameters"]["tool_parameters"][field_name] = (
                field_properties
            )
            # json_representation_2["function"]["parameters"]["required"] = required_args

    # print("converted a tool: ", required_args)
    print(json.dumps(json_representation_2, indent=2))
    return json_representation_2


def makePluginServerRequest(action: str, payload_data: dict, token: str):
    url = "https://avaai.pathor.in/api/v1/plugin/createGlobalPlugin"
    method = "POST"
    if action == "update":
        url = "https://avaai.pathor.in/api/v1/plugin/updateGlobalPlugin"
        method = "PUT"
    if action == "delete":
        url = "https://avaai.pathor.in/api/v1/plugin/deleteGlobalPlugin"
        method = "DELETE"
        payload_data = {"title": payload_data.get("title")}

    payload = json.dumps(payload_data)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    response = requests.request(method, url, headers=headers, data=payload)

    print(response.url, " : ", response.json())
    return response


# Exam of how to use tool creator
# if __name__ == "__main__":
# First create the tool data with addable data
#     tool_data = convert_tool_to_json(
#         CalendarTool(),#pass here the tool in similar way ex: MusicPlayerTool
#         tool_id="calendar",
#         human_description="""Stay organized and on track with this plugin, which retrieves and manages your Google Calendar events, meetings, and schedules, and sends notifications, reminders, and alerts to keep you informed.""",
#         logo="https://userdocbucket.s3.ap-south-1.amazonaws.com/Private/image/google-calendar_5968499.png",
#         public_name="G-Calendar",
#         tags=["productivity"],
#         isMain=True,
#     )

# Then make request to the server
#     makePluginServerRequest(
#         action="update",
#         payload_data=tool_data,
#         token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NTk5YTAyZTk3MWJlMGM5ZTg0YTI3YWUiLCJvcyI6ImJyb3dzZXIiLCJkZXZpY2VOYW1lIjoibW90byBnODIiLCJpYXQiOjE3MTU4OTc5NTQsImV4cCI6MTcxNzEwNzU1NH0.RzMe5qnCDQCKHi-ASX2Ey69jrtop-NJ5O5KUM9ag5n3VMXWimRyznH9AtSI_ImvF837tCuWB5Wn3wKtistveMg",
#     )

