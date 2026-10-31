**Context**

```
Audience:  Leadership team
Ask:       Treat Career growth as the priority theme for 2026 action
Mechanism: Both (sent document and live discussion)
Big Idea:  Career growth fell 15 points to 51% favourable while every other theme rose,
           so it needs a leadership response now.
```

Assumptions made: the figures are % favourable per theme for each year, as given in the CSV; the chart compares the two years only, with no response counts or significance tests, since the file has none; the audience is the leadership team, so the chart carries a single message rather than a full breakdown.

**Chart:** `<workspace>/04-engagement-survey/with_skill_haiku/chart.png` (1600 x 960 px)

It is a slopegraph, the default for change between two points across categories. Every theme is a grey line, labelled directly at both ends with its value, and Career growth is the single orange line (orange as the negative accent). The eye lands first on the orange line falling from 66% to 51%. The action title states the takeaway, and the source is in a small grey footnote.

What the data shows: Career growth is the only theme that dropped (66% to 51%, down 15 points). Tools rose the most among the rest (63% to 68%, up 5), Recognition rose 4 points, Pay and Workload rose 3 each, and Manager, Team and Mission rose 2 each. Career growth is now the lowest-scoring theme in 2026, below Workload (55%).

Script: `<workspace>/04-engagement-survey/with_skill_haiku/make_chart.py`

Notes: the neutral grey lines fall below the chroma threshold on the palette validator and sit at low contrast against the background. That is expected for context lines; the labels carry identity and are set in dark grey, so the chart does not rely on the lines alone.
