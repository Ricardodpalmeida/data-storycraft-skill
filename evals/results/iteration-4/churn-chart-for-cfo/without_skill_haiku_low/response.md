# Pro churn and the June price increase: chart and slide notes

## Chart

`<workspace>/iteration-4/churn-chart-for-cfo/without_skill_haiku_low/outputs/pro_churn_vs_june_price_increase.png`

Built with matplotlib from `make_churn_chart.py` in the same folder. Pro is the only highlighted series, Basic and Enterprise are grey for contrast, and the post-June period is shaded.

## What the data shows

- Pro churn averaged 2.3% per month from January to June and 5.7% from July to December, about 2.5 times the baseline.
- The jump is a step, not a drift: June was 2.5% (still baseline), July was 4.8%, and it stayed between 5.6% and 6.1% after that.
- Basic churn stayed between 4.0% and 4.4% all year. Enterprise stayed between 0.8% and 1.1%. Neither moved when Pro did.
- Active Pro customers fell from 1,950 in June to 1,512 in December, a drop of 22.5%.
- Using the Jan to Jun baseline, roughly 345 more Pro customers churned from July to December than would have at 2.3% (estimate, see assumptions).

## Suggested slide

Title: "Pro churn more than doubled after the June price increase; other plans held steady"

Body, in three points:
1. Pro churn: 2.3% per month before June, 5.7% after (2.5x).
2. Basic and Enterprise churn did not change over the same months, which points to the Pro price change rather than a company-wide problem.
3. About 345 extra Pro customers churned from July to December, and Pro active customers fell 22.5% since June.

## Where the argument is weaker

Before the CFO meeting, the following need to be addressed, because the roll-back ask depends on them:

- The file shows timing, not cause. It has no price data, no list of what else changed in July, and no reasons for cancellation. The strongest version of the claim is "churn rose right after the price change and only on Pro", not "the price increase caused the churn". Exit-survey or cancellation-reason data would make the case much stronger.
- Rolling back is a revenue question as well as a churn question. The file does not show the size of the increase or the revenue per Pro customer. If Pro revenue per customer rose enough to offset ~22% fewer customers, a full roll-back could cost money. The CFO will likely ask for this, so it is worth building before the meeting: monthly Pro revenue before and after June, with and without the lost customers.
- The chart's subtitle and title use the six-month average (5.7%), while the end label shows December (5.8%). It is labelled clearly, but expect a question about it.

## Assumptions

- The price increase took effect in June and applied to Pro only, since Basic and Enterprise are used as the control. The file does not confirm either point.
- Churn percentages are monthly rates of the customers active in that month, and the active count is used as the base for the 345 estimate.
- The July step is treated as the response to the June change. A one-month lag is typical for a price change that applies at the next billing cycle, but this is an assumption.
- The file was read as provided. Nothing was written back to the input.
