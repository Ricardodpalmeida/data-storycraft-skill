# Feature satisfaction chart for the product team

The chart is saved at `<workspace>/06-feature-satisfaction/without_skill_haiku/chart.png` (1600 x 960 px). The script that produces it is `<workspace>/06-feature-satisfaction/without_skill_haiku/make_chart.py`.

**Headline:** Exports is the only feature where dissatisfaction outweighs satisfaction (41% dissatisfied vs 38% satisfied). Search leads at 70% satisfied, followed by Dashboards (62%), Alerts (58%) and Sharing (54%).

**Chart design:** a diverging stacked bar chart. Each bar is centred on the neutral band, with dissatisfied ratings extending left and satisfied ratings extending right, split into "dissatisfied" and "very dissatisfied" (and "satisfied" and "very satisfied") segments. Features are sorted by share satisfied, and a right-hand column gives the satisfied and dissatisfied totals so the product team does not need to add segments.

**Assumptions:**
- Each feature was rated by all 1,240 respondents. Every row in the CSV sums to exactly 100%, so the percentages are treated as shares of the full sample for each feature.
- "Satisfied" means satisfied plus very satisfied, and "dissatisfied" means dissatisfied plus very dissatisfied. These are the totals in the right-hand column.
- The neutral share is split evenly on either side of zero so that the satisfied and dissatisfied bars start from the same centre line.
- The chart uses only the input CSV. No other data was used.
