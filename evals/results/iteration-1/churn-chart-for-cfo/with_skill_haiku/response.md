# Pro churn chart for the CFO slide

Audience: the CFO, who approves pricing and owns the revenue trade-off.
Ask: approve rolling back the June Pro price increase for existing Pro customers.
Big Idea: Pro churn more than doubled after the June price increase while our other plans held steady, so we recommend rolling the increase back for existing Pro customers, with Finance confirming the revenue impact before the decision.

Chart: evals-workspace/iteration-1/churn-chart-for-cfo/with_skill_haiku/outputs/pro_churn_after_june_price_increase.png

The eye lands on the orange Pro line jumping in July, right after the June marker. Pro churn averaged 2.3% a month from January to June and 5.7% from July to December. Basic (about 4.2%) and Enterprise (about 0.9%) barely moved.

## What to put on the slide

Title: Pro churn more than doubled after the June price increase

Three callouts, left-aligned beside the chart:
2.3% to 5.7%: average monthly Pro churn, January to June vs July to December.
Flat: Basic and Enterprise churn held steady all year, so the jump is specific to Pro.
1,950 to 1,512: Pro active customers, June to December (down 22%).

Decision line: Decision needed: roll back the June Pro increase for existing customers. Finance to confirm the revenue impact before the vote.

Footnote: the chart carries "Source: churn_by_plan.csv". Replace it with a plain source name before the deck is circulated.

## Before you present

The CSV shows timing and a contrast with the other plans. It does not prove the increase caused the churn. "The price increase is driving churn" is stronger than this data supports, and a CFO will push on it. A defensible sentence is: "Churn on Pro jumped the month after the increase while our other plans stayed flat, which points to the price change."

Four things to check before the meeting:

1. Confirm Basic and Enterprise got no price change in June. The contrast only works if they did not.
2. Check nothing else changed on Pro in July, such as a release, a billing or support change, a competitor launch or the end of a campaign. If something did, the timing still shows but the causal story weakens.
3. Confirm the effective date of the increase. A late-June start fits a July spike well. An earlier start would not.
4. Pull cancellation reasons if you have them. Price-related reasons would be the strongest support. The CSV is not split by customer age, so ask for churn among customers who received the increase, since that is the group a rollback for existing customers affects.

## The cost side, which the CFO will raise

The CSV has no price data, so it cannot size the rollback. You need D, the increase per customer per month, and P, the old Pro price.

Rolling back gives up about 1,512 × D a month on the current Pro base.
Excess churn now runs about 3.5 points a month above the pre-June rate, roughly 53 customers a month. Each one kept pays P.
Under best-case assumptions (the rollback fully restores the pre-June churn rate and kept customers stay), cumulative gain overtakes the cost after about 57 × (D ÷ P) − 1 months. That is about 5 months for a 10% increase and about 11 months for a 20% increase.
From July to December, roughly 360 more Pro customers left than the pre-June rate would have predicted.

## A second drop to check before the CFO does

Pro active customers fell by 438 between June and December. Churn explains most of it, but not all. Working back from the churn rates and customer counts, sign-ups also appear to have fallen: about 69 a month before June against about 28 a month from July to December, roughly 60% lower. This is an inference from the CSV, assuming churn is a percentage of the prior month's active base. Using end-of-month base gives similar results.

If real sign-up data confirms the drop, the price may be hurting acquisition as well. A rollback for existing customers would not fix that, because new customers would keep paying the higher price. Raise it yourself rather than let it come up in the room.

## Assumptions

The increase took effect in June, as you described. The CSV does not confirm the date.
Basic and Enterprise had no June price change. The chart's contrast depends on this.
Churn is a monthly percentage of the active base. The excess-churn and sign-up estimates depend on this.
The averages are simple means of the six months in each period.
The orange accent is for the negative series. The other two plans are grey and labelled directly, with no legend box, so identity does not depend on colour.
The PNG is light-background only. No dark-mode version was made.
The inputs folder also holds bad_slide.png, bad_slide.py and pilot_findings.md. I did not use them because they were not part of the request.

## Files

Chart: evals-workspace/iteration-1/churn-chart-for-cfo/with_skill_haiku/outputs/pro_churn_after_june_price_increase.png
Script: evals-workspace/iteration-1/churn-chart-for-cfo/with_skill_haiku/outputs/make_churn_chart.py
Skill reading log: evals-workspace/iteration-1/churn-chart-for-cfo/with_skill_haiku/outputs/notes.md
