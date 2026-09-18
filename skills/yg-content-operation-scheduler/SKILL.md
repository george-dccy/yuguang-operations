# yg-content-operation-scheduler — Yu Guang Operations Scheduler

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-content-operation-scheduler`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user asks for recurring Yu Guang checks, periodic publishing operations, queue monitoring, or scheduled review reminders.

The user does **not** need to name this skill.

Typical requests include:

- “每小时检查一次余光所及有没有待发布任务”
- “定时巡检 07 内容库”
- “自动处理待执行任务”
- “每天看看有没有发布后还没复盘的内容”
- “帮我建立余光运营的定时任务”

Explicit `/yg-content-operation-scheduler` invocation remains optional.

## Role

Define how Hermes periodically checks and operates the Yu Guang content system.

Hermes cron or another scheduler provides the trigger; this skill provides the business workflow.

## Recommended trigger

Default operational check:

- every hour

## Publish Queue

Find 07 records where:

- Automation Status = 待执行
- Human Approval Status = 已认可

Then invoke:

1. `yg-notion-content-operation`
2. `yg-publish-orchestrator`
3. the appropriate `yg-*-publisher`

If there are no executable tasks, exit quietly.

## Asset Reminder

Find records where:

- Human Approval Status = 已认可
- Content Images is empty

Create a reminder for manual asset upload; do not attempt publishing.

## Review Reminder

Find records where:

- Status = 已发布
- Review Summary is empty

Create a review reminder.

## Principles

The scheduler must not:

- create content
- select visual winners
- judge image quality
- bypass approval
- publicly publish by default
