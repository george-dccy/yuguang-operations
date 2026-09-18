# Yu Guang Xiaohongshu Browser Flow

Supports `yg-xiaohongshu-publisher`.

## Preconditions

Before opening browser:

- PublishTask is validated
- Content Images are available
- title/body are approved
- authenticated browser session exists

## Flow

1. Open Xiaohongshu creator platform.
2. Confirm current account.
3. Enter image-post creation workflow.
4. Upload approved images in original order.
5. Fill approved title.
6. Fill approved body text.
7. Fill approved tags if provided.
8. Save draft.
9. Verify draft saved.
10. Return execution result.

## Forbidden actions

- do not click final publish
- do not edit images
- do not rewrite copy
- do not invent hashtags
- do not switch accounts automatically

## Failure handling

If login expires, upload fails, or page structure is ambiguous:

- stop execution
- record failure reason
- return control to `yg-publish-orchestrator`
