# Pro churn chart for the CFO slide

Chart: evals-workspace/iteration-3/churn-chart-for-cfo/without_skill_haiku/outputs/pro_churn_price_increase.png
Script: evals-workspace/iteration-3/churn-chart-for-cfo/without_skill_haiku/outputs/churn_chart.py

## Bottom line

The data supports the first part of your claim. Pro churn more than doubled after the June price increase, while Basic and Enterprise did not move. The data does not yet support "roll it back". The file has no pricing and no revenue, and the CFO will ask whether the higher price made or lost money. I would frame the slide as a decision to analyze, with the rollback as one option.

## Slide text

Title: Pro churn more than doubled after the June price increase

Subtitle: Monthly churn rate by plan, 2025

Bullets:

1. Pro churn averaged 2.3% a month from January to June and 5.7% from July to December, 2.5 times higher. It peaked at 6.1% in September and was still 5.8% in December.
2. Basic (4.2%) and Enterprise (0.9%) churn was unchanged across both periods, so the price increase is the most likely driver.
3. Since July, about 345 more Pro customers have churned than the January to June rate would predict. The Pro base fell 22%, from 1,950 in June to 1,512 in December.
4. Decision needed: whether to roll back the increase for existing Pro customers. This needs a net revenue model before we commit.

## Numbers behind the slide

| Metric | Jan to Jun | Jul to Dec |
|---|---|---|
| Pro churn, monthly average | 2.3% | 5.7% |
| Basic churn, monthly average | 4.18% | 4.18% |
| Enterprise churn, monthly average | 0.93% | 0.93% |
| Pro churned customers per month (estimate) | 43 | 97 |

Pro active customers: 1,950 in June, 1,512 in December.

## Assumptions

- The price increase applied to Pro only and started in June. The churn step appears in July, so I placed the change point between June and July. If the new price hit at renewal, a one-month lag is normal, but expect the question.
- Churned Pro customers equal the churn rate times the active count. The file does not say whether the active count is start or end of month, so the counts are estimates.
- Excess churn is the monthly rate above 2.3%, times the active count, summed over July to December. That gives about 345 customers.

## What the data cannot show

- The price itself. Get the old price, new price, effective date and number of customers affected.
- Cause. The timing and the flat Basic and Enterprise lines make the price increase the leading explanation. Another Pro-only change in July, such as a feature limit, onboarding change, support change or competitor move, would look the same. Ask the product team what else changed in Pro that month.
- Who churned. The file does not separate existing customers from new ones, so it cannot confirm that a rollback for existing customers would keep the churners.
- Net revenue. As a rough break-even, assume a rollback brings back the roughly 345 lost customers, giving about 1,857 customers at the old price versus 1,512 at the new price. Under these simple assumptions, rolling back wins if the increase was smaller than about 23% of the old price. Above that, keeping the increase earns more. This ignores new sign-ups and future churn.

## Other signal to verify, not for the main slide

Implied new Pro customers (change in the active base plus churned customers) fell from about 70 a month in February to June to about 24 a month in July to December. If that holds, the increase may also be hurting acquisition. The file does not confirm this definition, so check it with the data owner before using it.

## Before the meeting

1. Get the price change details: old price, new price, effective date and affected customers.
2. Get revenue per Pro customer so the rollback can be priced.
3. Check whether anything else changed on the Pro plan in June or July.
4. If possible, compare churn for customers who renewed after the increase with customers who had not yet renewed. That is the strongest test of cause.
