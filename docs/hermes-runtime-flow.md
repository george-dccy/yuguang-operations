# Hermes Runtime Flow

## Overview

Hermes is the operation orchestrator.

It does not create content decisions. It executes approved workflows.

## Scheduled Trigger

Example:

Every hour:

1. Query Notion 07 content database.
2. Find tasks where:

- Automation Status = 待执行

3. Build PublishTask.
4. Send to Publish Orchestrator.

## Execution Chain

```
Hermes Scheduler
        |
        v
Notion Content Operation
        |
        v
Publish Orchestrator
        |
        v
Platform Adapter
        |
        v
browser-use
        |
        v
Platform Draft
```

## After Execution

Update Notion:

Success:

- Automation Status = 已完成
- Publishing Record updated

Failure:

- Automation Status = 执行失败
- Error recorded

## Safety

Default:

Create draft only.

Human remains final publisher.
