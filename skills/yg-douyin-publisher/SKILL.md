# yg-douyin-publisher — Yu Guang Douyin Publisher

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-douyin-publisher`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user asks to create, save, retry, or inspect a **Yu Guang Douyin draft**.

The user does **not** need to mention this skill name.

Typical requests include:

- “把这条内容存到抖音草稿箱”
- “帮我准备抖音图文草稿”
- “执行 07 里的抖音任务”
- “重试这条抖音发布任务”

Explicit `/yg-douyin-publisher` invocation remains optional.

## Role

Create Douyin drafts from approved Yu Guang PublishTasks.

## Input

- approved Content Images
- approved video assets if explicitly present
- approved title/body/tags
- Publish Instruction

## Preconditions

- Human Approval Status = 已认可
- Automation Status = 待执行 or 执行中 under orchestrator control
- approved platform assets exist
- Platforms includes 抖音

## Workflow

1. Open Douyin creator platform using authenticated browser profile.
2. Enter the correct image/video creation workflow.
3. Upload only approved assets.
4. Fill approved copy.
5. Save draft.
6. Verify draft saved.
7. Return execution result.

## Safety

Default behavior: **SAVE DRAFT ONLY**.

Never automatically publish, rewrite copy, replace assets, or invent tags.
