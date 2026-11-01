# Churn chart for the CFO

Chart: `<workspace>/iteration-4/churn-chart-for-cfo/new_skill_haiku_low/outputs/pro_churn_june_price_increase.png`
Script: `<workspace>/iteration-4/churn-chart-for-cfo/new_skill_haiku_low/outputs/churn_chart.py`

## Context

Audience:  CFO
Ask:       Approve rolling back the June Pro price increase for existing Pro customers
Mechanism: Live presentation, deck circulated afterwards
Big Idea:  Pro churn more than doubled after the June price increase and has not recovered, while Basic and Enterprise stayed flat, so we recommend rolling the increase back for existing Pro customers; please approve.

## Slide text

Title: Pro churn more than doubled after the June price increase and has not recovered

- Pro churn averaged 2.3% a month from January to June 2025 and 5.7% from July to December.
- Basic (4.2%) and Enterprise (0.9%) churn did not change over the same period, so the shift is specific to Pro.
- Pro active customers fell from 1,950 in June to 1,512 in December, about 22% fewer.
- Ask: approve rolling back the June price increase for existing Pro customers, and track Pro churn monthly to confirm recovery.

Footnote: Source: churn_by_plan.csv, monthly churn by plan, Jan to Dec 2025. Timing association only; other causes not ruled out.

## Where the eye lands

The orange Pro line jumping up in July, next to the dashed June price increase marker.

## Assumptions I made

- The price increase took effect in June 2025. Churn responded in July, so I treated July as the first affected month.
- Churn values are the monthly percentage of customers on each plan.
- The Basic and Enterprise lines are the control. Their flat trend argues against a company-wide cause such as a macro shock, but it does not prove the price was the cause.

## What the CFO is likely to push on

1. Other causes in June and July 2025. Check whether anything else changed for Pro in that window (product changes, support, billing, a competitor move). If something did, the chart still shows the timing, but the claim needs to be narrowed.
2. Revenue. A rollback gives up price revenue from the remaining Pro base. The case holds only if the churn saved is worth more than that. Bring the price difference and Pro revenue per customer. Roughly 440 fewer Pro customers is the gap to close.
3. Data freshness. The file ends in December 2025 and today is October 2026. Pull 2026 data before the meeting. If Pro churn has already come back down, the slide has to change.
4. Proof. The strongest version of the ask is a rollback for one group of existing Pro customers with a comparison group that keeps the new price. That would show cause, not just timing.
