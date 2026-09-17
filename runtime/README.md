# Hermes Runtime MVP

## Current flow

```
Notion 07 Content Tasks
        |
        v
notion_reader.py
        |
        v
PublishTask
        |
        v
publish_runner.py
        |
        v
Publish Orchestrator
        |
        v
Platform Adapter + browser-use
```

## Trigger

Hermes cron should call `run_once()` periodically.

## Safety

- Only process Automation Status = 待执行.
- Create drafts by default.
- Do not publish automatically unless explicitly enabled.
