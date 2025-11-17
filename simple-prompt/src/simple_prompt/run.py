#!/usr/bin/env python3
"""Run an experiment that asks a simple prompt"""

import sys

from inspect_ai import Task, eval, task  
from inspect_ai.dataset import Sample 
from inspect_ai.log import EvalLog
from inspect_ai.scorer import match 
from inspect_ai.solver import generate, system_message 

from .parameters import Parameters

@task
def _task(parameters: Parameters) -> Task:
    """Define an Inspect AI task that asks a simple prompt.

    Args:
        parameters: Experiment parameters containing the prompt

    Returns:
        Task: An Inspect AI task with the dataset, plan, and scorer
    """
    dataset = [
        Sample(input=parameters.prompt, target=parameters.expected_answer),
    ]

    plan = [
        system_message("You are a helpful assistant. Answer questions concisely."),
        generate(), 
    ]

    return Task(
        dataset=dataset,
        plan=plan,
        scorer=match(),  
    )


def _run(parameters: Parameters) -> EvalLog:
    """Run the experiment using Inspect AI.

    Compass Contract:
        1. Define Inspect AI tasks (see _task() above)
        2. Run eval() with the task and model
        3. Return results dict with 'output_path' and 'data' keys
        4. Compass framework will write 'data' to the configured storage location

    Args:
        parameters: Experiment parameters

    Returns:
        EvalLog: Inspect AI evaluation results
    """
    print(f"Running experiment with model: {parameters.model_name}")
    print(f"Prompt: {parameters.prompt}")

    return eval(
        _task(parameters),
        model=parameters.model_name,
        log_dir=parameters.log_dir,
    )

def main() -> EvalLog:
    """Main entry point.

    Returns:
        EvalLog: Compass evaluation results
    """
    try:
        parameters = Parameters()

        return _run(parameters)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

