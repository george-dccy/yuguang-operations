# Notion MCP Initialization Checklist

## Purpose

This document defines the first-run configuration process after installing yuguang-operations skills.

The skill package does not contain user credentials or workspace information. Notion access is provided by the user's configured MCP connection.

## First Run

1. Enable the Notion MCP server in the Hermes environment.
2. Authenticate the user's Notion account.
3. Verify access to the required databases.
4. Store local configuration references.

## Required Database

Primary database:

- 07｜内容任务与发布包库

Required fields:

- Status
- Human Approval Status
- Automation Status
- Content Images
- Platform Copy
- Platforms
- Publish Instruction
- Publishing Record

## Validation

A successful setup should be able to:

- query pending automation tasks;
- read attached content images;
- read platform copy;
- prepare a PublishTask object.
