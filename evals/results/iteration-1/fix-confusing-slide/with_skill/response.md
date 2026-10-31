Your director is right. The biggest problem is that the slide has no message: it puts two unrelated charts under a topic title ("Market Overview 2025"), and the one comparison that matters, reps vs revenue, is drawn in a way that hides your point.

## What was wrong

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Context | Topic title, no ask, a market share pie that has nothing to do with reps and revenue. The title says 2025 but the data runs Q1 2024 to Q4 2025. | Sales leadership has to work out the point themselves, and half the slide argues something else. | One slide, one message. The title states the finding and the subtitle states the ask. The pie is gone. |
| Visual | 3D-style pie with shadow and exploded slices. Revenue bars plus a reps line on a secondary y-axis. The bar axis starts at 4.0. | Pie slices are hard to compare. The two axes are aligned arbitrarily, so the line appears to track the bars, which is the opposite of your point. Starting bars at 4.0 makes $4.1M vs $4.6M look like a 6x gap. | Two line panels that share the x-axis, one for reps and one for revenue, both starting at zero. No secondary axis. |
| Clutter | Dashed gridlines, a different rainbow color per bar, two legends, 45 degree labels, shadows, and the 55-rep point clipped at the top edge. | Every element costs attention, and the bar colors carry no meaning. | All removed. Hairline gridlines only, horizontal labels, direct labels on the first, peak and last points. |
| Focus | A dozen or more colors, red and green side by side, nothing stands out. | The eye has nowhere to land, and red/green fails for colorblind viewers. | Reps in dark grey, revenue in one orange accent, one large number. The accent is validated for colorblind separation and contrast. |
| Design | Centered generic titles, rotated axis titles, no takeaway in words, no source. | Rotated text is slow to read and the audience has to infer the conclusion. | Left-aligned action title, horizontal axis titles, takeaway in words, source footnote, 16:9 for a slide. |
| Story | No tension, no resolution, no call to action. | A QBR slide should end with something to decide. | The title is the finding, the subtitle is the ask, and the big number is the so-what. |

## What the new slide says

Reps are up 45% since Q1 2024 (38 to 55), but quarterly revenue is up only 2% ($4.1M to $4.2M). That means revenue per rep fell 29%, from $108K to $76K a quarter. The subtitle asks leadership to understand why before hiring more.

I read the brief as: audience is sales leadership at the QBR, shown live; the point is that adding reps has not grown revenue. The eye lands on the title first, then the large -29%, then the orange revenue line sitting flat under the rising reps line. Every number on the slide is computed from your data in the script, so the title and annotations cannot drift from the chart.

## Assumptions to check

- Revenue is quarterly and the rep counts are net headcount for each quarter. If "reps" means quota-carrying reps only, or revenue is cumulative, the wording needs a tweak.
- The ask ("before we hire more, understand why") is my inference from your point. If you want something harder, such as pausing hiring, or softer, change the `ASK` line at the top of the script.
- The source line says "internal sales and headcount data". Replace it with the real system name.
- I cut the market share pie because it does not support this message. If leadership needs it, it belongs on its own slide as a sorted horizontal bar with "Us" highlighted. I can build that if you want it.

## Two questions to expect in the room

Someone will say new reps need ramp time. The data cannot rule that out, but the Q1 2024 additions have had well over a year. Someone may also point at 2024, when reps grew 16% and revenue grew 12%. The Q4 24 peak could be seasonal, so the like-for-like check is Q4 25 against Q4 24: reps up 25%, revenue down 9%, revenue per rep down 27%. Year on year, reps were up about 25% in every quarter of 2025 while revenue growth slid from +7% in Q1 to -9% in Q4. The conclusion holds either way.

## Files

- evals-workspace/iteration-1/fix-confusing-slide/with_skill/outputs/fixed_slide.png (2000 x 1125 px)
- evals-workspace/iteration-1/fix-confusing-slide/with_skill/outputs/fixed_slide.py (writes the PNG next to itself)
