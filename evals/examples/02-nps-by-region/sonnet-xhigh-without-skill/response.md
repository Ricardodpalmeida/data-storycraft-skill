The chart is ready for the QBR. It is a 1600 x 960 PNG, with the Nordics decline as the story and the other six regions in grey for context.

**What it says**

Nordics NPS peaked at 46.0 in March and has dropped every single month since, ending December at 24.0, which is 22 points lower. In January Nordics sat third of seven regions. It is now last, and 12 points below the next lowest region (France at 36.1).

The other six regions are flat. Their net change from January to December runs from -2.4 (UK) to +0.4 (Iberia), with no trend in any of them.

**How I built it**

I used a line chart because the question is how each region moved over time. Nordics is in red and everything else is in grey, so the eye goes straight to the one region that needs a conversation. Regions are labelled at the end of each line with their December value, so nobody has to decode a legend. Light quarter bands (Q1 to Q4) let the room find the quarter they care about. The y axis runs from 20 to 50 rather than from zero, and the footer says so.

The title states the finding rather than describing the chart, so the slide works even if someone only reads the headline.

**Assumptions I made**

- You did not say which quarter the review covers, so the chart shows the full year with quarters marked instead of cutting it to one quarter.
- The figures are plotted exactly as they are in the file, with no smoothing or rounding. End labels show one decimal, matching the CSV.
- "Held steady" for the other six means no sustained movement in either direction. They do wobble by a few points month to month (France dips to 34.3 in October, for example).

**Two things to check in the data before you present**

The file includes November and December, but today is 31 October, so those two months are dated after today. If they are forecasts or placeholders, the chart should not present them as actuals. I built in a switch for this: running `python make_chart.py --projected-from Nov` redraws November onward as dashed lines with a "Projected" label. Through October the story holds either way, since Nordics falls from 46.0 to 27.0 and has declined every month since March.

The Nordics series also looks different from the rest. Its values are all whole numbers and fall in an almost straight line (-3 a month for five months, then -2, -2, -2, -1), while the other six regions have decimals and normal month-to-month noise. That can be real, but it is worth confirming that Nordics comes from the same source and method as the other regions, because the whole headline rests on it.

One smaller point: UK closed at 44.8, its lowest reading of the year, down 3.5 from its August high of 48.3. It is still the top region, and the drop is well inside normal noise next to the Nordics move, so I left it off the chart.

**Files**

- <workspace>/02-nps-by-region/without_skill/chart.png
- <workspace>/02-nps-by-region/without_skill/make_chart.py
- <workspace>/02-nps-by-region/without_skill/response.md
