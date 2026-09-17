"""
Browser-use execution adapter for Hermes.

Responsibilities:
- Receive normalized PublishTask.
- Select platform adapter instructions.
- Invoke browser-use runtime.
- Return structured execution result.

This module intentionally does not contain platform-specific selectors.
Those belong to skills/platform-adapters/*.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BrowserExecutionResult:
    status: str
    platform: str
    message: str = ""


class BrowserRunner:
    """Runtime wrapper around browser-use.

    Browser profile, cookies, model configuration and credentials are injected
    by the Hermes deployment environment.
    """

    def __init__(self, browser_agent=None, adapter_registry=None):
        self.browser_agent = browser_agent
        self.adapter_registry = adapter_registry or {}

    def run(self, publish_task: Dict[str, Any]) -> BrowserExecutionResult:
        platform = publish_task.get("platform", "unknown")
        adapter = self.adapter_registry.get(platform)

        if self.browser_agent is None:
            return BrowserExecutionResult(
                status="not_configured",
                platform=platform,
                message="browser-use runtime is not configured"
            )

        if adapter is None:
            return BrowserExecutionResult(
                status="adapter_missing",
                platform=platform,
                message="no platform adapter configured"
            )

        task = {
            "platform": platform,
            "flow": adapter.get("browser_flow"),
            "payload": publish_task,
        }

        result = self.browser_agent.run(task)

        return BrowserExecutionResult(
            status=result.get("status", "unknown"),
            platform=platform,
            message=result.get("message", "")
        )
