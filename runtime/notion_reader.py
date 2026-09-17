"""Notion reader interface for Hermes runtime.

This module defines the MVP contract. The actual Notion MCP adapter can be
injected by Hermes environment.
"""


def get_pending_publish_tasks():
    """Return tasks where Automation Status == 待执行.

    Expected output is a list of PublishTask dictionaries.
    """
    return []


def build_publish_task(page):
    return {
        "task_id": page.get("id"),
        "platforms": page.get("platforms", []),
        "images": page.get("content_images", []),
        "copy": page.get("platform_copy", {}),
        "instruction": page.get("publish_instruction", ""),
    }
