Audience:  Marketing review group, with the budget owner as the decision maker
Ask:       Decide whether to keep raising monthly ad spend, or hold it while we test where sign-ups stop responding
Mechanism: Both (shown live in the review, and sent as a document afterwards)
Big Idea:  Since June, ad spend has more than doubled (EUR 60k to EUR 130k) while monthly sign-ups have grown only 3% (580 to 600), so cost per sign-up has risen from EUR 78 in January to EUR 217 in December; we should hold spend at the current level and set a sign-up target before adding more budget.

Chart: <workspace>/03-ad-spend/with_skill_haiku/chart.png
Script: <workspace>/03-ad-spend/with_skill_haiku/make_chart.py

The eye lands first on the action title and then on the blue spend line climbing to EUR 130k in December, which is set against the flat dark grey sign-up line below it.

Design choices:
- Two panels sharing the month axis instead of a secondary y-axis, so each series keeps its own honest scale (both start at zero).
- Blue is the one accent (spend). Sign-ups are dark grey. Values are labelled directly on the points that matter (Jan, Jun, Dec), so no legend is needed.
- The shaded area marks June onward, the period the title refers to.

Assumptions I made:
- Ad spend is in EUR thousands, as the column header says.
- Sign-ups are a monthly count of new sign-ups, not unique users.
- Nov and Dec are used as supplied. Today is 31 Oct 2026, so these months are either a plan or a forecast, not actuals. Please confirm before this goes to the review, because the "since June" story depends on the Dec figure.

Caveats the audience may raise:
- Sign-ups did rise from 510 to 580 between January and June while spend moved only from EUR 40k to EUR 60k, so spend is not the only driver. The chart shows this; the title focuses on the more recent period.
- The data shows correlation over time, not the effect of each euro spent. A channel or campaign breakdown would be needed to say where the extra spend stops paying back.
- Totals for the year: spend EUR 928k, sign-ups 6,830.
