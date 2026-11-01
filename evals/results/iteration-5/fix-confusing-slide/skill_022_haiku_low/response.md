Biggest problem: the slide has two competing messages (a market share pie and a dual-axis chart) and the chart's own numbers hide the point that reps grew while revenue did not.

Problems found in bad_slide.py / bad_slide.png:

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Context | Title "Market Overview 2025" names no takeaway, and the slide mixes two unrelated questions | The director cannot tell what to conclude | Action title: "Sales reps grew 25% in 2025, but revenue grew only 1%" |
| Visual | Pie chart for market share | Angles are hard to compare; the pie also has no clear link to the reps story | Removed from this slide (see assumptions) |
| Visual | Dual y-axis: revenue bars against reps line on a second axis | The crossing lines are arbitrary; the scale choice decides whether revenue looks like it rose or fell | Two stacked panels sharing the x-axis, both zero-based bars |
| Visual | Bar axis starts at 4.0 | Makes $4.1M vs $4.6M look like a 4x difference | Bars start at zero; differences are labeled, not exaggerated |
| Clutter | Gridlines, legend boxes, rainbow bar colors, 3D import, shadows, exploded slices | Decoration competes with the data; eight colors carry no meaning | Grey for reps, one blue accent for revenue, direct value labels, no gridlines or legends |
| Focus | Every element has equal weight; red, orange, yellow and green all compete | The eye has no entry point | Revenue in accent blue as the outcome that is not moving; reps in grey as context |
| Design | No source, no units on reps, no ask | Not usable in a QBR without a follow-up question | Footnote with annual totals and placeholder source; takeaway line with the ask |

Redesign: two stacked zero-based bar panels on a shared quarterly x-axis. Top: sales reps (grey, labeled 38 to 55). Bottom: revenue in $M (blue, labeled $4.1M to $4.2M). Action title in the top left. Bottom line: revenue per rep fell 19% (about $0.42M to $0.34M per rep per year) and the ask is to hold further rep hiring until productivity is reviewed. The eye lands on the flat blue bars against the rising grey bars.

Numbers checked against the input series:
- Annual revenue: 2024 = $17.2M, 2025 = $17.4M, growth +1.2%, shown as "1%".
- Average quarter-end reps: 2024 = 40.75, 2025 = 51.0, growth +25.2%, shown as "25%".
- Revenue per average rep: 2024 = $0.42M, 2025 = $0.34M, change -19%.

Assumptions (please confirm):
- Revenue is our company's revenue per quarter in $M, and reps are quarter-end headcount.
- The ask is to hold new rep hiring until productivity is reviewed. Replace it if the decision is different.
- The market share pie was dropped because it answers a different question. It belongs on its own slide if the director wants it kept.
- The source is a placeholder, "[insert source]".
- Average headcount is used for per-rep figures, since reps change during the year.

Files:
- Fixed PNG: <workspace>/iteration-5/fix-confusing-slide/skill_022_haiku_low/outputs/fixed_slide.png
- Fixed script: <workspace>/iteration-5/fix-confusing-slide/skill_022_haiku_low/outputs/fixed_slide.py
