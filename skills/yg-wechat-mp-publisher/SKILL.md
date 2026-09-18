# yg-wechat-mp-publisher — Yu Guang WeChat Official Account Publisher

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-wechat-mp-publisher`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user asks to create, save, retry, or inspect a **Yu Guang WeChat Official Account / 公众号 draft**.

The user does **not** need to mention this skill name.

Typical requests include:

- “把这篇放到公众号草稿箱”
- “生成微信公众号草稿”
- “执行 07 里这条公众号长文”
- “重试公众号草稿任务”

Explicit `/yg-wechat-mp-publisher` invocation remains optional.

## Role

Create WeChat Official Account article drafts from approved Yu Guang PublishTasks.

## Input

- approved cover image
- approved Content Images
- approved title
- approved long-form body
- Publish Instruction

## Preconditions

- Human Approval Status = 已认可
- Automation Status = 待执行 or 执行中 under orchestrator control
- required article assets exist
- Platforms includes 公众号 / 微信

## Workflow

1. Open WeChat Official Account editor using authenticated browser profile.
2. Create article draft.
3. Upload approved images.
4. Fill approved title and body.
5. Save draft.
6. Verify draft saved.
7. Return execution result.

## Safety

Default behavior: **SAVE DRAFT ONLY**.

Never automatically publish, rewrite the article, or replace approved assets.
