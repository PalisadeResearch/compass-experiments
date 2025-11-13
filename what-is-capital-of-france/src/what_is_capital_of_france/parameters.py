"""Pydantic models for experiment parameters."""

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings  # pyright: ignore[reportMissingImports]


class ModelConfig(BaseModel):
    """Configuration for a model with provider and model name."""

    provider: str = Field(..., description="Model provider (e.g., 'openai', 'anthropic')")
    model: str = Field(..., description="Model name (e.g., 'gpt-4.1', 'claude-3-opus')")


class ModelEnum(Enum):
    """Enumeration of supported models."""

    GPT_4_1 = ModelConfig(provider="openai", model="gpt-4.1")


class Parameters(BaseSettings):
    """Experiment parameters loaded from environment variables."""

    model: ModelConfig = Field(
        default=ModelEnum.GPT_4_1.value, description="Model to use for the experiment"
    )
    prompt: str = Field(
        default="What is the capital of France?", description="Prompt to use for the experiment"
    )

    model_config = ConfigDict()

