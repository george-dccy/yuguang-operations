# Yu Guang Platform Publishers

The public Hermes publisher skills are top-level project-specific skills so they are easy to discover and do not collide with generic skills:

- `yg-xiaohongshu-publisher`
- `yg-douyin-publisher`
- `yg-wechat-mp-publisher`

This `platform-adapters` directory is retained only as architecture documentation; it is not itself a user-facing skill.

## Invocation policy

Natural-language intent is the default. Users can simply say:

- “存到小红书草稿箱”
- “做一条抖音草稿”
- “放到公众号草稿箱”

Hermes should route the request to the matching `yg-*` publisher automatically.

## Common rules

- Use browser-use as the execution engine.
- Preserve the user's authenticated browser session.
- Use only human-approved assets from Notion 07.
- Save drafts by default.
- Do not publicly publish without separate explicit authorization.
