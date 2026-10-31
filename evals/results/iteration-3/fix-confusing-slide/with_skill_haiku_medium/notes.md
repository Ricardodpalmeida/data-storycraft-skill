# Notes: fix-confusing-slide (with_skill_haiku_medium)

## Skill files read, in order

1. <skill>/SKILL.md
2. <skill>/reference/context.md
3. <skill>/reference/choosing-visuals.md
4. <skill>/reference/decluttering.md
5. <skill>/reference/focusing-attention.md

Reference files not opened: designing.md, model-visuals.md, storytelling.md, worked-example.md, case-studies.md, practice-and-teams.md (not needed for a single-slide fix). The skill was not modified.

## Other inputs read

- <workspace>/inputs/bad_slide.py
- <workspace>/inputs/bad_slide.png (viewed)
- <workspace>/inputs/churn_by_plan.csv (used only for the backup question on churn)
- <workspace>/inputs/pilot_findings.md (read, judged unrelated, not used)

## Outputs

- fixed_slide.py: rebuilt chart script, writes fixed_slide.png next to itself
- fixed_slide.png: 1650x975 px at 150 dpi
- response.md: final reply to the user

## Checks run

- Script ran without error and the PNG was viewed after two renders. The first render showed a mathtext rendering bug in the subtitle caused by two unescaped dollar signs; fixed with escaped dollar signs.
- Arithmetic checked: 55 / 38 - 1 = 44.7% (shown as 45%); 4.2 / 4.1 - 1 = 2.4%; 17 = 55 - 38; revenue per rep 4.1 / 38 = $108K, 4.2 / 55 = $76K (-29%); Pro active customers 1,512 / 1,950 - 1 = -22.5%.
- Style: no em dashes, no emoji, no "trying" in the deliverables.
