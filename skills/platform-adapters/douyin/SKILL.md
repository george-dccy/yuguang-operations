# Douyin Platform Adapter

## Purpose

Create Douyin draft content from approved Notion publish tasks.

## Input

- Content Images
- Video assets if available
- Title
- Body
- Tags

## Rules

- Only process Automation Status = 待执行.
- Only use approved assets from 07 content task database.
- Default behavior is save draft only.
- Never publish automatically.

## Browser Flow

1. Open creator platform.
2. Create image/video post.
3. Upload approved assets.
4. Fill copy.
5. Save draft.
6. Return execution result.
