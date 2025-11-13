# What is the Capital of France?

A simple example experiment demonstrating the Compass framework with Inspect AI.

## Description

This experiment uses Inspect AI to evaluate a model's ability to answer a simple geography question. It demonstrates:
- Pydantic-based parameter configuration via environment variables
- Inspect AI integration with tasks, datasets, and scorers
- Structured result output with relative fsspec paths
- The Compass contract for experiment design

**Default question**: "What is the capital of France?"

## Compass Contract

This experiment follows the Compass contract:
1. **Uses Inspect AI** to define tasks and run evaluations
2. **Returns results** with `output_path` (relative path) and `data` keys
3. **Compass framework** handles writing to the configured storage location

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
uv run python -m what_is_capital_of_france.run

# Or run through Compass (handles storage automatically)
compass run what-is-capital-of-france
```

With custom parameters:

```bash
PROMPT="What is the capital of Germany?" EXPECTED_ANSWER="Berlin" \
  uv run python -m what_is_capital_of_france.run
```

## Docker

Build and run with Docker:

```bash
docker build -t what-is-capital-of-france .
docker run -e OPENAI_API_KEY="your-key" what-is-capital-of-france
```

## Output

The experiment outputs JSON with:
- `output_path`: Relative path where results should be stored (fsspec compatible)
- `data`: The experiment results containing:
  - `timestamp`: When the experiment ran
  - `parameters`: Configuration used (model_name, prompt, expected_answer)
  - `results`: Evaluation outcomes (scores, samples, etc.)

Example output:

```json
{
  "output_path": "what-is-capital-of-france/2024-11-13T10-30-45.123456/results.json",
  "data": {
    "timestamp": "2024-11-13T10:30:45.123456",
    "parameters": {
      "model_name": "openai/gpt-4",
      "prompt": "What is the capital of France?",
      "expected_answer": "Paris"
    },
    "results": {
      "total_samples": 1,
      "scores": {
        "match": {
          "value": 1.0
        }
      },
      "samples": [
        {
          "input": "What is the capital of France?",
          "target": "Paris",
          "output": "Paris",
          "score": 1.0
        }
      ]
    }
  }
}
```

## Storage

When run through Compass, the framework handles storage to the configured location (local, S3, GCS, Azure, etc.). The experiment provides the relative `output_path`, and Compass combines it with the base storage location from settings.

