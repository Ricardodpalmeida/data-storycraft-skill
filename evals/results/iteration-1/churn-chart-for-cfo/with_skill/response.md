The chart is saved as `pro_churn_after_price_increase.png` (2200 x 1100, white background, sized to sit on a 16:9 slide). The script that builds it is `make_churn_chart.py`; every number in the title and labels is computed from your CSV, not typed in.

I built it for your CFO in a live presentation, with this as the Big Idea: Pro churn went from 2.3% a month to 5.7% after the June price increase while Basic and Enterprise did not move, so we recommend rolling the increase back for existing customers, and we need approval.

The eye lands first on the steep orange step between June and July. It is the only coloured thing on the page; the other two plans are grey context.

## What to put on the slide

Use this as the slide title, typed as real text and not baked into the image: **Roll back the Pro price increase for existing customers**

That puts the ask first, which suits a busy CFO. The chart title underneath then reads as the evidence for it.

Place the PNG under it, left-aligned and as large as the slide allows.

Two short lines of text under or beside the chart:

- Pro lost 438 active customers between June and December (1,950 to 1,512, down 22%).
- Churn has not settled, and has run between 5.6% and 6.1% every month since August.

End the slide with one closing line: "We ask you to approve returning existing Pro customers to their pre-June price."

Keep everything else off the slide. Basic and Enterprise detail, cancellation reasons and the break-even maths belong in your notes or an appendix.

## What to say (30 seconds)

"I'm asking you to approve rolling back the Pro price increase for existing customers. Pro churn averaged 2.3% a month through June. Since the increase it has averaged 5.7%, while Basic and Enterprise did not move at all. We have gone from 1,950 to 1,512 Pro customers in six months and the rate has not come down. Rolling back stops that leak, and here is what it is worth in revenue: [your number]."

## What the data supports, and where the CFO will push

The title says "since the June price increase", on purpose. The data shows the timing and a clean comparison, but it does not prove cause on its own. What it does show:

- Pro churn sat between 2.1% and 2.5% for six straight months, then stepped to 4.8% in July and stayed at 5.6% to 6.1% from August.
- Basic and Enterprise are flat across the same months (Basic averages 4.2% before and after, Enterprise 0.9% before and after). That rules out a market-wide or seasonal cause.
- Pro now churns more than Basic, which is the cheaper plan (5.8% against 4.2% in December). Before June it was about half.

What it cannot rule out is something else changing on Pro in July (a product change, a competitor move, a billing migration). If you can, pull churn for Pro customers who did not receive the increase yet, and the cancellation reasons. One of those two cuts would close the gap.

Four questions to have answers for:

1. Why did June barely move (2.5%)? I assumed the increase reached customers at their next billing date, so July was the first month it bit. Confirm the effective date and say it out loud before the CFO asks.

2. What does it cost? This is the one most likely to sink the ask, and the CSV has no price or revenue data. As a rule of thumb, Pro customers fell 22% from June, so revenue per remaining customer would have needed to rise about 29% (1,950 divided by 1,512) just to match June revenue. That ignores the roughly 26 net customers a month Pro was adding before June. Bring the actual before and after price and Pro MRR so you can show whether the increase is net positive or negative.

3. How many customers did we lose because of it? At the 2.3% baseline, the six months from July to December would have lost roughly 350 fewer Pro customers than they did (345 to 360, depending on whether the customer count is read as month start or month end). This is an estimate, so present it as "roughly 350", not as an exact figure.

4. Does a rollback bring them back? No. It stops further losses, at about 55 extra customers a month at December's rate. The ones already gone need a win-back offer, which you may want to mention as part of the ask.

One more thing in the numbers that you should know before the meeting. Pro was growing by about 26 net customers a month before June and has shrunk by 52 to 84 a month since. Working back from churn and the customer counts, new Pro sign-ups also look lower after June (roughly 65 to 70 a month before, 20 to 40 after). That depends on assuming churn applies to the previous month's customer count, so check it against real sign-up numbers. If it holds, a rollback for existing customers fixes churn but not acquisition, and the CFO may ask why new customers are excluded.

## Assumptions I made

- The data is calendar 2025 and the increase took effect in June, with the first affected renewals in July.
- Orange means "the problem" here. Keep it that way for anything else in the deck so the colour carries the same meaning on every slide.
- I left Pro active customers off the chart, because plotting it with churn would need a second y-axis, which misleads. It is in the slide text instead.
