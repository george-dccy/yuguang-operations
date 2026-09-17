# Hermes Production Deployment Guide

## Components

- Hermes Agent: scheduler and orchestration
- Notion MCP: content source and status update
- yuguang-operations skills: business rules
- browser-use: browser execution runtime

## Deployment

1. Install Hermes environment.
2. Install this repository skills.
3. Configure Notion MCP connection.
4. Install browser-use.
5. Configure Chrome browser profile.
6. Start scheduler.

## Runtime Flow

```
Cron
 -> Notion query
 -> PublishTask
 -> Publish Orchestrator
 -> Platform Adapter
 -> browser-use
 -> Draft saved
 -> Notion update
```

## Safety

Default mode:

- create drafts only
- no automatic public publishing
- human approval remains final gate
