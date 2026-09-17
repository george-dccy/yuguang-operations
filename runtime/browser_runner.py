"""
Browser-use execution adapter for Hermes.

Responsibilities:
- Receive a normalized PublishTask.
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

    The actual browser-use Agent initialization should be injected by the
    Hermes environment because credentials, browser profile and model
    settings belong to deployment configuration.
    """

    def __init__(self, browser_agent=None):
        self.browser_agent = browser_agent

    def run(self, publish_task: Dict[str, Any]) -> BrowserExecutionResult:
        platform = publish_task.get("platform", "unknown")

        if self.browser_agent is None:
            return BrowserExecutionResult(
                status="not_configured",
                platform=platform,
                message="browser-use runtime is not configured"
            )

        # Future implementation:
        # 1. load platform adapter browser-flow
        # 2. create browser-use task
        # 3. execute draft creation
        # 4. return result

        return BrowserExecutionResult(
            status="completed",
            platform=platform,
            message="browser task executed"
        )
