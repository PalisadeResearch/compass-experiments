#!/usr/bin/env python3
"""Run an experiment that sends a request to OpenAI API and returns the response."""

import json
import sys

from openai import OpenAI  # pyright: ignore[reportMissingImports]

from .parameters import Parameters


def run_experiment(parameters: Parameters):
    """Run the experiment using OpenAI API."""
    model_config = parameters.model
    prompt = parameters.prompt

    # Get model provider and name from the config object
    provider = model_config.provider
    model_name = model_config.model

    client = OpenAI()

    # Send request to OpenAI API
    response = client.chat.completions.create(
        model=model_name, messages=[{"role": "user", "content": prompt}]
    )

    # Extract the response content
    result = {
        "provider": provider,
        "model": model_name,
        "prompt": prompt,
        "response": response.choices[0].message.content,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        },
        "finish_reason": response.choices[0].finish_reason,
    }

    return result


def main():
    """Main entry point."""
    try:
        parameters = Parameters()
        result = run_experiment(parameters)

        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

