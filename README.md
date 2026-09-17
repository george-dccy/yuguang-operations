# yuguang-operations

余光所及 AI 内容运营自动化体系。

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
        +--> Notion Content Operation Skill
        |
        +--> Publisher Skills
                    |
                    v
              browser-use runtime
                    |
                    v
       小红书 / 抖音 / 微信草稿箱
```

## Principles

- Notion is the single source of truth.
- Human approval is the quality gate.
- Hermes executes operations, not creative decisions.
- Browser automation only creates drafts by default; publishing requires explicit approval.

## Dependencies

Browser automation is provided by browser-use:
https://github.com/browser-use/browser-use

This repository stores business skills and platform rules, not the browser engine itself.
