# What is the Capital of France?

A simple example experiment demonstrating the Compass framework basics.

## Description

This experiment sends a question to an AI model and returns the response. It demonstrates:
- Pydantic-based parameter configuration via environment variables
- OpenAI API integration
- Structured result output

**Default question**: "What is the capital of France?"

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
# Required: OpenAI API key
export OPENAI_API_KEY="your-key-here"

# Optional: Custom prompt
export PROMPT="What is the capital of Spain?"

# Optional: Model configuration (JSON format)
export MODEL='{"provider": "openai", "model": "gpt-4o"}'
```

## Running

```bash
uv run python -m what_is_capital_of_france.run
```

Or with custom parameters:

```bash
PROMPT="What is 2+2?" uv run python -m what_is_capital_of_france.run
```

## Docker

Build and run with Docker:

```bash
docker build -t what-is-capital-of-france .
docker run -e OPENAI_API_KEY="your-key" what-is-capital-of-france
```

## Output

The experiment outputs JSON with:
- `provider`: Model provider used
- `model`: Model name
- `prompt`: The question asked
- `response`: The model's response
- `usage`: Token usage statistics
- `finish_reason`: Completion status

Example output:

```json
{
  "provider": "openai",
  "model": "gpt-4.1",
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris.",
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 8,
    "total_tokens": 23
  },
  "finish_reason": "stop"
}
```

