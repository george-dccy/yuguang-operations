"""
Hermes runtime entry point.

This is a minimal orchestration skeleton.
Actual Notion and browser integrations should be injected by runtime adapters.
"""


def scan_tasks():
    """Query Notion for executable publishing tasks."""
    return []


def execute_publish(task):
    """Send PublishTask to publish orchestrator."""
    pass


def run_once():
    tasks = scan_tasks()
    for task in tasks:
        execute_publish(task)


if __name__ == "__main__":
    run_once()
