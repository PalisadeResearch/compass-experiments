# Simple Prompt

A simple example experiment demonstrating the Compass framework with Inspect AI.

## Installation

```bash
# Install dependencies
uv sync

# Or with pip
pip install -e .
```

## Configuration

Configure the experiment using environment variables:

```bash
# Required: API key for the model provider
export OPENAI_API_KEY="your-key-here"
# Or for other providers:
# export ANTHROPIC_API_KEY="your-key-here"

# Optional: Custom model (in Inspect AI format: provider/model)
export MODEL_NAME="openai/gpt-4o"

# Optional: Custom prompt
export PROMPT="What is the capital of Spain?"

# Optional: Expected answer (for scoring)
export EXPECTED_ANSWER="Madrid"
```

## Running

```bash
# Run directly (prints results to stdout)
uv run python -m simple_prompt.run

# Or run through Compass (handles storage automatically)
compass run simple-prompt
```

With custom parameters:

```bash
PROMPT="What is the capital of Germany?" EXPECTED_ANSWER="Berlin" \
  uv run python -m simple-prompt.run
```

## Docker

Build and run with Docker:

```bash
docker build -t simple-prompt .
docker run -e OPENAI_API_KEY="your-key" simple-prompt
```
