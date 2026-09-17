# PublishTask Schema

The internal contract between Notion Content Operation and platform adapters.

```yaml
id: notion_page_id
platform: xiaohongshu
images:
  - file_url

title: string
body: string
tags:
  - string

publish_instruction: string
```

## Source Mapping

| PublishTask | Notion field |
|---|---|
| images | Content Images |
| title/body/tags | Platform Copy |
| platform | Platforms |
| instruction | Publish Instruction |

## Validation

Required:

- approved images
- platform copy
- target platform
- human approval
