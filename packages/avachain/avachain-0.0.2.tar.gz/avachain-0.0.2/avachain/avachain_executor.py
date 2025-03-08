import importlib
import inspect
import subprocess
import typing
from pydantic_core import PydanticUndefined
import requests
from datetime import datetime
import json
from typing import Dict, List, Optional, Callable

from avachain import (
    BaseTool,
    ClaudeLLM,
    OpenaiLLM,
    MistralAILLM,
    LLM,
    convert_tools_to_json,
    extract_function_info,
    find_and_execute_tool,
    CallbackHandler,
)
import time

# import openai
from print_color import print
from traceback import print_exc
from openai.types.chat import ChatCompletion
from mistralai.models.chat_completion import ChatMessage as MistralChatMessage


import requests

from avachain import map_type_to_json


import os


# def get_current_timestamp():
#     # Get the current timestamp
#     current_timestamp = datetime.now()

#     # Convert the timestamp to a string
#     timestamp_string = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

#     return timestamp_string


def get_current_timestamp():
    # Get the current timestamp with day of week
    current_timestamp = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")

    return current_timestamp


def getRimeTTS(text):
    url = "https://users.rime.ai/v1/rime-tts"

    payload = {
        "speaker": "eva",
        "text": text,
        "modelId": "mist",
        "samplingRate": 22050,
        "speedAlpha": 1.0,
        "reduceLatency": False,
    }
    headers = {
        "Accept": "audio/mp3",
        "Authorization": "Bearer M1jSmw004ffRB352M20OE1jGzncs0ualtgiIwXs_5nY",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.content)


