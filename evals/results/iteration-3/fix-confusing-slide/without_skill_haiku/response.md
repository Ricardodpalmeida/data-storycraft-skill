# Fixing the "Market Overview" slide

The original slide makes no single point. It shows two unrelated charts, uses two scales that cannot be compared, and never states what the viewer should conclude. The fixed version makes one point, that adding reps has not grown revenue, and the chart shows it directly.

## What was wrong

The title "Market Overview 2025" is a topic, not a takeaway, and the year is wrong because the data covers Q1 2024 to Q4 2025.

The pie chart shows market share, which says nothing about reps or revenue. It competes with the point the slide is supposed to make.

The bar and line chart uses two y-axes with unrelated ranges: revenue from 4.0 to 4.7 and reps from about 37 to 56. Those ranges can be set to make the lines look related, and the reader cannot tell whether the two actually move together. Across the eight quarters the correlation is 0.21, so the rising-line picture the chart suggests is not what the data shows. This dual axis is the main reason the slide is confusing.

The revenue bars start at 4.0 instead of zero. The Q4 24 bar (4.6) looks about six times the height of the Q1 24 bar (4.1), when the real difference is 12%.

Colour carries no meaning. Every bar and every pie slice has its own colour, and the "Revenue" legend swatch is red, which matches only the first bar. The "Us" slice is set apart only by a small offset. The sales reps legend also sits on top of the last data point.

## What changed

The pie is removed. Market share does not support the reps and revenue point, and if sales leadership needs it, it belongs on its own slide.

There is one chart on one axis. Both series are indexed to Q1 24 = 100, so they share a scale and their relative movement is visible without a second axis.

Colour now means something. Revenue is blue because it is the outcome the slide is about, and reps are grey. Direct labels at the line ends replace the legend and show the start and end values.

The title states the takeaway: "Adding 17 sales reps has not grown revenue." The subtitle gives the supporting numbers, and the footer explains the index and units.

## Numbers on the slide

Sales reps went from 38 to 55 between Q1 24 and Q4 25, up 45%. Quarterly revenue went from $4.1M to $4.2M over the same period, up 2%. Revenue is 9% below its Q4 24 peak of $4.6M.

## Assumptions

I compared the first and last quarters. A single quarter at each end can be sensitive, so the full-year view is a useful cross-check: 2025 revenue was $17.4M against $17.2M in 2024 (+1%), while average reps rose from 41 to 51 (+25%).

The script does not define the units. I treated reps as a quarterly count and revenue as quarterly $M.

The market-share figures have no period attached, so I could not match them to the revenue timeline. They are not on this slide.

The font is Inter. The script falls back to Helvetica, Arial or DejaVu Sans on machines without it.

## Talking points for the QBR (not on the slide)

Revenue per rep fell from about $108K per quarter in Q1 24 to about $76K in Q4 25, down 29%. Sales leadership is likely to ask about this next.

Expect a question about ramp time. New reps usually take several months to become productive, so part of the gap may be timing. The inputs contain no ramp, quota or territory data, so this slide cannot separate a hiring-timing effect from a real lack of impact. The headline describes what the data shows, namely that revenue stayed flat while reps grew. It does not prove that the hires caused the lack of growth.

## Files

The fixed chart is at evals-workspace/iteration-3/fix-confusing-slide/without_skill_haiku/outputs/fixed_slide.png

The script is at evals-workspace/iteration-3/fix-confusing-slide/without_skill_haiku/outputs/fixed_slide.py. Running it with python3 writes fixed_slide.png next to itself.
