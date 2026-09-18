# yg-setup — Yu Guang Operations Setup

## Identity

This skill belongs exclusively to the **Yu Guang / 余光所及 Operations** project.

Canonical skill name: `yg-setup`.

## Natural-language invocation

Hermes should invoke this skill automatically when the user's intent is to initialize, inspect, repair, or validate the Yu Guang operations environment.

The user does **not** need to type `/yg-setup` or mention this skill by name.

Typical natural-language requests include:

- “检查一下余光所及的运营环境”
- “帮我初始化发布系统”
- “看看 Notion MCP 和 browser-use 配好了没有”
- “把余光项目的运行环境检查一遍”
- “为什么发布自动化还跑不起来”

Explicit invocation with `/yg-setup` remains supported, but is optional.

## Purpose

Initialize and validate the Yu Guang Operations environment before running publishing automation.

This skill handles configuration and capability checks, not content creation or publishing.

## Responsibilities

Verify:

- Notion MCP connection
- access to 07｜内容任务与发布包库
- required Notion properties
- browser-use runtime
- authenticated browser profile
- Hermes scheduler capability
- Yu Guang project configuration

Collect or validate:

- Notion workspace connection
- content task database id/reference
- browser profile path
- enabled platforms

## Separation of Concerns

### Skill
Defines business rules, required fields, and validation logic.

### MCP
Provides authenticated access to Notion and other external services.

### Config
Stores user-specific ids and runtime parameters outside the repository.

## Required Notion fields

- Status
- Human Approval Status
- Automation Status
- Content Images
- Platform Copy
- Platforms
- Publish Instruction
- Publishing Record

## Validation result

A successful setup should confirm:

- database accessible
- required fields found
- browser runtime available
- browser login state usable
- scheduler ready

## Safety

During setup:

- do not publish
- do not create drafts
- do not modify user content
- do not change approval state
