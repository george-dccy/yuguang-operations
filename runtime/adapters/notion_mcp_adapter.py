"""
Notion MCP adapter skeleton.

Responsibilities:
- query 07 content task database;
- filter executable tasks;
- transform Notion pages into PublishTask.

The actual MCP client should be injected by the Hermes runtime.
"""


class NotionMCPAdapter:
    def __init__(self, notion_client, database_id):
        self.notion_client = notion_client
        self.database_id = database_id

    def get_pending_tasks(self):
        """Return tasks where Automation Status is ready for execution."""
        # Implementation depends on the Hermes MCP runtime.
        return []

    def to_publish_task(self, page):
        """Convert a Notion page into a normalized PublishTask."""
        return {
            "task_id": page.get("id"),
            "platforms": page.get("platforms", []),
            "images": page.get("content_images", []),
            "copy": page.get("platform_copy", {}),
            "instruction": page.get("publish_instruction", ""),
        }
