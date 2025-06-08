"""Calculate project progress percentage.

Usage:
    python3 progress.py TOTAL TASKS COMPLETED
"""

import argparse


def calculate_percentage(total_tasks: int, completed_tasks: int) -> float:
    """Return the completion percentage.

    Args:
        total_tasks: Total number of tasks in the project.
        completed_tasks: Number of tasks completed so far.

    Returns:
        The completion percentage as a float.

    Raises:
        ValueError: If any of the arguments are invalid.
    """
    if total_tasks <= 0:
        raise ValueError("Total tasks must be greater than zero")
    if completed_tasks < 0:
        raise ValueError("Completed tasks cannot be negative")
    if completed_tasks > total_tasks:
        raise ValueError("Completed tasks cannot exceed total tasks")
    return (completed_tasks / total_tasks) * 100


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate project progress percentage")
    parser.add_argument("total_tasks", type=int, help="Total number of tasks")
    parser.add_argument("completed_tasks", type=int, help="Number of completed tasks")
    args = parser.parse_args()

    percentage = calculate_percentage(args.total_tasks, args.completed_tasks)
    print(f"Project completion: {percentage:.2f}%")


if __name__ == "__main__":
    main()
