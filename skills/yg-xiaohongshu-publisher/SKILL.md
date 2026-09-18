# yg-xiaohongshu-publisher — Yu Guang Xiaohongshu Publisher

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-xiaohongshu-publisher`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user asks to create, prepare, save, retry, or inspect a **Yu Guang Xiaohongshu draft**.

The user does **not** need to mention this skill name.

Typical requests include:

- “把这条存到小红书草稿箱”
- “帮我做一个小红书图文草稿”
- “把 07 里这条小红书内容执行掉”
- “重试刚才失败的小红书草稿”

Explicit `/yg-xiaohongshu-publisher` invocation remains optional.

## Role

Execute Xiaohongshu draft creation for an approved Yu Guang PublishTask.

Do not decide content quality, rewrite copy, select images, or generate new assets.

## Preconditions

Only execute when:

- Human Approval Status = 已认可
- Automation Status = 待执行 or currently 执行中 under orchestrator control
- Content Images exists
- Platforms includes 小红书

## Browser

Use browser-use runtime with the configured authenticated browser profile.

If login has expired, stop and request manual authentication.

## Workflow

1. Open Xiaohongshu creator center.
2. Confirm correct authenticated account.
3. Enter image-post creation.
4. Upload Content Images in approved order.
5. Fill approved title.
6. Fill approved body.
7. Add only approved tags.
8. Save draft.
9. Verify that the draft was saved.
10. Return structured result.

## Safety

Default action: **SAVE DRAFT ONLY**.

Never:

- click final publish automatically
- change image order
- edit or crop approved images
- rewrite copy
- add unrelated hashtags

## Output

Return:

- platform
- status
- timestamp
- draft confirmation/reference if available
- error message if failed
