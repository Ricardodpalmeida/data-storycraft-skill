# Notes: skill files read, in order

1. <skill>/SKILL.md (read in full)
2. <skill>/reference/model-visuals.md (read; used for the slopegraph and emphasis choices, otherwise the default from SKILL.md's visual table)
3. dataviz skill, loaded via the Skill tool from /tmp/claude-0/bundled-skills/2.1.316/075642f6476c8d5a8ac5673a829e8dad/dataviz/SKILL.md (body read; the reference files it lists were not opened)

Also executed (not read): /tmp/claude-0/bundled-skills/2.1.316/075642f6476c8d5a8ac5673a829e8dad/dataviz/scripts/validate_palette.js, run on the two-colour palette #A6A6A6 and #D55E00 in light mode. Result: lightness band and CVD and normal-vision separation passed; chroma floor failed for the neutral grey (expected for a context colour); contrast warned for the grey, handled by direct labels.

Input read: <workspace>/inputs/engagement_survey.csv (read-only).
