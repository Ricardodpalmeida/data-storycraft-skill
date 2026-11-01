Audience:  Sales leadership at the quarterly business review
Ask:       Decide whether to keep adding reps before revenue per rep is understood
Mechanism: Live presentation (the slide is also readable as a sent document)
Big Idea:  Adding 17 reps (+45%) since Q1 24 has not grown quarterly revenue (+2%), so net rep hiring should freeze until revenue per rep is reviewed.
Check:     Revenue Q1 24 to Q4 25 is +2.4% at the quarter endpoints and +1.2% full year (17.2 to 17.4 $M). Reps 38 to 55 is +44.7%. Revenue per rep is $108K to $76K a quarter (-29%). Market share sums to 100%, so no mismatch. Mismatch: the data ends Q4 25 while today is Nov 2026, so confirm the period before presenting.

Biggest problem: The slide uses a pie chart and a dual-axis bar and line chart with a truncated axis, so the eye cannot find the one point (reps up, revenue flat) and the title names no takeaway.

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Visual | Pie chart for market share | Angles are hard to compare, and the pie does not support the rep-versus-revenue message | Removed; if the share matters, it becomes its own sorted bar slide |
| Visual | Bars for revenue, line for reps on a secondary y-axis | Two scales let the reader draw any shape they like; the bars are also on a 4.0 to 4.7 axis, which exaggerates small swings | Two stacked panels sharing the x-axis, each on its own honest axis; both start at zero |
| Clutter | Shadow, exploded slices, dashed gridlines, legends in boxes, 45 degree labels, unused 3D import | Each element competes for attention and none carries the message | All removed; each series labelled directly |
| Focus | Rainbow colors with no meaning (eight bar colors, four pie colors) | Nothing stands out, so the eye lands nowhere | One accent (blue) for reps, the decision under review; revenue in dark grey |
| Design | Title "Market Overview 2025", centered and with no takeaway | Viewer must work out the point themselves | Action title with the takeaway and the event: "Adding 17 sales reps (+45%) since Q1 24 has not grown revenue (+2%)" |
| Story | No call to action on the slide | The slide ends without telling leadership what to decide | Slide text block ends with the ask |

Redesign: Two stacked line panels sharing the quarter axis. Top: sales reps in accent blue, labelled 38 and 55. Bottom: quarterly revenue in dark grey on a zero-based axis, labelled $4.1M and $4.2M. Title, left-aligned, names the event. Below the chart, one line on revenue per rep ($108K to $76K a quarter), then the ask in bold. Footnote with source and the revenue-per-rep definition. Spec and code: <workspace>/iteration-6/fix-confusing-slide/skill_023_haiku_low/outputs/bad_slide_fixed.py

Where the eye lands first: the blue line climbing in the top panel, then the flat dark line below it, because it is the only colored element and the title names both.

Assumptions I made:
- The numbers are quarterly revenue and quarter-end rep headcount.
- The ask is a freeze on net new rep hiring plus a revenue-per-rep review. The data does not say what leadership should decide, so change the ask if the real decision differs.
- The market share data was dropped from this slide because it does not support the rep point. It needs its own slide if the director wants it.
- The data runs to Q4 25 and today is Nov 2026, so check that the QBR is using the right period.

Files:
- Fixed PNG: <workspace>/iteration-6/fix-confusing-slide/skill_023_haiku_low/outputs/bad_slide_fixed.png
- Fixed script: <workspace>/iteration-6/fix-confusing-slide/skill_023_haiku_low/outputs/bad_slide_fixed.py
