"""Notion write-back adapter skeleton.

Used after browser automation completes.
"""


class NotionWriter:
    def __init__(self, notion_client):
        self.notion_client = notion_client

    def mark_completed(self, page_id, record):
        """Update automation status and publishing record."""
        return {
            "page_id": page_id,
            "status": "completed",
            "record": record,
        }

    def mark_failed(self, page_id, error):
        """Update failed execution information."""
        return {
            "page_id": page_id,
            "status": "failed",
            "error": str(error),
        }
