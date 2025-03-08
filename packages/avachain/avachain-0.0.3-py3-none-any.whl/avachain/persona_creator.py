import os
from typing import List, Dict, Any, Type, Union
from dataclasses import dataclass
from pathlib import Path
import inspect
import textwrap
import traceback
import json
import requests
from pydantic_core import PydanticUndefined
from print_color import print

from .avachain import BaseTool, BaseModel
from .avachain_executor import AvaAgent

# Constants
API_BASE_URL = "https://avaai.pathor.in/api/v1"
UPLOAD_ENDPOINT = f"{API_BASE_URL}/users/userStorage/storeicon/"
CREATE_PERSONA_ENDPOINT = f"{API_BASE_URL}/persona/createPersona"
UPDATE_PERSONA_ENDPOINT = f"{API_BASE_URL}/persona/updatePersona"
DELTET_PERSONA_ENDPOINT = f"{API_BASE_URL}/persona/deletePersona/dummyy/"
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

@dataclass
class TypeMapping:
    """Mapping of Python types to JSON schema types."""
    TYPES = {
        int: "number",
        float: "number",
        str: "string",
        bool: "boolean",
    }

    @classmethod
    def to_json_type(cls, type_info: Type) -> str:
        """Convert Python type to JSON schema type."""
        return cls.TYPES.get(type_info, str(type_info))
    
def validate_logo_path(logo_path: Union[str, Path]) -> Path:
    if not logo_path:
        raise ValueError("Logo path cannot be empty")
    
    path = Path(logo_path)
    
    if not path.exists():
        raise ValueError(f"Logo file does not exist: {path}")
    
    if not path.is_file():
        raise ValueError(f"Logo path is not a file: {path}")
        
    if path.suffix.lower() not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValueError(
            f"Logo file must be one of: {', '.join(ALLOWED_IMAGE_EXTENSIONS)}. "
            f"Got: {path.suffix}"
        )
        
    if not os.access(path, os.R_OK):
        raise ValueError(f"Logo file is not readable: {path}")
        
    return path

def upload_file(file_path: Union[str, Path], token: str) -> str:
    """
    Upload a file to the server and return its URL.
    
    Args:
        file_path: Path to the file to upload
        token: Authentication token
        
    Returns:
        str: URL of the uploaded file
        
    Raises:
        Exception: If file upload fails
    """
    try:
        path = validate_logo_path(file_path)
        with open(path, "rb") as file:
            response = requests.post(
                UPLOAD_ENDPOINT,
                files={"file": file},
                headers={"Authorization": f"Bearer {token}"}
            )
            response.raise_for_status()
            return response.json()["location"]
    except Exception as e:
        print(f"Error uploading file: {e}")
        traceback.print_exc()
        raise

def convert_tool_to_json(tool: BaseTool, tool_id: str) -> Dict[str, Any]:
    """
    Convert a tool object into a JSON representation.
    
    Args:
        tool: The tool object to convert
        tool_id: Identifier for the tool
        
    Returns:
        Dict containing the JSON representation of the tool
    """
    run_method_source = textwrap.dedent(inspect.getsource(tool._run))
    
    tool_json = {
        "title": tool_id,
        "ai_description": tool.description,
        "func_run": run_method_source,
        "func_schema": {},
        "parameters": {
            "tool_extras": {
                "isDirect": tool.return_direct,
                "name": tool.name,
            },
            "tool_parameters": {},
        },
    }

    if not tool.args_schema:
        return tool_json

    # Process tool parameters
    for field_name, field_info in tool.args_schema.__annotations__.items():
        field = tool.args_schema.model_fields[field_name]
        
        field_properties = {
            "type": TypeMapping.to_json_type(field_info),
            "description": getattr(field, "description", "No description available"),
            "default": "" if field.default is PydanticUndefined else field.default,
            "enum": []
        }

        # Handle enums
        if field.json_schema_extra:
            enum_values = field.json_schema_extra.get("enumerate")
            if enum_values:
                field_properties["enum"] = enum_values

        tool_json["parameters"]["tool_parameters"][field_name] = field_properties

    return tool_json

def prepare_tools_config(agent: AvaAgent) -> Dict[str, Any]:
    """
    Prepare tools configuration for an agent.
    
    Args:
        agent: The AvaAgent object
        
    Returns:
        Dict containing the tools configuration
    """
    try:
        config = {
            "base_sys_prompt": agent.sys_prompt_original,
            "tools": [
                convert_tool_to_json(tool, tool.name.lower())
                for tool in agent.tools_list
            ]
        }
        return config
    except Exception as e:
        print(f"Error preparing tools config: {e}")
        traceback.print_exc()
        return {}

