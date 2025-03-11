import os
from ai.jobfile import InferenceCommand
from openai import OpenAI


class Chat:
    def __init__(self, system: str, tools: dict):
        self._client = self.get_client()
        self.messages = []
        self.system = system
        self.tools = tools

    def get_client(self):
        return OpenAI(
            api_key=os.environ.get("SILICON_FLOW_API_KEY"),
            base_url="https://api.siliconflow.cn/v1"
        )

    def send_messages(self, prompt: str, inference: InferenceCommand):
        tools = [{
            "type": "function",
            "function": tool.model_dump()
        }
            for tool in inference.tools
        ]
        if not self.messages:
            self.messages.append({
                "role": "system",
                "content": inference.system_prompt
            })

        self.messages.append({
            "role": "user",
            "content": prompt
        })

        response = self._client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=self.messages,
            tools=tools,  # type: ignore
        )

        self.messages.append(response.choices[0].message.model_dump())

        tool_calls = response.choices[0].message.tool_calls or []
        for tool_call in tool_calls:
            if tool_call.function.name in self.tools:
                tool = self.tools[tool_call.function.name]
                tool.run(tool_call)
                function_response = tool.result
            else:
                function_response = "I don't know how to run this tool"

            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": function_response
            })

            response = self._client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=self.messages,
                tools=tools,  # type: ignore
            )

        self.messages.append(response.choices[0].message.model_dump())
        return response.choices[0].message.model_dump()
