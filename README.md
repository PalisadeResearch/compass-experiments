# Compass Experiments

A collection of experiments built with the [Compass](https://github.com/palisade/compass) framework.

## Using These Experiments

### Installation

Each experiment is a standalone Python package. To use an experiment:

```bash
cd simple-prompt
uv sync  # or pip install -e .
```

### Running

Set up your API keys:

```bash
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

Run the experiment:

```bash
uv run python -m simple_prompt.run
```

### Configuration

Experiments use environment variables for configuration. See each experiment's README for specific parameters. You can set the environment variables in the `.env` file.

## Contributing

We welcome contributions! To add a new experiment:

1. Fork this repository
2. Create a new directory for your experiment
3. Follow the structure of existing experiments
4. Add documentation in a README.md
5. Submit a pull request

## Structure

Each experiment should follow this structure:

```
experiment-name/
├── README.md              # Experiment documentation
├── pyproject.toml         # Dependencies and metadata
├── Dockerfile             # Docker setup (optional)
├── src/
│   └── experiment_name/   # Python package (use underscores)
│       ├── __init__.py
│       ├── run.py         # Main entry point
│       └── parameters.py  # Pydantic parameter models
```

## License

See each experiment's directory for licensing information.

