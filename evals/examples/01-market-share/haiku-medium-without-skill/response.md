The board chart is ready: `<workspace>/01-market-share/without_skill_haiku/chart.png` (1600 x 960 px).

It is a horizontal bar chart of 2026 revenue share by vendor, sorted from largest to smallest, with "Us" highlighted in blue and every other vendor in grey. "Others" sits last in a lighter grey since it is a catch-all rather than a vendor. The headline reads "We hold 18% of 2026 revenue share, #3 of 5 named vendors", and the subtitle notes that Northwind leads at 24%, 6 points ahead of us.

Assumptions I made:
- `share_of_revenue_pct` is share of revenue, as the column name says, and the figures are final 2026 numbers.
- The six rows sum to 100%, which I checked in the script.
- "Us" is the row labelled exactly "Us" in the file.
- "Others" is not counted as a named vendor, so our rank is 3 of 5.
- The board audience reads English and the figures are shown as whole percentages.

Script: `<workspace>/01-market-share/without_skill_haiku/make_chart.py`. It reads only the input CSV and writes only to this folder. Re-running it regenerates the chart.
