# Content Operation Scheduler Skill

## Role

This skill defines how Hermes periodically checks the Yu Guang content system.

The scheduler itself is outside this skill. Hermes cron triggers this workflow.

## Trigger

Recommended frequency:

- every hour

## Check Sources

Read:

Notion 07 Content Task database

## Tasks

### Publish Queue

Find records where:

- Automation Status = 待执行

Action:

Call publish orchestrator.

### Asset Reminder

Find records where:

- Human Approval Status = 已认可
- Content Images is empty

Action:

Create reminder for manual asset upload.

### Review Reminder

Find records where:

- Status = 已发布
- Review Summary is empty

Action:

Create review task.

## Principles

Hermes is a scheduler and executor.

It does not:

- create content
- select winners
- judge image quality
- publish without approval
