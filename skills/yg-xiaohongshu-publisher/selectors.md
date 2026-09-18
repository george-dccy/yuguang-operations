# Yu Guang Xiaohongshu Interaction Notes

Supports `yg-xiaohongshu-publisher`.

Prefer semantic browser-use interaction over brittle CSS/XPath selectors.

Resolve controls by visible meaning whenever possible:

- creator center entry
- 图文 / image-post creation entry
- upload component
- title input
- body editor
- tag/topic input
- 保存草稿 action

When platform UI changes:

1. stop if draft vs publish controls are ambiguous
2. update these notes with newly observed wording
3. manually validate one draft before restoring automation

Never use a final-publication control as a fallback for draft saving.
