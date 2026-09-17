"""
End-to-end Hermes publish workflow.

Flow:
Notion MCP -> PublishTask -> Orchestrator -> Browser Runner -> Notion Writer
"""

from runtime.adapters.notion_mcp_adapter import NotionMCPAdapter
from runtime.adapters.notion_writer import NotionWriter
from runtime.browser_runner import BrowserRunner


class HermesPublishFlow:
    def __init__(self, notion_reader=None, orchestrator=None, browser_runner=None, notion_writer=None):
        self.notion_reader = notion_reader or NotionMCPAdapter()
        self.orchestrator = orchestrator
        self.browser_runner = browser_runner or BrowserRunner()
        self.notion_writer = notion_writer or NotionWriter()

    def run_once(self):
        tasks = self.notion_reader.get_pending_tasks()
        results = []

        for task in tasks:
            try:
                publish_tasks = self.orchestrator.build_tasks(task) if self.orchestrator else [task]

                for publish_task in publish_tasks:
                    result = self.browser_runner.run(publish_task)
                    results.append(result)

                    if result.status == "completed":
                        self.notion_writer.mark_completed(task, result)
                    else:
                        self.notion_writer.mark_failed(task, result)

            except Exception as exc:
                self.notion_writer.mark_error(task, str(exc))

        return results
