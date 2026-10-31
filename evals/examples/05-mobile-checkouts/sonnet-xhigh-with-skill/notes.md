# Skill files read, in order

1. `<skill>/SKILL.md`, read first as instructed. It supplied the context block, the visual defaults, the declutter, focus and design steps, the rules, the output format and the matplotlib starting point.
2. `<skill>/reference/choosing-visuals.md`, opened because the data is only two points and the SKILL.md table does not cover that case directly. It confirmed the line default, the "label points directly and drop the axis when exact values matter, never both" rule, and the warning that collapsing two numbers into one derived figure can hide useful magnitudes (so both 41% and 68% are shown, with the +27 points as support).
3. `<skill>/reference/model-visuals.md`, opened for the line-chart recipes (accent series with markers and value labels on the referenced points, thin grey reference line with a grey label, dark grey title).

No other skill files were opened.

# Other file read

`<workspace>/inputs/mobile_checkouts.csv` (two rows: 2024 = 41, 2026 = 68).

# Files written

All in `<workspace>/05-mobile-checkouts/with_skill/`: `make_chart.py`, `chart.png`, `response.md`, `notes.md`.
