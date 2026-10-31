# Pro churn after the June price increase: chart and slide text

## Chart

File: <workspace>/iteration-3/churn-chart-for-cfo/without_skill_haiku_medium/outputs/churn_pro_vs_plans.png

Script: <workspace>/iteration-3/churn-chart-for-cfo/without_skill_haiku_medium/outputs/churn_chart.py

## What the data shows

- Pro monthly churn averaged 2.3% from January to June 2025 and 5.7% from July to December.
- It jumped from 2.5% in June to 4.8% in July, peaked at 6.1% in September, and was 5.8% in December.
- Basic churn did not move (4.18% average before and after) and Enterprise churn did not move (0.93%).
- Estimated Pro accounts lost per month rose from about 44 (January to June average) to about 97 (July to December average). These counts are the churn rate multiplied by the active base, so treat them as estimates.
- The Pro active base fell from 1,950 in June to 1,512 in December, a drop of about 22%.

## Caveat you need before the CFO meeting

The data shows that Pro churn rose at the same time as the June price increase, and that no other plan moved. That is a strong timing pattern and it makes the price increase the leading suspect. It does not prove the price increase caused the churn. The file has no price data, no churn reasons, no customer-level data, and no record of what else changed on the Pro plan in mid-2025 (product, billing, support, onboarding, competitors).

A CFO will likely ask those questions. If the slide says "the price increase is driving churn" as a settled fact, the first challenge could undermine the whole ask. The safer wording is "coincides with" plus a check you can run before the meeting. Exit survey reasons for Pro cancellations since July, or a comparison of churn between customers who received the increase and those who did not, would settle it.

## Rollback case

The rollback decision depends on money the file does not contain. The trade-off is:

- Revenue gained from the price increase on the Pro accounts that remain.
- Against lifetime revenue lost from roughly 50 extra Pro accounts per month (97 minus 44) since July.

Pull the Pro price difference and ARPU and put them next to that churn figure. If the rollback recovers more revenue than it costs, the case is strong. If it does not, a partial measure may be better, such as a retention offer for at-risk existing customers or a rollback for a random half of them for two months, with churn tracked against the other half.

## Slide text

Title: Pro churn rose from 2.3% to 5.7% a month after the June price increase. Basic and Enterprise did not change.

Supporting points:
- Pro churn averaged 2.3% a month before the increase and 5.7% after it, peaking at 6.1% in September.
- Basic (4.2%) and Enterprise (0.9%) churn stayed flat over the same period.
- Pro lost about 97 accounts a month after the increase, compared with about 44 before.

Ask: Approve a rollback test for existing Pro customers while we measure its revenue and churn impact against the current price, with a decision point at the end of Q1.

Footnote: Monthly churn rate by plan, January to December 2025. Source: churn_by_plan.csv. The timing association does not establish cause.

## Assumptions

- The June price increase took effect in June 2025, as you described. The file has no date for it, and I assumed the churn response began in July, the first month after the increase.
- Churn values are monthly rates. The lost-account counts assume the active customer count is the base each month.
- The increase applied to all Pro customers. If it applied only to some, the slide needs to say so.
- I used only churn_by_plan.csv, as you specified.
