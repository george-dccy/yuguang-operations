# Yu Guang PublishTask Schema

Internal contract between `yg-notion-content-operation`, `yg-publish-orchestrator`, and the Yu Guang platform publisher skills.

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
| title/body/tags | Platform Copy or approved platform section in page body |
| platform | Platforms |
| instruction | Publish Instruction |

## Validation

Required:

- approved images
- approved platform copy
- target platform
- Human Approval Status = 已认可
