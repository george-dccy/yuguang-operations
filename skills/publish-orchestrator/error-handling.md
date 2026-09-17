# Publish Error Handling

## Principles

Publishing automation must fail safely.

Never publish partial or uncertain content.

## Common Errors

### Missing images

Action:

- stop execution
- report missing Content Images
- keep Automation Status unchanged

### Browser failure

Action:

- capture error
- retry according to platform adapter policy
- mark execution failure if unresolved

### Login expired

Action:

- stop
- request manual browser authentication
- do not attempt credential recovery

### Draft creation failure

Action:

- preserve task state
- record error details
- allow later retry

## Notion Recording

Write:

- execution status
- timestamp
- error message
