# Yu Guang Publish Error Handling

Supports `yg-publish-orchestrator`.

## Principles

Publishing automation must fail safely.

Never publish partial, uncertain, or unapproved content.

## Missing images

- stop execution
- report missing Content Images
- do not proceed to platform workflow

## Browser failure

- capture the error
- retry only according to Yu Guang retry policy
- mark execution failure if unresolved

## Login expired

- stop
- request manual browser authentication
- do not attempt password or 2FA recovery

## Draft creation failure

- preserve content and approval state
- record error details
- allow later retry
- never click final publish as a fallback

## Notion recording

Write:

- execution status
- timestamp
- platform
- error message or draft confirmation
