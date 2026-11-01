# Notes: fix confusing slide (old_skill_haiku_low)

## Skill files read, in order

1. <skill-v0.2.0>/SKILL.md
2. <skill-v0.2.0>/reference/worked-example.md
3. <skill-v0.2.0>/reference/choosing-visuals.md
4. dataviz skill (loaded via the Skill tool; base directory /tmp/claude-0/bundled-skills/2.1.316/ecf1f0638e419be4b21d712083816191/dataviz), SKILL.md only

Not read: the other data-storycraft references, and the dataviz references and scripts. Skill files were not modified.

## Inputs read
- <workspace>/inputs/bad_slide.py
- <workspace>/inputs/bad_slide.png

## Assumptions
- Audience: sales leadership at the QBR. Mechanism: live presentation with a sent copy.
- Big Idea: adding reps has not grown revenue. Reps went from 38 to 55 (+45%) and revenue from $4.1M to $4.2M (+2%), Q1 2024 to Q4 2025.
- Ask (not on the slide, to confirm with the director): decide whether to keep adding reps until revenue per rep is understood.
- Market share pie (Supplier A to D, Us at 20%) was dropped because it does not support the reps-vs-revenue message. It can go to an appendix if the director wants it.
- Source line is generic ("quarterly sales headcount and revenue"). Replace it with the real source.
- Quarter labels were kept as in the original data.
- Revenue axis runs $0M to $5M so that the flatness is shown honestly. The original's truncated 4.0 to 4.7 axis exaggerated the swings.

## Problems found in the original
- Pie chart for shares, with exploded slices, shadow and a rainbow of colors, which is hard to compare.
- Dual y-axes: revenue bars and reps line on different scales, so the visual crossing suggests a relationship that the scales create.
- Bar chart with a truncated y-axis (4.0 to 4.7), which exaggerates small differences.
- Eight different bar colors with no meaning; the accent logic is absent.
- Two legends that repeat the series names, plus gridlines and a boxed layout.
- Title "Market Overview 2025" is a topic, not an action title, and does not match the quarter range (Q1 2024 to Q4 2025).
- Unused 3D import.
- Pie, dual axis and the 3D import are code-level clutter; the script also saved to a relative path.

## Fix applied
- Two stacked panels sharing one x-axis (allowed by the skill as the alternative to a secondary axis): reps as grey bars starting at zero, revenue as a single blue line on a zero-based axis.
- Action title, subtitle with the numbers, direct value labels on endpoints only, source footnote.
- Colors: grey for context, one blue accent for the revenue line.

## Dataviz validator
Not run. The fixed chart uses one neutral grey and one accent blue, with no categorical palette, so there is no categorical palette to validate.
