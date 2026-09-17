# Xiaohongshu Adapter Notes

This file stores platform-specific interaction notes.

## Principle

Prefer semantic browser-use interaction over brittle selectors.

Avoid hard-coded DOM assumptions whenever possible.

## Elements To Resolve

- Creator center entry
- Image post creation entry
- Upload component
- Title input
- Body editor
- Tag input
- Save draft action

## Maintenance

When platform UI changes:

1. Update this file.
2. Test draft creation manually.
3. Update browser-use instructions if required.

## No Auto Publish

The adapter must only save drafts unless explicit user approval is provided.
