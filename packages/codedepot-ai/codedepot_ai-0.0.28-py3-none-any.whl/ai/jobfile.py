from typing import Any
import yaml
from pydantic import BaseModel


class GpuSpec(BaseModel):
    minGpusPerNode: int
    minVramPerGPU: int
    totalGpuCount: int


class ParameterSpec(BaseModel):
    type: str
    properties: dict[str, Any]
    required: list[str]


class ToolSpec(BaseModel):
    name: str
    description: str
    parameters: list[ParameterSpec]


class InferenceCommand(BaseModel):
    interface: str  # 'api' or 'webapp'
    system_prompt: str
    tools: list[ToolSpec]
    tool_file: str


class JobSpec(BaseModel):
    name: str
    command: list[str]
    gpuSpec: GpuSpec | None = None

    @classmethod
    def from_file(cls, filename: str) -> 'JobSpec':
        """
        Load a ClusterSpec from a file
        """
        with open(filename, 'r') as file:
            y = yaml.load(file, Loader=yaml.FullLoader)
            return cls(**y)
