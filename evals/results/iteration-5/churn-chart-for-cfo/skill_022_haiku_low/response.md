# Churn chart for the CFO

## Context

```
Audience:  CFO (budget and pricing decisions)
Ask:       Approve rolling back the June Pro price increase for existing Pro customers, with a 60-day check
Mechanism: Live presentation, deck circulated afterwards
Big Idea:  Pro churn rose from about 2.3% to 5.7% a month after the June price increase and has stayed there,
           so we should roll the increase back for existing Pro customers now and confirm the cause with a check.
```

Assumptions I made:
- The June price increase took effect in June 2025, the year in the file. If it was June 2026, the file does not cover it (see the first caveat below).
- Churn rates are monthly, and the file has no price, revenue or cancellation-reason data.
- The CFO's decision is to approve a rollback. A short monitoring period is included as a safeguard, since the file alone cannot prove cause.

## Deliverable

Chart: `<workspace>/iteration-5/churn-chart-for-cfo/skill_022_haiku_low/outputs/pro_churn_after_june_price_increase.png`

Script: `<workspace>/iteration-5/churn-chart-for-cfo/skill_022_haiku_low/outputs/make_chart.py`

The chart is a line chart with Pro in orange, the one accent, since the change is negative. Basic and Enterprise are grey and labelled directly. The June price increase is marked with a dashed line, and the values the message depends on are labelled (2.5% in June, 4.8% in July, 5.8% in December). The y-axis starts at zero.

Where the eye lands first: the orange line jumping between June and July, which is the point of the slide.

## Slide text

**Pro churn jumped after the June price increase and has stayed near 6%**

- Pro churn averaged 2.3% a month from January to June and 5.7% from July to December
- Basic (4.2%) and Enterprise (0.9%) churn did not change over the same period
- Pro active customers fell from 1,950 in June to 1,512 in December
- Estimated 345 more Pro customers lost than the January to June rate would predict, July to December

Decision requested: approve rolling back the June Pro price increase for existing Pro customers, and review Pro churn after 60 days to confirm the effect.

Footnote: Source: churn_by_plan.csv, January to December 2025. Timing shows association, not proven cause.

## Caveats to settle before the meeting

1. **Check the year.** The file covers 2025 only, and today is November 2026. If the price increase was in June 2026, this data cannot show it. Confirm the year before the slide goes out.
2. **Timing and plan fit are the evidence, not proof.** The jump starts in July, the month after the June change, and only Pro moved. Something else in July 2025 that hit only Pro (a product change, a billing issue, a competitor offer) would look the same. The CFO is likely to ask this first. Good answers would be cancellation reasons from exit surveys, or churn by customer cohort who did and did not receive the increase.
3. **The 345 figure is an estimate.** It applies the monthly churn rate to the active count each month and ignores new sign-ups, which the file does not show.
4. **The rollback has a revenue cost** that this file cannot size. Bring the price difference per customer and the count of affected Pro customers so the CFO can weigh the saved churn against the lost price.

Notes on the skill files used are in `<workspace>/iteration-5/churn-chart-for-cfo/skill_022_haiku_low/outputs/notes.md`.
