"""Hermes publish runner MVP.

Flow:
Notion -> PublishTask -> Orchestrator -> Platform Adapter.
"""

from notion_reader import get_pending_publish_tasks, build_publish_task


def execute_task(task):
    """Placeholder for Publish Orchestrator integration."""
    return {
        "task_id": task["task_id"],
        "status": "not_implemented",
    }


def run_once():
    pages = get_pending_publish_tasks()
    results = []

    for page in pages:
        task = build_publish_task(page)
        results.append(execute_task(task))

    return results


if __name__ == "__main__":
    print(run_once())
