```
Audience:  CFO, who decides on the pricing and revenue trade-off
Ask:       Approve rolling back the June Pro price increase for existing Pro customers
Mechanism: Live presentation next week, so the slide stays sparse and you carry the detail
Big Idea:  Pro churn has more than doubled since the June price increase while Basic and
           Enterprise stayed flat and the Pro base shrank 22%, so we recommend rolling the
           increase back for existing Pro customers; please approve it.
```

The chart is at `evals-workspace/iteration-3/churn-chart-for-cfo/with_skill/outputs/pro_churn_after_price_increase.png` (2400 x 1320 px), and the script that builds it from your CSV is `make_chart.py` in the same folder. The eye lands first on the thick orange Pro line jumping at the dashed June marker, because it is the only coloured, heavy element on a field of grey lines.

One thing up front, because the CFO will go straight to it. The chart proves the churn story, but the decision will turn on revenue, and the file has no price data. Read the "before the meeting" section below before you finalise the slide.

## What to put on the slide

Use this as the slide title: "Roll back the June Pro price increase for existing customers".

Under it, one smaller line: "Pro customers are down 22% since June, from 1,950 to 1,512".

Then the chart, about 10 inches wide on a 16:9 slide, left-aligned with the title. Nothing else. The chart already carries its own finding as a title, the 2.3% and 5.7% averages, the control plans and the source, so adding bullets would only compete with it.

The chart title says "right after" and not "caused" on purpose. A CFO will challenge "driving", and the flat Basic and Enterprise lines make the causal argument for you without you having to claim more than the data shows.

## What to say (about three minutes)

Pro was steady. For six months churn sat between 2.1% and 2.5% and the base grew from 1,820 to 1,950 customers. In June we raised the price. From July churn jumped to 4.8%, peaked at 6.1% in September and was still 5.8% in December, so six months on there is no sign of it fading. Basic and Enterprise did not move at all, which tells us this is not a company-wide problem. Pro is the only plan whose price changed and the only plan whose churn changed. The Pro base is now 22% smaller than in June. We are asking you to approve a rollback for existing Pro customers from [date].

## Before the meeting

**Run the revenue break-even.** Pro has 22.5% fewer customers than in June, so the price increase only raised Pro revenue if it was bigger than about 29%, assuming everyone who stayed pays the new price. With your real percentage plugged in, Pro revenue versus June is roughly:

| Price increase | Pro revenue vs June |
|---|---|
| 10% | -14.7% |
| 15% | -10.8% |
| 20% | -7.0% |
| 25% | -3.1% |
| 30% | +0.8% |

Pick the row that matches the actual increase and put that one line in your notes or on the slide. If the increase was well above 29%, rollback is a harder sell on revenue alone and your argument shifts to lost growth and customer lifetime value.

**Check the cause.** The timing and the flat control plans are strong, but they are not proof. Confirm nothing else changed for Pro in July (product, billing, support, a competitor). Also expect the question "why did June look normal?" June churn was 2.5%, basically the old level. I assumed the new price started hitting customers at renewal, so the effect shows from July. If the price actually took effect in July, move the label.

**Check new customers.** The file does not split existing from new customers, so it supports "Pro churn rose" but not "existing customers are the ones leaving". There is also a derived signal worth checking with whoever owns the data. If churn is calculated on the Pro customer count and the count is month-end, the numbers imply new Pro sign-ups fell from about 70 a month through June to roughly 15 to 20 a month by December. If that is real, the new price is also hurting acquisition, and a rollback only for existing customers would not fix it. I kept this off the slide because it depends on how churn is defined in your system. If it holds up, consider widening the ask to new customers or proposing a test.

## Assumptions I made

- The CFO is the decision maker and the slide is shown live.
- Churn is a monthly rate, as a percentage of each plan's customers.
- "Before" is January to June and "after" is July to December, and the price increase is drawn at June.
- Every number on the chart is either a raw data point or a simple mean of six monthly rates, and the script recalculates them from the CSV and stops if the claims "more than doubled" or "Basic and Enterprise stayed flat" ever stop being true.
