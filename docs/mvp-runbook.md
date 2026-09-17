# 余光所及 Hermes MVP Runbook

## Goal

完成：

Notion 07 内容任务 -> Hermes -> browser-use -> 平台草稿箱

## Runtime Flow

1. Scheduler triggers Hermes.
2. Notion MCP Adapter queries pending tasks.
3. Publish Orchestrator creates platform tasks.
4. Browser Runner invokes browser-use.
5. Platform Adapter executes browser workflow.
6. Notion Writer updates execution status.

## Required configuration

- Notion MCP connection
- 07 database id
- browser-use installation
- Chrome profile with logged-in accounts

## Safety

Default behavior:

- create drafts only
- no automatic public publishing
- preserve human approval gate

## First test

Create one test item in 07:

Automation Status = 待执行

Then run Hermes once and verify:

- browser opens platform
- draft is created
- Notion receives execution result
