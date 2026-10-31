# Fixed slide: reps vs revenue

Context

```
Audience:  Sales leadership, quarterly business review
Ask:       Review revenue per rep before approving more hires (assumed; the brief did not state one)
Mechanism: Live presentation (one slide in the QBR deck)
Big Idea:  Adding 17 sales reps since Q1 2024 has not grown revenue, so approve further hiring only after we review what each rep produces.
```

**Biggest problem:** the slide tells two unrelated stories on one canvas, and the chart that carries the real message puts revenue and reps on two y-axes, with the revenue bars cut off at $4.0M.

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Context | Title "Market Overview 2025" is a topic label. The slide mixes a market-share snapshot with revenue vs reps. No ask. The data runs Q1 2024 to Q4 2025, so "2025" is wrong. | Leadership cannot see the point in the first seconds. | Action title on the reps-revenue point. Market share removed: it has no time period and does not support the message. |
| Visual | Pie chart of five suppliers, where 11% vs 14% is hard to compare. Revenue bars and reps line share one chart on two y-axes. | Pies are read by angle, not length. Two y-axes let the line look like it climbs to meet the bars, which implies a link the data does not show. | Pie removed. Two stacked line panels on one quarter axis, each starting at zero. |
| Clutter | Unused 3D import, pie shadow and explode, dashed gridlines, rotated labels, boxed legends that repeat the titles. | Each element competes with the message. | All removed. Gridlines off, labels horizontal, panel titles replace legends. |
| Focus | Seven saturated colors (red, orange, yellow, green, purple, blue, pink) on bars that encode nothing. | Nothing is emphasized, so the eye goes to the purple and orange, not to the gap between reps and revenue. | Reps in grey, revenue in one blue accent. |
| Design | Centered title. Revenue axis starts at $4.0M. Reps line runs off the top at Q4 25. | Truncation makes a 12% gap look six-fold. The clipped endpoint hides the final value. | Both axes start at zero. Endpoints labelled. Large callouts on the right. |
| Story | No sentence says what to conclude or decide. | Leadership must infer the point from two charts. | The title states the point, the callouts give +45% and +2%, and the subtitle sets the period. |

**Redesign:** two stacked line panels on one shared quarter axis. The top panel shows sales reps as a grey line from 38 to 55. The bottom panel shows revenue as the blue line from $4.1M to $4.2M, the only saturated color on the slide. Both start at zero. The right column shows +45% for reps and +2% for revenue, each under "Change since Q1 2024". The title reads "Adding 17 sales reps since Q1 2024 has not grown revenue", with a source footnote.

The eye lands first on the title, then the blue +2%, because the title is top left and blue is the only accent.

Files:

- PNG: evals-workspace/iteration-3/fix-confusing-slide/with_skill_haiku/outputs/fixed_slide.png
- Script: evals-workspace/iteration-3/fix-confusing-slide/with_skill_haiku/outputs/fixed_slide.py

**Assumptions to confirm**

1. The ask is a productivity review before more hires. Check this with the director.
2. Headcount is sales reps per quarter. The input does not say whether that is an end-of-quarter count.
3. The footnote says "internal" data. Replace it with the source system's name if the director wants one.
4. The market share pie is off this slide. It needs its own slide if the director wants it.

**Questions the director may ask**

- Revenue peaked in Q4 24 at $4.6M, and Q4 25 at $4.2M is about 9% lower. That supports the point but may raise a seasonality question.
- Full year: 2025 revenue was $17.4M against $17.2M in 2024 (+1%), while average reps rose from 40.75 to 51 (+25%).
- Revenue per rep fell from about $108K a quarter in Q1 24 to about $76K in Q4 25, roughly 30% lower. It is left off the slide to keep one message. It would make a strong next slide or speaker line.
