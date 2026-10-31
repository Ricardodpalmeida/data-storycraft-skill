# Engagement survey: 2025 vs 2026 by theme

The chart is saved at `<workspace>/04-engagement-survey/without_skill_haiku/chart.png` (1600 x 960 px). The script that builds it is `<workspace>/04-engagement-survey/without_skill_haiku/make_chart.py`.

**Key finding:** Career growth is the only theme that fell. It dropped 15 points, from 66% to 51% favourable, and is now the lowest-scoring theme in the survey (Workload is at 55%). The other seven themes rose by 2 to 5 points. Team (80%) and Mission (76%) remain the strongest.

| Theme | 2025 | 2026 | Change (pts) |
|---|---|---|---|
| Career growth | 66 | 51 | -15 |
| Manager | 71 | 73 | +2 |
| Mission | 74 | 76 | +2 |
| Team | 78 | 80 | +2 |
| Workload | 52 | 55 | +3 |
| Pay | 58 | 61 | +3 |
| Recognition | 55 | 59 | +4 |
| Tools | 63 | 68 | +5 |

**Chart design:** a dumbbell chart, one row per theme, with grey dots for 2025 and navy dots for 2026. Career growth is highlighted in red and sorted to the top so the decline is the first thing a reader sees. Each row shows the point change on the right.

**Assumptions:**
- Values are % favourable as given in the CSV. Changes are in percentage points, not percent change.
- Both years cover the same eight themes, and the survey base (response rates, population) is comparable across years. The file does not say, so this is unverified.
- No significance testing was possible, since the file has no sample sizes. Small moves such as +2 may be within normal survey noise. Only the 15-point drop in Career growth is large enough to treat as a clear signal without further data.
- "For the leadership team" was read as a presentation for leaders, so the headline states the finding instead of only describing the data.
