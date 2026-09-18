# yg-publish-orchestrator — Yu Guang Publishing Orchestrator

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-publish-orchestrator`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user asks to execute one or more approved Yu Guang publishing tasks, create platform drafts, or coordinate multi-platform publishing.

The user does **not** need to mention this skill by name.

Typical requests include:

- “把这条内容存到对应平台草稿箱”
- “处理 07 里待执行的发布任务”
- “把已认可的内容分别生成小红书和抖音草稿”
- “执行今天的发布任务，但不要真正发布”
- “继续跑余光所及的发布流程”

Explicit `/yg-publish-orchestrator` invocation remains optional.

## Role

Coordinate approved Notion content tasks and dispatch them to the correct Yu Guang platform publisher skill.

Do not create content. Do not judge images. Do not rewrite approved copy.

## Input

Receive a PublishTask:

```yaml
id:
platform:
images:
title:
body:
tags:
publish_instruction:
```

## Preconditions

Only accept tasks satisfying:

- Human Approval Status = 已认可
- Automation Status = 待执行
- Content Images exists

Otherwise stop and report missing requirements.

## Routing

Dispatch by platform:

- xiaohongshu -> `yg-xiaohongshu-publisher`
- douyin -> `yg-douyin-publisher`
- wechat / wechat-mp / 公众号 -> `yg-wechat-mp-publisher`

Do not directly operate platform websites from this skill.

## Execution

1. Validate assets and approval state.
2. Mark Automation Status = 执行中.
3. Normalize PublishTask.
4. Dispatch to the appropriate `yg-*` publisher.
5. Receive PublishResult.
6. Write result to Notion.

## Notion update rules

After successful **draft creation**:

- Automation Status = 已完成
- append Publishing Record
- record execution timestamp/result

Do **not** set Status = 已发布 unless actual public publication has happened.

After failure:

- Automation Status = 执行失败
- record error reason
- preserve retryability

## Safety

Default behavior is **CREATE DRAFT ONLY**.

Never automatically:

- click final publish
- change approved copy
- replace approved images
- invent hashtags
- bypass Human Approval Status
