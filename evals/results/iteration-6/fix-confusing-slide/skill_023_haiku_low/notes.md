# Notes

## Skill files read, in order

1. <skill>/SKILL.md
2. <skill>/reference/case-studies.md
3. <skill>/reference/model-visuals.md

The skill was not modified.

## Other inputs read

- <workspace>/inputs/bad_slide.py
- <workspace>/inputs/bad_slide.png

## Process

- Read SKILL.md first, then opened case-studies.md (for the dual-axis and pie replacement guidance) and model-visuals.md (for the zero-based, direct-label line recipe).
- Rendered the fixed chart, found two problems (a mathtext parse of the dollar signs and crowded revenue ticks), fixed them, and re-rendered and checked the PNG.
- Numbers recomputed from the input arrays before writing the title (see Check line in response.md).
