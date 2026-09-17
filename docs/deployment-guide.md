# Deployment Guide

## Architecture

```
Hermes Agent
    |
    +-- yuguang-operations skills
    |
    +-- Notion MCP
    |
    +-- browser-use runtime
```

## Installation Order

1. Install Hermes Agent environment
2. Install yuguang-operations skills
3. Install browser-use runtime
4. Configure Notion MCP
5. Configure runtime settings
6. Start scheduler

## Notion MCP Setup

The repository does not contain user credentials.

After installation, connect the user's Notion account through MCP and configure:

- workspace access
- 07 content task database
- required property mapping

## Runtime Configuration

User-specific configuration belongs in local config files, not the repository.

Examples:

- database ids
- browser profile paths
- enabled platforms

## First Validation

Before enabling automation:

1. Confirm Notion can read 07 content tasks.
2. Confirm browser-use can open the configured browser profile.
3. Confirm a test task can generate a PublishTask.
4. Confirm draft creation works without final publishing.

## Production Safety

Default mode:

- create drafts only
- require human final approval
- write execution results back to Notion
