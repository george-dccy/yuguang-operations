# Yu Guang Notion MCP Initialization Checklist

This checklist supports `yg-setup`.

The Yu Guang skill package does not contain user credentials or workspace secrets. Notion access must be supplied by the user's configured Hermes MCP connection.

## First run

1. Enable the Notion MCP server in Hermes.
2. Authenticate the user's Notion account.
3. Verify access to 07｜内容任务与发布包库.
4. Verify required properties.
5. Store only local runtime references needed by the Yu Guang deployment.

## Required fields

- Status
- Human Approval Status
- Automation Status
- Content Images
- Platform Copy
- Platforms
- Publish Instruction
- Publishing Record

## Validation

The environment must be able to:

- query pending automation tasks
- read approved Content Images
- read platform copy
- prepare a PublishTask
- write execution status back after publishing operations

Do not modify or publish content during this validation.
