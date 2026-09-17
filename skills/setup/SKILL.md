# Setup Skill

## Purpose

Initialize the Yu Guang Operations environment before running Hermes automation.

This skill handles configuration, not content operations.

## Responsibilities

1. Verify required capabilities:

- Notion MCP connection
- browser-use runtime
- Hermes scheduler

2. Collect runtime configuration:

- Notion workspace connection
- Content task database id
- Browser profile path
- Enabled platforms

## Separation of Concerns

### Skill
Defines:

- what to read
- what fields are required
- workflow rules

### MCP
Provides:

- authenticated connection to external services
- Notion data access

### Config
Stores:

- user-specific ids
- runtime parameters

## Notion Initialization

After connecting Notion MCP, verify access to:

07｜内容任务与发布包库

Required fields:

- Status
- Human Approval Status
- Automation Status
- Content Images
- Platform Copy
- Platforms
- Publish Instruction

## Validation

A successful setup should return:

- database accessible
- required fields found
- browser runtime available
- scheduler ready

## Safety

Do not publish during setup.
Do not modify user content during setup.
