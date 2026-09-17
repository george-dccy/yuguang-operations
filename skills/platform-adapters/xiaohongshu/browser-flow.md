# Xiaohongshu Browser Flow

## Purpose

Define browser-use execution steps for creating Xiaohongshu drafts.

Browser-use is responsible for interaction. This document defines business flow only.

## Preconditions

Before opening browser:

- PublishTask is validated.
- Images are available from Notion Content Images.
- Title and body are available.
- User login session exists.

## Flow

1. Open Xiaohongshu creator platform.
2. Confirm current account.
3. Enter image post creation workflow.
4. Upload approved images.
5. Fill title.
6. Fill body text.
7. Fill tags if provided.
8. Save draft.
9. Return execution result.

## Forbidden Actions

- Do not click final publish.
- Do not edit images.
- Do not rewrite copy.
- Do not add unrelated hashtags.

## Failure Handling

If login expires, upload fails, or page structure changes:

- stop execution;
- record failure reason;
- keep Automation Status unchanged or mark failed according to orchestrator rules.
