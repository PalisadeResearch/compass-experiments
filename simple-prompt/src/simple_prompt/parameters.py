"""Pydantic models for experiment parameters.

Compass Contract:
    Experiments define their own parameters. Compass framework handles storage.
"""

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Parameters(BaseSettings):
    """Experiment parameters loaded from environment variables."""

    # Model to use for evaluation (in Inspect AI format: provider/model)
    model_name: str = Field(
        default="openai/gpt-4.1",
        description="Model to use for the experiment (e.g., 'openai/gpt-4.1', 'anthropic/claude-4.5-haiku')",
    )

    # The question to ask
    prompt: str = Field(
        default="What is the capital of France?",
        description="Prompt to use for the experiment",
    )

    # Expected answer for scoring
    expected_answer: str = Field(
        default="Paris",
        description="Expected answer for scoring the model's response",
    )

    model_config = ConfigDict(
        env_prefix="",  # Prefix for environment variables
        case_sensitive=False,  # Case-insensitive env vars
    )

