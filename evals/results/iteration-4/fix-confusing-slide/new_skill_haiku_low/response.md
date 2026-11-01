**Biggest problem:** the slide shows three things at once (market share, revenue, and reps) on two unrelated visuals, and the one comparison that matters (reps vs revenue) is a dual-axis line over bars whose y-axis starts at 4.0, so the eye cannot see that revenue is flat while reps climb.

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Context | Title "Market Overview 2025" with no takeaway, no audience ask | Leadership cannot tell what to conclude | Action title: "Adding 11 sales reps in 2025 (+25%) grew revenue only 1%", plus an explicit ask |
| Visual | Pie chart for market share | Angles are hard to compare; pie is off-message here | Removed |
| Visual | Revenue bars with y-axis starting at 4.0 | Truncated bars exaggerate differences (4.1 vs 4.6 looks like a huge gap) | Revenue as a line in its own panel; reps as bars from zero |
| Visual | Dual y-axis (revenue and reps) | Lines and bars on two scales invent a visual relationship | Two stacked panels sharing the x-axis |
| Clutter | Rainbow colors with no meaning, 3D import, shadows, explode, gridlines, rotated labels, two legends | Colors carry no information and compete with the message | One accent (blue) for revenue, grey for context, no gridlines or legends |
| Focus | Everything the same weight | Nothing draws the eye | Accent on the revenue line and its two totals; reps in grey with values labelled |
| Design | Text centred, legends overlapping the data | Hard to scan | Left-aligned title, subtitle and panel titles; direct labels |
| Story | No beginning, middle or end | No call to action | Title states the finding; bottom line states the ask |

**Redesign:** a two-panel slide sharing the quarterly x-axis. Top: revenue line in blue with the 2024 total ($17.2M) and 2025 total ($17.4M, +1%) annotated. Bottom: sales reps as grey bars from zero, with the Q4 24 to Q4 25 change (+11, +25%) annotated. Action title and ask sit above and below the chart, with a source footnote.

Files:
- Fixed PNG: <workspace>/iteration-4/fix-confusing-slide/new_skill_haiku_low/outputs/fixed_slide.png
- Fixed script: <workspace>/iteration-4/fix-confusing-slide/new_skill_haiku_low/outputs/fixed_bad_slide.py

Where the eye lands first: the blue revenue line in the top panel, which stays nearly flat from 2024 to 2025 while the grey rep bars climb below it.

Assumptions to check before the QBR:
- The ask ("hold the next rep hiring wave until we know why new reps are not converting") is my guess. Replace it with the real decision.
- I used full-year totals for revenue and Q4 to Q4 for headcount. Confirm that reps are quarter-end counts.
- The market share pie is gone. If sales leadership needs share, put it on a separate slide.
- The source footnote is a placeholder.
