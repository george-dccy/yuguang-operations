# Hermes Runtime Flow

## Overview

Hermes is the Yu Guang operation orchestrator.

Users normally interact through natural conversation. Hermes should infer and invoke the matching `yg-*` skills; explicit skill names are optional.

## Scheduled Trigger

Example, every hour:

1. `yg-content-operation-scheduler` checks Notion 07.
2. `yg-notion-content-operation` identifies eligible tasks.
3. `yg-publish-orchestrator` validates and routes each task.
4. One platform publisher executes:
   - `yg-xiaohongshu-publisher`
   - `yg-douyin-publisher`
   - `yg-wechat-mp-publisher`
5. browser-use creates the platform draft.
6. execution result is written back to Notion.

## Execution Chain

```
Hermes scheduler / natural-language request
        |
        v
yg-content-operation-scheduler (when scheduled)
        |
        v
yg-notion-content-operation
        |
        v
yg-publish-orchestrator
        |
        v
yg-*-publisher
        |
        v
browser-use
        |
        v
Platform Draft
```

## After Execution

Success:

- Automation Status = 已完成
- Publishing Record updated
- Status remains unchanged unless public publication actually occurred

Failure:

- Automation Status = 执行失败
- error recorded

## Safety

Default: create draft only.

Human remains the final public-publishing gate.
