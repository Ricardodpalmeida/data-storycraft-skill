Chart: <workspace>/iteration-6/churn-chart-for-cfo/skill_023_haiku_low/outputs/pro_churn_after_june_price_increase.png

Context

```
Audience:  CFO (decision maker on pricing and retention)
Ask:       Approve rolling back the June Pro price increase for existing customers
Mechanism: Live presentation, with the slide also sent as a document
Big Idea:  Pro churn more than doubled after the June price increase (2.3% average before, 5.7% after), about 345 extra Pro customers lost in Jul-Dec, so roll the increase back for existing Pro customers.
Check:     No totals in the input. Averages recomputed from the monthly rates: Pro 2.30% before, 5.70% after (2.48x). Basic 4.18% and Enterprise 0.93% both unchanged. No mismatches.
```

Slide text

Title: Pro churn more than doubled after the June price increase, while Basic and Enterprise stayed flat

Body: Monthly Pro churn rose from 2.5% in June to 4.8% in July and peaked at 6.1% in September. It was still 5.8% in December. Basic (4.2%) and Enterprise (0.9%) churn did not move over the same months, so the change is specific to Pro. Roughly 345 more Pro customers churned from July to December than the January-June rate would predict.

Footnote: Source: churn_by_plan.csv, Jan-Dec 2025. The timing is consistent with the price increase, but this data does not show the cause. Other changes in July are not in this data set.

Ask: Roll back the June Pro price increase for existing customers, and decide by [date] whether to extend the rollback to new sign-ups.

The eye lands first on the orange Pro line stepping up right after the dashed June line.

Assumptions I made
- The June price increase is the Pro price change you mentioned, and it took effect in June. The data has no price column, so the chart shows the churn timing, not the price itself.
- The churn columns are monthly rates, and the active-customer count is the base for those rates. The 345 figure is an approximation: for each month from July to December, (Pro churn rate minus the Jan-Jun average of 2.30%) times that month's active Pro customers, summed.
- The ask has no date or amount in the brief, so the Ask line has a placeholder [date]. Fill it in before the meeting.

Things to fix or prepare before the CFO sees this
- The data supports "coincides with" more than "driving". Use "after" in the title, as written, and keep the causal caveat in the footnote. A CFO will ask about other July changes (a competitor move, a product release, a billing change). Check those first.
- The chart cannot show what rolling back would earn back. That needs the size of the price increase and the Pro revenue per customer. With those, compare the revenue kept by lower churn against the revenue given up on the increase. Without that comparison, the ask is a recommendation, not a decision.
- Basic and Enterprise staying flat is the strongest supporting point. It rules out a general churn event, such as a broad service problem, that would hit every plan.
