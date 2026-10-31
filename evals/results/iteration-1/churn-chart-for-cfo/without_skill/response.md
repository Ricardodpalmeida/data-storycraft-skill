# Pro churn chart and slide for the CFO

The chart is ready (`pro_churn_chart.png`, 16:9, 2400x1350, built to drop straight onto a slide). The data backs your story well on timing and specificity, but it cannot prove the price caused the churn, and it has no revenue numbers. The slide below is written to stay on the safe side of that, and the section after it lists the three checks that would let you say "driven by" with a straight face.

## What the data shows

Pro churn ran at 2.3% a month from January to June and never left a 2.1% to 2.5% band. It jumped to 4.8% in July and has averaged 5.7% since, which is 2.5x the old level. It has not faded: 5.8% in December against a 6.1% peak in September.

Basic and Enterprise have the same average before and after the increase, to two decimals (4.18% and 0.93%). So the move is specific to the plan that was repriced. Pro used to churn at roughly half of Basic's rate, and has churned faster than Basic in every month since July.

The Pro base went from 1,950 customers in June to 1,512 in December (down 22%), after growing 7% in the first half of the year.

## What to put on the slide

Slide title (the PNG deliberately has no headline, so the title does that job):

> Pro churn has run at 2.5x its old level since the June price increase, and no other plan moved

Left two thirds: the chart.

Right third, three big numbers with a one-line caption each:

| Big number | Caption |
|---|---|
| 2.3% to 5.7% | Average monthly Pro churn, January to June vs July to December |
| 1,950 to 1,512 | Pro customers, June to December (down 22%, after +7% in H1) |
| About 350 | More Pro customers lost since July than the old churn rate would have produced |

Bottom bar, the ask:

> We recommend rolling back the Pro price increase for existing customers from [date].

One line under the ask, for the CFO's money question:

> At 5.7% monthly churn a Pro customer stays about 18 months on average, against about 43 months at 2.3%. A price increase would have to be well above 100% to pay back a lifetime that much shorter. Actual increase: [X]%.

Footnote on the slide: "Source: monthly churn by plan, Jan to Dec 2025. Churn = share of the plan's customers lost in the month."

Speaker notes (about 40 seconds):

"Pro churn sat around 2.3% for the first half of the year. After the June price increase it went to 4.8% in July and has stayed close to 6% since. Basic and Enterprise did not move at all, so this is not a company-wide effect, it is specific to Pro. We have lost about 350 more customers than we would have at the old churn rate, and a Pro customer now stays about 18 months instead of about 43. Unless the increase was far above 100%, we earn less per customer lifetime than before. We recommend rolling it back for existing customers."

The only blanks you must fill are the rollback date and the actual percentage increase. Neither is in the file.

## What the chart proves and what it does not

You want to show the increase is driving churn. The chart gives you three strong pieces of circumstantial evidence: the jump comes right after the increase, only the repriced plan moved, and it has persisted for six months. It does not prove cause. The file has no price, no effective date, no customer-level data and no cancellation reasons. A Pro-only event in July (a product change, an outage, a billing change, a competitor launch) would produce the same picture.

If the CFO asks "how do you know it was the price?", the honest answer from this file is that nothing comparable happened on the other plans. Until you have run the checks below, I would say "coincides with and is consistent with the increase" in conversation, and keep the slide title as written, since it states only what the data shows.

Three checks, about an hour of work, that would make the causal claim solid:

- Pull cancellation reasons for Pro since July and see what share cite price.
- Split Pro churn by billing cycle or renewal date. Price-driven churn clusters at renewal.
- Ask product and support whether anything else changed on Pro in June or July.

## Two things the CFO may raise

Do not say 438 customers churned. Excess churn accounts for about 350 of the 438 drop. The rest looks like fewer new sign-ups: if the customer column is an end-of-month count, implied gross additions fell from about 70 a month before the increase to between 19 and 42 a month after. A rollback for existing customers does nothing for that, so expect the question of whether the new-customer price should change too.

The 18 versus 43 month lifetime comparison assumes the churn rate holds and uses revenue, not margin. On revenue the break-even increase is about 150%. If variable costs are 20% of price it is still about 120%. If churn fades back toward 2.3% the argument weakens, but December gives no sign of that yet.

If the CFO wants proof before committing, a clean fallback is to roll back for a random half of existing Pro customers for 90 days and compare churn between the two groups.

## Assumptions I made

- The churn percentage is the share of a plan's customers lost in that month. The file does not say so explicitly.
- The increase took effect around the end of June. The dashed line sits on June and the jump shows in July. June itself (2.5%) is inside the normal band, so confirm the effective date, because the CFO will ask why June is flat.
- `pro_active_customers` is read as an end-of-month count.
- The "about 350" figure is (monthly Pro churn minus the 2.3% baseline) times the previous month's customer base, summed July to December. The two ways of reading the customer column give 345 and 360.
- I ignored the other files in the inputs folder (a market share slide and a customer-support pilot note) because they do not relate to this question.

## Files

- `evals-workspace/iteration-1/churn-chart-for-cfo/without_skill/outputs/pro_churn_chart.png`
- `evals-workspace/iteration-1/churn-chart-for-cfo/without_skill/outputs/make_chart.py` (rebuilds the chart and prints every number quoted above)
- `evals-workspace/iteration-1/churn-chart-for-cfo/without_skill/outputs/response.md`
