The chart and slide text are below. The data shows the timing clearly, but it does not yet prove the price caused the churn. Check the five points under "Before you present" before you present it as settled.

```
Audience:  CFO, who decides on Pro pricing and its revenue trade-off
Ask:       Approve rolling back the June Pro price increase for existing customers
Mechanism: Live presentation, with the slides possibly circulated afterwards
Big Idea:  The June Pro price increase is the most likely cause of a doubling in Pro churn
           that has cost about 345 extra customers since July, so we should roll it back
           for existing Pro customers; please approve.
```

The chart is saved at evals-workspace/iteration-3/churn-chart-for-cfo/with_skill_haiku/outputs/pro_churn_june_price_increase.png and is built by churn_chart.py in the same folder.

**What to put on the slide**

Title: Pro churn more than doubled after the June price increase

Subtitle: Basic and Enterprise churn held flat over the same months

Place the chart under the title, then add three short points beneath it:

- Pro churn averaged 2.3% a month from January to June and 5.7% from July to December.
- Over the same months, Basic (4.2%) and Enterprise (0.9%) did not move.
- About 345 more Pro customers churned than the January to June rate predicts, and the Pro base fell 22.5%, from 1,950 in June to 1,512 in December.

Close the slide with the ask in bold: **Approve a rollback of the June price increase for existing Pro customers.**

The chart footnote already cites churn_by_plan.csv, monthly churn rate by plan, January to December 2025.

The eye lands first on the orange Pro line rising from 2.5% in June to 4.8% in July. It is the only coloured series, the only break in the grey lines, and it sits beside the dashed June marker.

**Before you present**

1. Timing is not proof of cause. Pro is the only plan that moved, which fits a price effect. The file cannot rule out other Pro changes in June or July 2025, such as a product change, a billing migration, a support change or a competitor launch. Check that first, because the CFO is likely to ask. If something else changed, narrow the title and the ask.

2. The break starts in July, not June. June churn was 2.5%, just above the January to May range of 2.1% to 2.4%. A one-month lag is plausible if the increase reached invoices in June and customers left in July, but confirm the date the increase took effect. If it applied from July, the story is cleaner.

3. The data is ten months old. The file ends in December 2025 and today is 31 October 2026, so expect the question "what has happened since?" Refresh with 2026 data if it exists. If churn has already come down, the story changes.

4. The file cannot show the cost of a rollback. Get the monthly price uplift per Pro customer, the average Pro revenue per customer, and the number of customers on the increased price. Without these, the CFO cannot weigh the rollback against the churn.

5. New Pro sign-ups may have fallen too. The file implies new Pro customers dropped from about 69 a month (February to June) to about 28 a month (July to December). This is an estimate that assumes churn is measured on the prior month's base. On that basis, higher churn explains about 58% of the monthly swing in net Pro customers and fewer new customers about 42%. If the price also deters buyers, a rollback for existing customers will not fix that. Confirm with real sign-up data.

Until points 1 and 2 are checked, say that the timing and the Pro-only pattern point to the price increase, rather than saying it is proven.

**Assumptions**

- "June price increase" means June 2025, the only June the file covers. If you meant June 2026, this file cannot support the claim.
- Basic and Enterprise were not repriced, so they serve as the comparison group.
- Averages are simple means of the monthly rates, not customer-weighted.
- The 345 figure applies the January to June Pro rate (2.3%) to each month's Pro base as the baseline.

I did not modify the skill. The skill files I read, in order, are listed in notes.md at evals-workspace/iteration-3/churn-chart-for-cfo/with_skill_haiku/outputs/notes.md.
