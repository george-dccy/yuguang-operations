# yg-notion-content-operation — Yu Guang Notion Content Operations

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-notion-content-operation`.

## Natural-language invocation

Hermes should invoke this skill automatically whenever the user asks to inspect, retrieve, prepare, or update Yu Guang publishing tasks in Notion.

The user does **not** need to name this skill explicitly.

Typical requests include:

- “看看 07 里有哪些待发布内容”
- “把今天已认可的内容准备好”
- “找一下待执行的发布任务”
- “从 Notion 读取这条内容的图片和文案”
- “更新这条任务的自动化状态”

Explicit `/yg-notion-content-operation` invocation remains optional.

## Role

Read Yu Guang Notion content assets, identify executable publishing tasks, and prepare structured tasks for publisher skills.

Do not create visual concepts. Do not judge image quality.

## Source of Truth

Notion is the content-operation source of truth.

Primary database:

07｜内容任务与发布包库

## Publish Eligibility

Only prepare executable publishing tasks when:

- Status = 已定稿
- Human Approval Status = 已认可
- Automation Status = 待执行

Never treat the following as publishable assets:

- unfinished content
- unapproved images
- experimental generation results
- images directly from 03 generation tasks
- unselected 05 results

## Asset Rules

Read final publishing images only from:

- Content Images

## Output

Create one normalized PublishTask per target platform:

```yaml
task_id:
platform:
images:
title:
body:
tags:
publish_instruction:
```

## State updates

Supported Automation Status transitions:

- 待执行 -> 执行中
- 执行中 -> 已完成
- 执行中 -> 执行失败

Keep Publishing Record updated.

Saving a platform draft does **not** mean Status = 已发布.
