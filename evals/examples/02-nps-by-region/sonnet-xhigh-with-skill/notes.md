# Skill files read, in order

1. <skill>/SKILL.md, read first as instructed. It gave the workflow, the context block, the chart defaults, the rules and the final check.
2. <skill>/reference/context.md, opened because the request was vague on audience and ask, so I needed the Big Idea guidance.
3. <skill>/reference/model-visuals.md, opened to look for a line chart recipe. Its line recipes (progress vs goal, actual vs forecast) did not fit, so I only took the typography guidance.
4. <skill>/reference/focusing-attention.md, opened for the color decisions (grey base, one accent, colorblind safety) and the eyes-drawn test.
5. <skill>/reference/case-studies.md, opened for the tangled line chart strategies. It confirmed one highlighted line with the rest in grey, since full context matters here.
6. <skill>/reference/designing.md, opened for the accessibility and emphasis guidance (bold plus color, plain words, spelling out NPS).

No other skill files were opened. The folder listing showed decluttering.md, choosing-visuals.md, storytelling.md, worked-example.md and practice-and-teams.md, and I left them unread because SKILL.md already covered the decluttering and chart choice a single line chart needs, and this is one chart, not a deck.

# Other reads and writes

- Input read: <workspace>/inputs/nps_by_region.csv (12 months, 7 regions, no missing values).
- A directory listing of the parent folder showed the file names inside a sibling without_skill folder. I did not open any of those files.
- Written only to <workspace>/02-nps-by-region/with_skill/: chart.png, make_chart.py, response.md, notes.md.

# Assumptions made

- Audience, ask and mechanism were inferred, since the request named only a quarterly business review.
- The data runs to December 2026 while today is 31 October 2026, so November and December were plotted as supplied and flagged in the response.
- Orange was used as the accent because the message is negative news, per the skill.
- The y-axis starts at 20 (line chart), disclosed in the chart footnote.

# Checks run in the script

- Nordics peak is March at 46, the December value is 24, and the drop is 22.
- Nordics falls in every month after March (asserted).
- Every other region stays within 3.0 points of its January value (asserted).
- Output image size verified as 1600 x 960 pixels.
