# yuguang-operations

余光所及 AI 内容运营自动化体系。

## Hermes skill namespace

All user-facing Hermes skills in this repository use the project-specific prefix `yg-` to avoid collisions with generic or third-party skills.

Current skills:

- `yg-setup`
- `yg-notion-content-operation`
- `yg-publish-orchestrator`
- `yg-content-operation-scheduler`
- `yg-xiaohongshu-publisher`
- `yg-douyin-publisher`
- `yg-wechat-mp-publisher`

### Natural conversation is the default

Users do **not** need to explicitly call these skills by name.

Hermes should infer the appropriate Yu Guang skill from natural-language intent. For example:

- “检查一下余光的运行环境” -> `yg-setup`
- “看看 07 里有哪些待发布内容” -> `yg-notion-content-operation`
- “把这条内容存到对应平台草稿箱” -> `yg-publish-orchestrator`
- “每小时巡检一次待执行任务” -> `yg-content-operation-scheduler`
- “把这条存到小红书草稿箱” -> `yg-xiaohongshu-publisher`
- “把这条存到抖音草稿箱” -> `yg-douyin-publisher`
- “把这篇放到公众号草稿箱” -> `yg-wechat-mp-publisher`

Explicit slash invocation remains available for troubleshooting and deterministic manual runs.

## Architecture

```
ChatGPT / 创作 Agent
        |
        v
Notion 内容资产系统
        |
        v
Hermes Operations Agent
        |
        +--> yg-notion-content-operation
        |
        +--> yg-publish-orchestrator
                    |
                    +--> yg-xiaohongshu-publisher
                    +--> yg-douyin-publisher
                    +--> yg-wechat-mp-publisher
                              |
                              v
                        browser-use runtime
                              |
                              v
                 小红书 / 抖音 / 微信草稿箱
```

## Principles

- Notion is the single source of truth for approved publishing assets.
- Human approval is the quality gate.
- Hermes executes operations, not creative decisions.
- Natural-language routing is preferred over explicit skill invocation.
- Browser automation creates drafts by default; public publishing requires separate explicit approval.

## Dependencies

Browser automation is provided by browser-use:
https://github.com/browser-use/browser-use

This repository stores Yu Guang business skills and platform rules, not the browser engine itself.