class AvaAgent:
    def __init__(
        self,
        sys_prompt: str,
        ava_llm: LLM,
        tool_choice: str = None,
        tools_list: Optional[List[BaseTool]] = [],
        pickup_mes_count: int = 4,
        logging: bool = False,
        use_system_prompt_as_context: bool = False,
        is_function_based: bool = False,
        max_agent_iterations: int = 4,
        throw_error_on_iteration_exceed: bool = False,
        callback_handler: CallbackHandler = None,
        agent_name_identifier: str = "agent",
        deeper_logs: bool = False,
        include_message_timestap: bool = True,
        streaming: bool = False,
        pikcup_mes_count_in_sys_history: int = 3,
        tts_streaming: bool = False,
        is_non_gpt_model: bool = False,
        print_tts_streaming: bool = True,
    ):
        self.include_message_timestap = include_message_timestap
        self.use_system_prompt_as_context = use_system_prompt_as_context
        self.is_function_based = is_function_based
        self.sys_prompt_original = sys_prompt
        self.sys_prompt: str = sys_prompt
        self.messages: List = []
        self.tools_list: List = tools_list
        self.ava_llm: LLM = ava_llm
        self.pickup_mes_count: int = pickup_mes_count
        self.pikcup_mes_count_in_sys_history = pikcup_mes_count_in_sys_history
        self.isOpenaiLLM = isinstance(self.ava_llm, OpenaiLLM)
        self.is_non_gpt_model = is_non_gpt_model
        if use_system_prompt_as_context:
            # since we dont want the agent to be totally dumb
            self.pickup_mes_count = pikcup_mes_count_in_sys_history
            self.system_prompt_contexts_history = """"""
            self.generate_system_prompt_with_context(
                self.system_prompt_contexts_history
            )
        self.agent_name_identifier = agent_name_identifier
        self.current_user_msg: str = None

        self.appendToMessages(role="system", content=sys_prompt)

        self.converted_tools_list: List[Dict] = convert_tools_to_json(
            tools=tools_list, is_function_based=self.is_function_based
        )
        self.logging: bool = logging
        self.deeper_logs = deeper_logs
        self.callback_handler: CallbackHandler = callback_handler
        self.throw_error_on_iteration_exceed: bool = throw_error_on_iteration_exceed
        self.max_agent_iterations: int = max_agent_iterations
        self.current_agent_iteration: int = 0
        self.streaming: bool = streaming
        self.tts_streaming = tts_streaming
        self.tool_choice = tool_choice
        self.print_tts_streaming = print_tts_streaming
        print(f"{agent_name_identifier} TOOlS:")
        if self.deeper_logs:
            for json_representation in self.converted_tools_list:
                print(json.dumps(json_representation, indent=2))

    def run(
        self,
        msg: str = None,
        actual_mes: Optional[str] = None,
        image_input: Optional[str] = None,
    ):
        """Runs the agent via main executor"""
        if not msg:
            raise ValueError("Input to agent cannot be blank")

        try:
            print(
                f"\nRunning {self.agent_name_identifier} ... with input: '{msg}'\n",
                color="purple",
            )

            content = actual_mes if actual_mes else msg
            self.appendToMessages(role="user", content=content, image_input=image_input)

            if self.use_system_prompt_as_context:
                timestamp = (
                    f"(SystemNote:{get_current_timestamp()}): "
                    if self.include_message_timestap
                    else ": "
                )
                self.system_prompt_contexts_history += f"\nUSER{timestamp}{msg}"

            self.current_user_msg = msg
            self.messages = self.trim_list(
                input_list=self.messages, count=self.pickup_mes_count
            )

            return self.ava_main_executor(
                messages=self.messages,
                tools_list=self.tools_list,
                ava_llm=self.ava_llm,
            )

        except ValueError as e:
            if self.logging:
                print_exc()
            raise ValueError(f"Error in agent run : ", e)

    def generate_system_prompt_with_context(self, context_string=None):
        if context_string:
            self.sys_prompt = f"""{self.sys_prompt_original}\n
            Please take into account the preceding and ongoing dialogues between you and the user for context, and utilize this information to inform your subsequent responses."
            Below are the prior and current converstations between you and the user (with message SystemNote). Use it as context and information in further conversations with the User:
            {context_string}
            """
        else:
            self.sys_prompt = self.sys_prompt_original
        # result = f"This is the string with input: {context_string}" if context_string else "..."
        # return result

    def appendToMessages(
        self,
        role: str,
        content: str,
        image_input: Optional[str] = None,
        tool_call_id: Optional[str] = None,
        tool_name: Optional[str] = None,
    ):
        # if role == "system":
        #     role = "developer"

        print(
            self.agent_name_identifier.capitalize(),
            ": ",
            "appending message: Currently LLM is openai? ",
            self.isOpenaiLLM,
        )
        if role == "user" and self.include_message_timestap:
            content = f"(SystemNote:{get_current_timestamp()}) " + content

        if self.isOpenaiLLM:
            self.validate_and_append_to_list(
                role=role,
                content=content,
                image_input=image_input,
                tool_name=tool_name,
                tool_call_id=tool_call_id,
            )
            # if image_input:
            #     # Format for GPT-4 Vision with image
            #     self.messages.append(
            #         {
            #             "role": role,
            #             "content": [
            #                 {"type": "text", "text": content},
            #                 {
            #                     "type": "image_url",
            #                     "image_url": {"url": f"{image_input}"},
            #                 },
            #             ],
            #         }
            #     )
            # else:
            #     # Regular text-only message

            #     self.messages.append(
            #         {"role": role, "content": [{"type": "text", "text": content}]}
            #     )

        elif isinstance(self.ava_llm, MistralAILLM):
            # if not role == "system":
            self.messages.append(MistralChatMessage(role=role, content=content))
        elif isinstance(self.ava_llm, ClaudeLLM):
            if not role == "system":
                self.messages.append({"role": role, "content": content})

    def validate_and_append_to_list(
        self,
        role,
        content,
        image_input: Optional[str] = None,
        tool_call_id: Optional[str] = None,
        tool_name: Optional[str] = None,
        function_arguments: Optional[str] = None,
    ):
        """
        Validates and appends a new dictionary to the provided list, ensuring JSON compliance.

        Args:
            role (str): The role to add (e.g., "user", "developer", "system").
            content (str): The content to add.
            data_list (list): The existing list of dictionaries to which the new entry will be appended.

        Returns:
            list: The updated list with the new entry, validated and JSON-compliant.

        Raises:
            ValueError: If validation fails for the new entry or the updated list.
        """
        try:
            # if self.logging:
            # print(
            #     f"Validating inputs: role: {role}, content: {content}, image_inputs: {image_input}, tool_call_id:{tool_call_id}, tool_name: {tool_name}"
            # )
            # Validate role
            if not isinstance(role, str):
                raise ValueError("Role must be a string.")
            if role.strip() == "":
                raise ValueError("Role cannot be an empty string.")

            # Ensure content is a string
            if not isinstance(content, str):
                content = str(content)

            # Retain only printable ASCII characters (32 to 126) and strip whitespace
            content = "".join(
                char for char in content if 32 <= ord(char) <= 126
            ).strip()

            # Escape special characters in content to ensure JSON compliance
            safe_content = json.dumps(content)[
                1:-1
            ]  # Escape and remove surrounding quotes

            # return safe_content

            if image_input:
                new_entry = {
                    "role": role,
                    "content": [
                        {"type": "text", "text": safe_content},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"{image_input}"},
                        },
                    ],
                }
            else:
                # Create the new dictionary
                if tool_call_id:
                    new_entry = {
                        "role": role,
                        "tool_call_id": tool_call_id,
                        "tool_name": tool_name,
                        "content": safe_content,
                    }
                elif tool_call_id and role == "assistant":
                    {
                        "role": "assistant",
                        "tool_calls": [
                            {
                                "id": tool_call_id,
                                "function": {
                                    "arguments": function_arguments,
                                    "name": tool_name,
                                },
                            }
                        ],
                    }
                else:
                    new_entry = {"role": role, "content": safe_content}

            # Append to the list
            self.messages.append(new_entry)

            # Validate the entire list by attempting to serialize it into a JSON string
            # try:
            json.dumps(self.messages)  # Raises an error if invalid
            # except TypeError as e:
            #     if (
            #         "Object of type ChatCompletionMessage is not JSON serializable"
            #         in str(e)
            #     ):
            #         pass  # Ignore this specific error
            #     else:
            #         raise e

            return self.messages

        except Exception as e:
            raise ValueError(f"Failed to validate and append entry: {e}")

    def validate_entry(self, role, content):
        """
        Validates a single dictionary entry for JSON compliance.

        Args:
            role (str): The role to validate (e.g., "user", "developer").
            content (str): The content to validate.

        Returns:
            dict: A validated and JSON-compliant dictionary entry.

        Raises:
            ValueError: If validation fails for the entry.
        """
        try:
            # Validate role
            if not isinstance(role, str):
                raise ValueError("Role must be a string.")
            if role.strip() == "":
                raise ValueError("Role cannot be an empty string.")

            # Ensure content is a string
            if not isinstance(content, str):
                content = str(content)

            # Escape special characters in content to ensure JSON compliance
            safe_content = json.dumps(content)[
                1:-1
            ]  # Escape and remove surrounding quotes

            # Create and return the validated dictionary
            return {"role": role, "content": safe_content}

        except Exception as e:
            raise ValueError(f"Failed to validate entry: {e}")

    def generateSysMessageForLLM(self, content: str):
        # if not to_add_system_context_history:
        print(
            self.agent_name_identifier.capitalize(),
            ": ",
            "Currently LLM is openai? ",
            self.isOpenaiLLM,
        )
        if self.isOpenaiLLM:
            return self.validate_entry(role="system", content=content)
        elif isinstance(self.ava_llm, MistralAILLM):
            # if not role == "system":
            return MistralChatMessage(role="system", content=content)
        # elif isinstance(self.ava_llm, ClaudeLLM):
        #     if not role == "system":
        #         self.messages.append({"role": "system", "content": content})

    def refreshSysMessage(self, content: str = None):
        # if isinstance(self.ava_llm, MistralAILLM):
        # if not content:
        # MistralChatMessage(role="system", content=self.sys_prompt)
        self.messages[0] = self.generateSysMessageForLLM(content=self.sys_prompt)
        # else:
        #     # MistralChatMessage(role="system", content=self.sys_prompt)
        #     self.messages[0] = self.generateSysMessageForLLM(content=content)

    def updateSysMessage(self, content: str = None):
        # if isinstance(self.ava_llm, MistralAILLM):
        if not content:
            # MistralChatMessage(role="system", content=self.sys_prompt)
            self.messages[0] = self.generateSysMessageForLLM(content=self.sys_prompt)
        else:
            self.sys_prompt = content
            self.sys_prompt_original = content
            # MistralChatMessage(role="system", content=self.sys_prompt)
            self.messages[0] = self.generateSysMessageForLLM(content=content)

        # # elif self.isOpenaiLLM:
        #     self.messages[0] = self.generateSysMessageForLLM(content=self.sys_prompt)

    def getSystemMessage(
        self,
    ):
        return self.sys_prompt

    def clearMessageHistory(self, del_systen_chat_history: bool = False):
        if self.logging:
            print(
                self.agent_name_identifier.capitalize(),
                ": ",
                f"Deleting chat history..🗑️ for {self.agent_name_identifier}",
            )
        self.messages.clear()
        if self.use_system_prompt_as_context and del_systen_chat_history:
            self.system_prompt_contexts_history = ""
            self.generate_system_prompt_with_context(context_string=None)
        self.appendToMessages(role="system", content=self.sys_prompt)
        if self.logging and self.deeper_logs:
            print(
                self.agent_name_identifier.capitalize(),
                ": ",
                "Agent chat history cleared 🧹: ",
                self.messages,
                "\n",
                color="magenta",
            )

    def trim_list1(self, input_list: list, count: int):
        """
        Trim the list to the last 'count' items if the length is greater than 'count'.

        Parameters:
        - input_list (list): The input list to be trimmed.
        - count (int): The desired count of items in the final list.

        Returns:
        - list: Trimmed list.
        """
        print(self.agent_name_identifier.capitalize(), ": ", "trimmnig list")

        if len(input_list) < count:
            return input_list

        # a simple check if the last item of the messsage array has the tool_calls content or None
        print(
            self.agent_name_identifier.capitalize(),
            ": ",
            f"last message item: {input_list[-1]}",
            color="yellow",
        )
        if input_list[-1].get("tool_calls", None):
            print(
                "skkipping trimmnig list since last message has tool_calls...",
                color="red",
            )

            return input_list

        else:
            if not self.use_system_prompt_as_context:
                input_list = input_list[-count:]
                # input_list[0] = self.generateSysMessageForLLM(content=self.sys_prompt)
                input_list.insert(
                    0, self.generateSysMessageForLLM(content=self.sys_prompt)
                )
            else:
                input_list = input_list[-count:]
                # input_list[0] = self.generateSysMessageForLLM(content=self.sys_prompt)
                input_list.insert(
                    0, self.generateSysMessageForLLM(content=self.sys_prompt)
                )
            return input_list

    def is_candidate_valid(self, candidate: list) -> bool:
        """
        Check that every message with role 'tool' is preceded by at least one message
        that contains a tool call.
        """
        for idx, msg in enumerate(candidate):
            if msg.get("role") == "tool":
                # If this tool response is at the beginning, or there’s no earlier message with a tool call, it’s orphaned.
                if idx == 0 or not any(m.get("tool_calls") for m in candidate[:idx]):
                    return False
        return True

    def trim_list(self, input_list: list, count: int):
        """
        Trim the conversation history to (at least) the last 'count' messages,
        ensuring that if any message includes a tool call (via "tool_calls")
        or is a tool response (role == "tool"), its counterpart is included.

        If extending is needed to maintain a valid pair sequence, the final message list
        might exceed the desired count.
        """
        print(
            f"{self.agent_name_identifier.capitalize()}: Trimming list", color="magenta"
        )

        # If the list is short enough, nothing to trim.
        if len(input_list) <= count:
            candidate = input_list[:]
        else:
            # Start with a candidate that is the last 'count' messages.
            candidate_start = len(input_list) - count
            candidate = input_list[candidate_start:]

            # If the candidate list is not valid (for example, it starts with a tool response
            # that’s orphaned or a tool response somewhere is missing its corresponding tool call),
            # then extend the candidate backwards.
            while candidate_start > 0 and not self.is_candidate_valid(candidate):
                candidate_start -= 1
                candidate = input_list[candidate_start:]

        # Optionally, you might want to log if the candidate was extended beyond your count.
        if len(candidate) > count:
            print(
                f"{self.agent_name_identifier.capitalize()}: Extended candidate length to preserve tool pairs (final count: {len(candidate)})"
            )

        # Always ensure the system prompt is at the beginning.
        candidate.insert(0, self.generateSysMessageForLLM(content=self.sys_prompt))
        return candidate

    def ava_main_executor(
        self, messages: List[dict], tools_list: List[BaseTool], ava_llm: LLM
    ):
        """
        tools_list: is actual list of tools with tools as class ex: [mytool(),mytool2()]

        converted_tools_list: is the converted list of to json with schema

        messages: the list of user-assistant messages pairs
        """
        tools_list_copy = tools_list.copy()
        if self.current_agent_iteration <= self.max_agent_iterations:
            self.current_agent_iteration += 1

            if self.logging:
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "Messages List: ",
                    self.messages,
                    "\n",
                    color="purple",
                )

            if self.callback_handler and hasattr(self.callback_handler, "on_agent_run"):
                self.callback_handler.on_agent_run(input_msg="agent started running!")

            if self.messages and self.ava_llm:
                # For OpenaiLLM and MistralAILLM
                if self.isOpenaiLLM or isinstance(self.ava_llm, MistralAILLM):
                    return self.handle_openai_llm_completions(
                        messages=messages, tools_list=tools_list_copy, ava_llm=ava_llm
                    )
                # For ClaudeLLM
                return self.handle_claude_llm_completions(
                    messages=messages, tools_list=tools_list_copy, ava_llm=ava_llm
                )

            self.current_agent_iteration = 0
            raise ValueError(
                f"Error: Check the passed message: {messages}, tools: {tools_list_copy}, and ava llm: {ava_llm}"
            )
        else:
            self.current_agent_iteration = 0
            if not self.throw_error_on_iteration_exceed:
                return (
                    "Sorry! I wasn't able to complete you query after several tries!!."
                )
            raise ValueError(
                f"{self.agent_name_identifier} wasnt' able to come to the conclusion and was exceeding the max agent iteration count of {self.max_agent_iterations}"
            )

    def handle_claude_llm_completions(
        self, messages: List[dict], tools_list: List[BaseTool], ava_llm: ClaudeLLM
    ):
        llm_resp = ava_llm.ava_llm_completions(
            self.messages,
            self.converted_tools_list,
            is_function_based=self.is_function_based,
            system=self.sys_prompt,
        )
        if self.logging:
            print(
                self.agent_name_identifier.capitalize(),
                ": ",
                "OPENAI LLM RESP:",
                llm_resp,
                "\n",
                color="green",
            )
        agent_response = llm_resp.content[0].text
        agent_mes = llm_resp.content[0].text
        self.appendToMessages(role="assistant", content=agent_mes)
        if self.use_system_prompt_as_context:
            if not self.include_message_timestap:
                self.system_prompt_contexts_history += f"\nYOU:{agent_mes}"
            else:
                self.system_prompt_contexts_history += (
                    f"\nYOU(SystemNote:{get_current_timestamp()}):{agent_mes}"
                )
            self.generate_system_prompt_with_context(
                context_string=self.system_prompt_contexts_history
            )
            self.updateSysMessage()
        if self.logging:
            print(
                f"{self.agent_name_identifier.capitalize()} message: ",
                agent_mes,
                color="yellow",
            )
            print()
        if self.callback_handler and hasattr(
            self.callback_handler, "on_general_response"
        ):
            self.callback_handler.on_general_response(response=agent_mes)
        self.current_agent_iteration = 0
        return agent_mes

    def handle_openai_llm_completions(
        self, messages: List[dict], tools_list: List[BaseTool], ava_llm: OpenaiLLM
    ):
        llm_resp = None
        if not self.streaming:
            t0 = time.time()
            llm_resp = ava_llm.ava_llm_completions(
                self.messages,
                self.converted_tools_list,
                is_function_based=self.is_function_based,
                streaming=self.streaming,
                tool_choice=self.tool_choice,
            )
            if self.logging:
                t1 = time.time() - t0
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "AI responded in : {:.2f} milliseconds".format(t1 * 1000),
                    color="blue",
                )
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "OPENAI LLM RESP:",
                    llm_resp,
                    "\n",
                    color="green",
                )
            return self.complete_normal_openai_llm_response(
                # agent_response=agent_response,
                llm_resp=llm_resp,
                messages=messages,
                tools_list=tools_list,
                ava_llm=ava_llm,
            )

        else:
            # HERE WE ARE HANDLING STREAMING RESPONSES
            t0 = time.time()
            llm_resp = ava_llm.ava_llm_completions(
                self.messages,
                self.converted_tools_list,
                is_function_based=self.is_function_based,
                streaming=self.streaming,
                tool_choice=self.tool_choice,
            )
            if self.logging:
                t1 = time.time() - t0
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "AI responded in : {:.2f} milliseconds".format(t1 * 1000),
                )
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "OPENAI STREAMING LLM RESP:",
                    llm_resp,
                    "\n",
                    color="green",
                )
            return self.complete_streaming_openai_llm_response(
                # agent_response=agent_response,
                llm_resp=llm_resp,
                messages=messages,
                tools_list=tools_list,
                ava_llm=ava_llm,
                start_time=t0,
            )

    def complete_normal_openai_llm_response(
        self,
        llm_resp,
        messages: List[dict],
        tools_list: List[BaseTool],
        ava_llm: OpenaiLLM,
    ):
        agent_response = llm_resp.choices[0].message
        if not self.is_function_based:
            if llm_resp.choices[0].message.tool_calls:
                """THIS MEANS AGENT MADE TOOL CALL"""

                if self.isOpenaiLLM:
                    messages.append(
                        # agent_response
                        # if not self.is_non_gpt_model
                        # else
                        {
                            "role": agent_response.role,
                            "content": "",
                            "tool_calls": [
                                tool_call.model_dump()
                                for tool_call in llm_resp.choices[0].message.tool_calls
                            ],
                        }
                    )
                if self.logging:
                    print(
                        self.agent_name_identifier.capitalize(),
                        ": ",
                        f"Total tools called: ",
                        len(llm_resp.choices[0].message.tool_calls),
                    )
                for tool_call in llm_resp.choices[0].message.tool_calls:
                    name, params, tool_id = extract_function_info(
                        tool_call=tool_call, is_function_based=self.is_function_based
                    )
                    # print(f"Name: {name}")
                    # print(f"Params: {params}")

                    if name:
                        if self.logging:
                            print(
                                self.agent_name_identifier.capitalize(),
                                ": ",
                                f"Executing tool '{name}' ... with param(s): ",
                                f"'{params}'",
                                "\n",
                                color="yellow",
                            )
                        if self.callback_handler and hasattr(
                            self.callback_handler, "on_tool_call"
                        ):
                            self.callback_handler.on_tool_call(
                                tool_name=name, tool_params=params
                            )

                        if len(json.loads(params)) == 0:
                            print(
                                self.agent_name_identifier.capitalize(),
                                ": ",
                                "Empty param received!",
                                color="yellow",
                            )
                        resp, is_direct = find_and_execute_tool(
                            tool_name=name,
                            tool_params=json.loads(params),
                            tools_list=tools_list,
                            is_empty_tool_params=True
                            if len(json.loads(params)) == 0
                            else False,
                        )
                        # if len(json.loads(params)) == 0:
                        #     resp = "pass"
                        if resp:
                            if self.logging:
                                print(
                                    self.agent_name_identifier.capitalize(),
                                    ": ",
                                    f"Tool '{name}' response: ",
                                    resp,
                                    "\n",
                                    color="blue",
                                )

                            # messages.append({"role": "function", "name": name, "content": resp})
                            if isinstance(self.ava_llm, MistralAILLM):
                                messages.append(
                                    MistralChatMessage(
                                        role="tool",
                                        name=name,
                                        content=f"""{repr(resp)}""",
                                    )
                                )
                            elif self.isOpenaiLLM:
                                self.appendToMessages(
                                    role="tool",
                                    tool_name=name,
                                    content=resp,
                                    tool_call_id=tool_id,
                                )
                                # if not self.is_non_gpt_model
                                # pass

                            if self.use_system_prompt_as_context:
                                self.system_prompt_contexts_history += (
                                    f"\nTOOL({name}): {resp}"
                                )
                            # if
                            # Passin updated values in the recursive call
                            if is_direct:
                                if self.logging:
                                    print(
                                        self.agent_name_identifier.capitalize(),
                                        ": ",
                                        "Returning tool response as direct message",
                                        "\n",
                                        color="magenta",
                                    )
                                    print(
                                        f"{self.agent_name_identifier.capitalize()} message: ",
                                        resp,
                                        color="yellow",
                                    )
                                    print()

                                self.appendToMessages(role="assistant", content=resp)
                                if self.use_system_prompt_as_context:
                                    if not self.include_message_timestap:
                                        self.system_prompt_contexts_history += (
                                            f"\nYOU:{resp}"
                                        )
                                    else:
                                        self.system_prompt_contexts_history += f"\nYOU(SystemNote:{get_current_timestamp()}):{resp}"
                                    self.generate_system_prompt_with_context(
                                        context_string=self.system_prompt_contexts_history
                                    )
                                    self.updateSysMessage()
                                return resp

                return self.ava_main_executor(
                    messages=messages, tools_list=tools_list, ava_llm=ava_llm
                )

            else:
                """THIS MEANS THE AGENT JUST REPLIED NORMALLY WITHOUT FUNCTION OR TOOL CALLING"""
                agent_mes = llm_resp.choices[0].message.content
                self.appendToMessages(role="assistant", content=agent_mes)
                if self.use_system_prompt_as_context:
                    if not self.include_message_timestap:
                        self.system_prompt_contexts_history += f"\nYOU:{agent_mes}"
                    else:
                        self.system_prompt_contexts_history += (
                            f"\nYOU(SystemNote:{get_current_timestamp()}):{agent_mes}"
                        )
                    self.generate_system_prompt_with_context(
                        context_string=self.system_prompt_contexts_history
                    )
                    self.updateSysMessage()
                if self.logging:
                    print(
                        f"{self.agent_name_identifier.capitalize()} message: ",
                        agent_mes,
                        color="yellow",
                    )
                    print()
                if self.callback_handler and hasattr(
                    self.callback_handler, "on_general_response"
                ):
                    self.callback_handler.on_general_response(response=agent_mes)
                self.current_agent_iteration = 0
                if self.tts_streaming:
                    pass
                    # play_carts_tts(text=agent_mes)
                return agent_mes

        else:
            if llm_resp.choices[0].message.function_call:
                """THIS MEANS AGENT MADE FUNCTION CALL"""
                for function_call in llm_resp.choices[0].message.function_call:
                    name, params, tool_id = extract_function_info(
                        tool_call=llm_resp.choices[0].message.function_call,
                        is_function_based=self.is_function_based,
                    )
                    # print(f"Name: {name}")
                    # print(f"Params: {params}")

                    if name:
                        if self.logging:
                            print(
                                self.agent_name_identifier.capitalize(),
                                ": ",
                                f"Executing function '{name}' ... with param(s): ",
                                f"'{params}'",
                                "\n",
                                color="yellow",
                            )
                        if self.callback_handler and hasattr(
                            self.callback_handler, "on_tool_call"
                        ):
                            self.callback_handler.on_tool_call(
                                tool_name=name, tool_params=params
                            )

                        resp, is_direct = find_and_execute_tool(
                            tool_name=name,
                            tool_params=json.loads(params),
                            tools_list=tools_list,
                        )

                        if resp:
                            if self.logging:
                                print(
                                    self.agent_name_identifier.capitalize(),
                                    ": ",
                                    f"Returned From Function '{name}' response: ",
                                    resp,
                                    "\n",
                                    color="blue",
                                )

                            # messages.append({"role": "function", "name": name, "content": resp})
                            messages.append(
                                {
                                    # "role": "tool",
                                    # "content": resp
                                    # "tool_call_id": tool_call.id,
                                    "role": "function",
                                    "name": name,
                                    "content": resp,
                                }
                            )
                            if self.use_system_prompt_as_context:
                                self.system_prompt_contexts_history += (
                                    f"\nFUNCTION({name}): {resp}"
                                )
                            # if
                            # Passin updated values in the recursive call
                            if is_direct:
                                print(
                                    self.agent_name_identifier.capitalize(),
                                    ": ",
                                    "Returning tool response as direct message",
                                    "\n",
                                    color="magenta",
                                )
                                self.appendToMessages(role="assistant", content=resp)
                                if self.use_system_prompt_as_context:
                                    if not self.include_message_timestap:
                                        self.system_prompt_contexts_history += (
                                            f"\nYOU:{resp}"
                                        )
                                    else:
                                        self.system_prompt_contexts_history += f"\nYOU(SystemNote:{get_current_timestamp()}):{resp}"
                                    self.generate_system_prompt_with_context(
                                        context_string=self.system_prompt_contexts_history
                                    )
                                    self.updateSysMessage()
                                return resp
                return self.ava_main_executor(
                    messages=messages, tools_list=tools_list, ava_llm=ava_llm
                )

            else:
                """THIS MEANS THE AGENT JUST REPLIED NORMALLY WITHOUT FUNCTION OR TOOL CALLING"""

                agent_mes = llm_resp.choices[0].message.content
                self.appendToMessages(role="assistant", content=agent_mes)
                if self.use_system_prompt_as_context:
                    if not self.include_message_timestap:
                        self.system_prompt_contexts_history += f"\nYOU:{agent_mes}"
                    else:
                        self.system_prompt_contexts_history += (
                            f"\nYOU(SystemNote:{get_current_timestamp()}):{agent_mes}"
                        )
                    self.generate_system_prompt_with_context(
                        context_string=self.system_prompt_contexts_history
                    )
                    self.updateSysMessage()

                if self.logging:
                    print(
                        f"{self.agent_name_identifier.capitalize()} message: ",
                        agent_mes,
                        color="yellow",
                    )
                    print()
                if self.callback_handler and hasattr(
                    self.callback_handler, "on_general_response"
                ):
                    self.callback_handler.on_general_response(response=agent_mes)
                self.current_agent_iteration = 0
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "TTS STREAMING VAL:",
                    self.tts_streaming,
                )
                if self.tts_streaming:
                    pass
                    # play_carts_tts(text=agent_mes)
                return agent_mes

    def complete_streaming_openai_llm_response(
        self,
        llm_resp,
        messages: List[dict],
        tools_list: List[BaseTool],
        ava_llm: OpenaiLLM,
        start_time: float,
    ):
        response_text: str = ""
        previous_chunk = ""
        stop_reason = None
        function_chunk = None
        tts_chunk: str = ""
        function_response = {
            "name": "",
            "arguments": "",
            "id": "",
            "tool_call_model_dump": {},
        }
        function_calls_list = []
        speech = True
        is_function_call = False

        # start_time = time.time()
        first_token_received = False

        for line in llm_resp:
            if not first_token_received:
                first_token_received = True
                elapsed = time.time() - start_time
                print(f"\nTime to first token: {elapsed:.3f} seconds\n", color="blue")

            if self.logging:
                print(
                    self.agent_name_identifier.capitalize(),
                    ": ",
                    "Openai LLM streaming line: ",
                    line,
                    line,
                    color="green",
                )
                print()
            chunk = None

            if len(line.choices) < 1:
                continue

            if line.choices[0].finish_reason:
                print("", end="\n", flush=True)
                stop_reason = line.choices[0].finish_reason
                if self.logging:
                    print(
                        self.agent_name_identifier.capitalize(),
                        ": ",
                        "Steams ends with reason: ",
                        stop_reason,
                        "\nFUNCTION CALL: ",
                        is_function_call,
                    )
                break
            if line.choices[0].delta:
                chunk = line.choices[0].delta.content
                # tts_chunk = chunk
                function_chunk = line.choices[0].delta.tool_calls
            if function_chunk:
                is_function_call = True
                # print("TOOL CALLED!", function_chunk)
                for tool_call in function_chunk:
                    function_info = tool_call.function

                    if tool_call.id:
                        function_response["id"] += tool_call.id
                    if tool_call.model_dump().get("id", None):
                        function_response["tool_call_model_dump"].update(
                            tool_call.model_dump()
                        )
                    if function_info.name:
                        function_response["name"] += function_info.name
                        function_response["tool_call_model_dump"]["function"][
                            "name"
                        ] = function_response["name"] + function_info.name

                    if function_info.arguments:
                        function_response["arguments"] += function_info.arguments
                        function_response["tool_call_model_dump"]["function"][
                            "arguments"
                        ] = function_response["arguments"] + function_info.arguments

                        # function_response["tool_call_model_dump"]["function"] = {
                        #     "arguments": function_response["name"],
                        #     "name": function_response["arguments"],
                        # }
                    # function_response+=tool_call.

                print(
                    f"{self.agent_name_identifier.capitalize()} Tool call : ",
                    function_response,
                    color="yellow",
                    end="\r",
                    flush=True,
                )

            # elif line
            elif chunk and chunk != previous_chunk and function_chunk is None:
                is_function_call = False
                # print("CHUNK:", chunk)
                # yield chunk.encode('utf-8') + b'\n'
                response_text += chunk
                tts_chunk += chunk
                if self.callback_handler and hasattr(
                    self.callback_handler, "on_streaming_chunk"
                ):
                    self.callback_handler.on_streaming_chunk(chunk=chunk)
                # Debugging statements
                # print("Received chunk:", chunk)
                # print("Updated response_text:", response_text)
                # Clear the previous line and print the updated text
                if self.print_tts_streaming:
                    print(
                        f"{self.agent_name_identifier.capitalize()} message: ",
                        response_text,
                        color="yellow",
                        end="\r",
                        flush=True,
                    )
                previous_chunk = chunk
                # Check if the chunk ends with a sentence-ending punctuation
                if tts_chunk.strip()[-1] in {
                    ".",
                    "!",
                    "?",
                }:  # Used to play one sentence at a time
                    if self.tts_streaming == True:
                        # pass
                        # text_to_speech(chunk)
                        # play_tts_audio(
                        #     text=tts_chunk,
                        #     speaker="eva",
                        #     sampling_rate=10000,
                        #     speed_alpha=1.0,
                        #     reduce_latency=True,
                        #     authorization_token="M1jSmw004ffRB352M20OE1jGzncs0ualtgiIwXs_5nY"
                        # )

                        # auraTTS(
                        #     text=tts_chunk,
                        #     api_key="5cccacec5b580bca8a4d77f1f8e11424496ec8b1",
                        #     output_file="output_audio.mp3",
                        # )
                        # asyncio.run(cart_main(voice="dfs", transcript=tts_chunk))
                        # await cart_main(voice="dfs", transcript=tts_chunk)
                        # loop = asyncio.get_event_loop()
                        # if (
                        #     loop.is_running()
                        # ):  # Check if the event loop is already running
                        #     # Schedule the task to run in the current event loop
                        #     print(
                        #         self.agent_name_identifier.capitalize(),
                        #         ": ",
                        #         "playing cart tts",
                        #     )
                        #     loop.create_task(
                        #         cart_main(voice="dfs", transcript=tts_chunk)
                        #     )
                        # else:
                        #     print(
                        #         self.agent_name_identifier.capitalize(),
                        #         ": ",
                        #         "playing cart tts",
                        #     )
                        #     # If for some reason the loop isn't running (which is unlikely in a typical asyncio context),
                        #     # you might want the event loop, but usually, you'd want to use create_task as above
                        #     asyncio.run(cart_main(voice="dfs", transcript=tts_chunk))

                        tts_chunk = ""

        # Print a newline after the streaming is finished
        print("", end="\n", flush=True)
        if not is_function_call:
            agent_mes = response_text
            self.appendToMessages(role="assistant", content=agent_mes)
            if self.use_system_prompt_as_context:
                if not self.include_message_timestap:
                    self.system_prompt_contexts_history += f"\nYOU:{agent_mes}"
                else:
                    self.system_prompt_contexts_history += (
                        f"\nYOU(SystemNote:{get_current_timestamp()}):{agent_mes}"
                    )
                self.generate_system_prompt_with_context(
                    context_string=self.system_prompt_contexts_history
                )
                self.updateSysMessage()

            # if self.logging:
            #     print(f"{self.agent_name_identifier.capitalize()} message: ",
            #           agent_mes, color='yellow')
            #     print()
            if self.callback_handler and hasattr(
                self.callback_handler, "on_general_response"
            ):
                self.callback_handler.on_general_response(response=agent_mes)
            self.current_agent_iteration = 0
            return agent_mes

        else:
            """This means there is streaming function or say tool call fuckkkkkkkkk"""

            if function_response:
                name = function_response["name"]
                params = function_response["arguments"]
                id = function_response["id"]
                tool_call_dump = function_response["tool_call_model_dump"]
                tool_call_dump["function"]["name"] = name

                print(f"tool call model dump:{tool_call_dump} ")
                messages.append(
                    {"role": "assistant", "content": "", "tool_calls": [tool_call_dump]}
                    # llm_resp.message
                    # if not self.is_non_gpt_model
                    # else {
                    #     "role": "ass",
                    #     "content": "",
                    #     "tool_calls": [
                    #         tool_call.model_dump()
                    #         for tool_call in llm_resp.choices[0].message.tool_calls
                    #     ],
                    # }
                )
                if name:
                    if self.logging:
                        print(
                            self.agent_name_identifier.capitalize(),
                            ": ",
                            f"Executing tool '{name}' ... with param(s): ",
                            f"'{params}'",
                            "\n",
                            color="yellow",
                        )
                    if self.callback_handler and hasattr(
                        self.callback_handler, "on_tool_call"
                    ):
                        self.callback_handler.on_tool_call(
                            tool_name=name, tool_params=params
                        )

                    resp, is_direct = find_and_execute_tool(
                        tool_name=name,
                        tool_params=json.loads(params),
                        tools_list=tools_list,
                    )

                    if resp:
                        if self.logging:
                            print(
                                self.agent_name_identifier.capitalize(),
                                ": ",
                                f"Tool '{name}' response: ",
                                resp,
                                "\n",
                                color="blue",
                            )

                        # messages.append({"role": "function", "name": name, "content": resp})
                        if isinstance(self.ava_llm, MistralAILLM):
                            messages.append(
                                MistralChatMessage(role="tool", name=name, content=resp)
                            )
                        elif self.isOpenaiLLM:
                            messages.append(
                                {
                                    # "role": "tool",
                                    # "content": resp
                                    "tool_call_id": id,
                                    "role": "tool",
                                    "name": name,
                                    "content": resp,
                                }
                            )
                        if self.use_system_prompt_as_context:
                            self.system_prompt_contexts_history += (
                                f"\nTOOL({name}): {resp}"
                            )
                        # if
                        # Passin updated values in the recursive call
                        if is_direct:
                            if self.logging:
                                print(
                                    self.agent_name_identifier.capitalize(),
                                    ": ",
                                    "Returning tool response as direct message",
                                    "\n",
                                    color="magenta",
                                )
                                print(
                                    self.agent_name_identifier,
                                    ": ",
                                    f"{self.agent_name_identifier.capitalize()} message: ",
                                    resp,
                                    color="yellow",
                                )
                                print()

                            self.appendToMessages(role="assistant", content=resp)
                            if self.use_system_prompt_as_context:
                                if not self.include_message_timestap:
                                    self.system_prompt_contexts_history += (
                                        f"\nYOU:{resp}"
                                    )
                                else:
                                    self.system_prompt_contexts_history += f"\nYOU(SystemNote:{get_current_timestamp()}):{resp}"
                                self.generate_system_prompt_with_context(
                                    context_string=self.system_prompt_contexts_history
                                )
                                self.updateSysMessage()
                            return resp
            return self.ava_main_executor(
                messages=messages, tools_list=tools_list, ava_llm=ava_llm
            )

    def prepare_conversation_history_summary(
        self,
    ):
        """This function is for preparing and conversation summary from the prioer messages"""

        pass


import ast
