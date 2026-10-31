**Context**

```
Audience:  CFO
Ask:       Approve rolling back the Pro price increase for existing customers, after confirming the revenue impact
Mechanism: Live presentation (slide), chart may also be sent as a document
Big Idea:  Pro churn more than doubled after the June price increase (2.3% a month before, 5.7% after) while Basic and Enterprise did not move, so we recommend rolling the increase back for existing Pro customers.
```

**Deliverable**

Chart: `<workspace>/iteration-3/churn-chart-for-cfo/with_skill_haiku_medium/outputs/pro_churn_after_price_increase.png`

Script that produces it: `<workspace>/iteration-3/churn-chart-for-cfo/with_skill_haiku_medium/outputs/make_churn_chart.py`

The chart is a line chart of monthly churn for all three plans in 2025. Pro is the only orange line, Basic and Enterprise are grey and labelled directly, and a dashed line marks the June price increase. Pro's June (2.5%) and December (5.8%) values are labelled.

**What to put on the slide**

Title: Pro churn more than doubled after the June price increase, while Basic and Enterprise held steady

Chart: the PNG above.

Footnote: Source: churn_by_plan.csv, monthly churn rate by plan, Jan to Dec 2025.

Three supporting sentences you can say out loud or put under the chart:

- Pro churn averaged 2.3% a month from January to June and 5.7% from July to December.
- Basic (about 4.2%) and Enterprise (about 0.9%) averaged the same before and after July, so the change is specific to Pro.
- Pro active customers fell from 1,950 in June to 1,512 in December, and roughly 345 more Pro customers churned than the June rate would have predicted. This is an estimate that applies the excess churn rate to each month's active base.

Ask line: Approve rolling back the Pro price increase for existing customers, once the revenue impact is confirmed.

**Where the eye lands first:** the orange Pro line jumping up after the dashed June marker, because it is the only coloured line and the steepest movement on the page.

**Assumptions I made**

- The price increase took effect in July billing. The file shows June at a normal 2.5%, so if the increase was live in June, the timing needs checking before the meeting.
- The file has no price or revenue data, so the slide makes no revenue claim. The CFO will likely ask whether the lost customers cost more than the extra price brings in. Bring average revenue per Pro customer before and after the increase to answer that.
- The 345 figure assumes churn applies to each month's active Pro customers. It is an approximation.

**Caveats to raise before presenting**

- This is strong correlation, not proof of cause. Basic and Enterprise staying flat argues against a company-wide cause such as the economy or seasonality. But anything else that changed for Pro in July (a feature change, support, a campaign, a competitor move) would produce the same pattern. Check the July change log before saying "caused by".
- The data does not show that a rollback would bring churn back down. Customers who left may not return, and the rollback has its own revenue cost. Present it as the recommended test or decision, not as a guaranteed fix.
- I did not run the dataviz palette validator. The chart uses one accent colour plus greys, so there is no categorical palette to check, but the orange and grey contrast should be looked at on the projector.