def push_to_store(
    token: str,
    name: str,
    age: str,
    gender: str,
    public_description: str,
    logo_path: str,
    title: str = "",
    agent_obj: AvaAgent = None,
    can_be_used_as_tool: bool = False,
    behaviour: List[str] = None,
    tags: List[str] = None,
    languages: List[str] = None,
    hobbies: List[str] = None,
    supported_os: List[str] = None,
    is_public: bool = True,
    action: str = "create",
    custom_personaId: str = None,
    is_AssistantProfile: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """
    Push a persona to the AvA store as either an Agent or Assistant Profile.
    
    Args:
        token: Authentication token
        name: Persona name
        age: Persona age
        gender: Persona gender
        public_description: Public description
        logo_path: Path to logo file
        title: Optional title
        agent_obj: Optional AvaAgent object
        can_be_used_as_tool: Whether persona can be used as tool
        behaviour: List of behaviors
        tags: List of tags
        languages: List of supported languages
        hobbies: List of hobbies
        supported_os: List of supported operating systems
        is_public: Whether persona is public
        action: Action to perform (create/update/delete)
        custom_persona_id: Optional custom ID
        is_assistant_profile: Whether this is an assistant profile, When True, agent will become profile with no tools
        
    Returns:
        Dict containing the server response
        
    Raises:
        ValueError: If validation fails
    """
    # Handle delete action
    if action == "delete":
        if not custom_personaId:
            raise ValueError("custom_personaId is required for delete operations")
            
        headers = {"Authorization": f"Bearer {token}"}
        url = DELTET_PERSONA_ENDPOINT + custom_personaId
        try:
            response = requests.delete(url=url, headers=headers)
            
            if not response.ok:
                error_detail = response.json() if response.content else "No error details available"
                print(f"Server returned error: {error_detail}")
                
            response.raise_for_status()
            print(f"Successfully deleted persona with ID: {custom_personaId}")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"\nError deleting persona: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status code: {e.response.status_code}")
                try:
                    error_detail = e.response.json()
                    print(f"Error details: {json.dumps(error_detail, indent=2)}")
                except ValueError:
                    print(f"Raw response: {e.response.text}")
            traceback.print_exc()
            raise

    # Handle deprecated parameter
    if "is_MainAssistant" in kwargs:
        is_AssistantProfile = kwargs["is_MainAssistant"]
        print("Warning: 'is_MainAssistant' is deprecated. Use 'is_assistant_profile'")

    # Validate input
    if is_AssistantProfile and agent_obj and agent_obj.tools_list:
        raise ValueError("Assistant profiles cannot have tools")

    supported_os = supported_os or []
    if is_AssistantProfile:
        supported_os.append("nt")
    elif not supported_os:
        raise ValueError("Agents must support at least one OS ('nt' or 'android')")

    # Upload logo
    logo_url = upload_file(logo_path, token)

    # Prepare payload
    payload = {
        "name": name,
        "title": title,
        "age": age,
        "gender": gender,
        "languages": languages or [],
        "personality": public_description,
        "behavior": behaviour or [],
        "logo": logo_url,
        "voice": {
            "id": "random1",
            "pitch": 210,
            "amplitude": 0.25,
            "speed": 52,
            "pause": 0.8,
        },
        "os": supported_os,
        "hobbies": hobbies or [],
        "price": "nill",
        "tags": tags or [],
        "base_sys_prompt": "nil",
        "Is_main_agent": is_AssistantProfile,
        "is_agentic_tool": can_be_used_as_tool,
        "tools_config": prepare_tools_config(agent_obj) if agent_obj else {},
        "isPublic": is_public,
    }

    # Handle persona ID for different actions
    print('custom_persona_id', custom_personaId)
    if action == "update":
        if not custom_personaId:
            raise ValueError("personaId is required for update operations")
        payload["personaId"] = custom_personaId
    else:
        if custom_personaId:
            payload["customPersonaId"] = custom_personaId

    # Make request
    url = UPDATE_PERSONA_ENDPOINT if action == "update" else CREATE_PERSONA_ENDPOINT
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        
        response = requests.request(
            "PUT" if action == "update" else "POST",
            url=url,
            json=payload,
            headers=headers
        )
        
        if not response.ok:
            error_detail = response.json() if response.content else "No error details available"
            print(f"Server returned error: {error_detail}")
            
        response.raise_for_status()
        print(f"Status: {response.json()['message']}")
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"\nError pushing to store: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            try:
                error_detail = e.response.json()
                print(f"Error details: {json.dumps(error_detail, indent=2)}")
            except ValueError:
                print(f"Raw response: {e.response.text}")
        traceback.print_exc()
        raise