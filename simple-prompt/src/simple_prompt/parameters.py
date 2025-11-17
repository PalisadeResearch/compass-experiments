"""Pydantic models for experiment parameters.

Compass Contract:
    Experiments define their own parameters. Compass framework handles storage.
"""

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Parameters(BaseSettings):
    """Experiment parameters loaded from environment variables."""

    model_name: str = Field(
        default="openai/gpt-4.1",
        description="Model to use for the experiment (e.g., 'openai/gpt-4.1', 'anthropic/claude-4.5-haiku')",
    )

    prompt: str = Field(
        default="What is the capital of France?",
        description="Prompt to use for the experiment",
    )

    expected_answer: str = Field(
        default="Paris",
        description="Expected answer for scoring the model's response",
    )

    log_dir: str | None = Field(
        default="./logs",
        description="Directory to store the logs",
    )

    model_config = ConfigDict(
        env_prefix="",
        case_sensitive=False,
    )

