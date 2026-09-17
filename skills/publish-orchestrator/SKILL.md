# Publish Orchestrator Skill

## Role

Coordinate publishing workflow after Notion approval.

Input:

PublishTask from notion-content-operation.

Output:

PublishResult.

## Workflow

1. Validate assets.
2. Select platform adapter.
3. Invoke browser automation capability.
4. Create platform draft.
5. Return execution result.
6. Update Notion.

## Safety

Default behavior:

SAVE DRAFT ONLY.

Never click final publish unless explicitly instructed.

## Browser Layer

Use browser-use runtime.

Do not implement custom browser automation here.

Platform-specific behavior belongs to adapters.
