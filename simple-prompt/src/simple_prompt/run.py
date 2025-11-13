#!/usr/bin/env python3
"""Run an experiment that asks 'What is the capital of France?' using Inspect AI.

This experiment demonstrates the Compass framework with Inspect AI:
1. Define an Inspect AI task with dataset, plan, and scorer
2. Run the evaluation
3. Return results with a relative output path
4. Compass framework handles writing to the configured storage location
"""

import json
import sys
from datetime import datetime

from inspect_ai import Task, eval, task  # type: ignore
from inspect_ai.dataset import Sample  # type: ignore
from inspect_ai.scorer import match  # type: ignore
from inspect_ai.solver import generate, system_message  # type: ignore

from .parameters import Parameters


@task
def _task(parameters: Parameters) -> Task:
    """Define an Inspect AI task that asks about the capital of France.

    Args:
        parameters: Experiment parameters containing the prompt

    Returns:
        Task: An Inspect AI task with the dataset, plan, and scorer
    """
    # Create a single-sample dataset with the prompt
    dataset = [
        Sample(input=parameters.prompt, target=parameters.expected_answer),
    ]

    # Define the evaluation plan
    plan = [
        system_message("You are a helpful assistant. Answer questions concisely."),
        generate(),  # Generate a response from the model
    ]

    # Use match scorer to check if the response matches the expected answer
    return Task(
        dataset=dataset,
        plan=plan,
        scorer=match(),  # Exact match scorer
    )


def _run(parameters: Parameters):
    """Run the experiment using Inspect AI.

    Compass Contract:
        1. Define Inspect AI tasks (see capital_of_france_task() above)
        2. Run eval() with the task and model
        3. Return results dict with 'output_path' and 'data' keys
        4. Compass framework will write 'data' to the configured storage location

    Args:
        parameters: Experiment parameters

    Returns:
        dict: Must contain 'output_path' (relative path) and 'data' (results to write)
    """
    print(f"Running experiment with model: {parameters.model_name}")
    print(f"Prompt: {parameters.prompt}")

    # Run Inspect AI evaluation
    results = eval(
        _task(parameters),
        model=parameters.model_name,
    )

    # Get timestamp for output path
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S.%f")

    return {
        "output_path": f"what-is-capital-of-france/{timestamp.replace(':', '-')}/results.json",
        "data": results,
    }


def main():
    """Main entry point.

    When run directly (not through Compass), prints results to stdout.
    When run through Compass, returns results for framework to handle storage.
    """
    try:
        # Load parameters from environment variables
        parameters = Parameters()

        # Run the experiment
        _run(parameters)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

