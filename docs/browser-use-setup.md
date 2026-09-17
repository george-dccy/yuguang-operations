# Browser Use Integration

## Purpose

browser-use is the browser execution layer.

Yu Guang Operations does not implement browser control itself.

## Responsibility Split

Hermes:
- schedule
- read Notion
- create PublishTask

Yu Guang Skills:
- define business workflow
- define platform rules

browser-use:
- open browser
- click
- type
- upload files
- save drafts

## Recommended Runtime

Install browser-use in Hermes environment:

```bash
pip install browser-use
```

Use a persistent Chrome profile to keep platform login sessions.

## Safety

Default mode:

Create drafts only.

Human confirmation is required before public publishing.
