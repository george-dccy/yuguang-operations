"""Retry policy for Hermes publishing workflow."""

from dataclasses import dataclass


@dataclass
class RetryPolicy:
    max_attempts: int = 3
    retry_delay_seconds: int = 60

    def should_retry(self, attempts: int) -> bool:
        return attempts < self.max_attempts
