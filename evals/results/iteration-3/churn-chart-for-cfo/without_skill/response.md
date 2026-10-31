The chart is ready as a 16:9 PNG (2000 x 1125) so it drops straight into a slide. The data backs your story on timing and isolation. It does not on its own prove cause, and the slide wording below is built so the CFO cannot pick that apart.

Files in evals-workspace/iteration-3/churn-chart-for-cfo/without_skill/outputs/

- pro_churn_after_price_increase.png (the chart)
- make_churn_chart.py (regenerates the chart and prints every number quoted below)
- response.md (this reply)

## What the data says

- Pro churn ran at 2.3% a month from January to June (range 2.1% to 2.5%). From July to December it averaged 5.7%, about 2.5x higher, peaking at 6.1% in September. It has plateaued, not recovered.
- Basic (4.2%) and Enterprise (0.9%) stayed flat all year. Nothing company-wide happened in July, which is what makes the Pro jump read as a Pro-specific event. Pro used to churn well below Basic and now churns faster than it.
- Pro active customers fell from 1,950 in June to 1,512 in December (down 22%). Against the old 2.3% churn rate, roughly 360 of those exits are extra.

## What to put on the slide

Title

"Since the June price increase, Pro churn has run at 2.5x its old level, and only on Pro"

I deliberately did not write "the price increase is driving churn". It is the conclusion you want, but a CFO will challenge the word "driving" and the title should not be the part that can be attacked. Say the causal part out loud and let the chart carry it.

Body, next to the chart, three short lines

- Pro churn rose from 2.3% a month (Jan-Jun) to 5.7% (Jul-Dec) and has not come back down.
- Basic and Enterprise did not move, so this is specific to Pro.
- The Pro base shrank from 1,950 to 1,512 customers (down 22%), about 360 more exits than the old churn rate would have produced.

The ask, in a box at the bottom

"Roll back the June increase for existing Pro customers."

The money line (fill this in before the meeting, it is the one the CFO cares about most)

"Pro needs a price increase of more than 29% just to bring in the same monthly revenue as in June. Ours was [X]%, so Pro revenue is [up/down] [Y]% versus June."

The 29% comes straight from the file (1,950 divided by 1,512). It assumes the increase applied to every Pro customer. You have the actual price change, I do not, so check it. If the increase was under 29%, this is your strongest line.

Speaker note, if asked about lifetime value

At 2.3% monthly churn a customer stays about 43 months on average, at 5.7% about 18 months. The new price would have to be roughly 2.5x the old one to earn back the shorter lifetime. This holds only if the extra churn is caused by the price and a rollback returns churn to the old level, so use it as a back-of-envelope, not a forecast.

## What the CFO is likely to ask

- Why did customers leave? The file shows when and on which plan, not why. Pull cancellation reasons or exit survey tags for July to December, and confirm nothing else changed on Pro in July (packaging, support, product, a competitor move).
- Is it existing customers who are leaving? The file is aggregated by plan. Your ask is a rollback for existing customers, so a split between customers on the old price and those who joined after is the evidence that settles it.
- Will a rollback bring them back? Churn has levelled off at about 6%, so a rollback stops roughly 50 to 70 extra cancellations a month. It will not return the customers who already left. Present the benefit as stopping the loss.
- What about new sign-ups? This one is my inference, so keep it off the slide. If I rebuild monthly additions from the customer counts and churn rates (closing base = opening base x (1 - churn) + new customers), gross new Pro customers run at about 69 a month from February to June, then about 28 a month from July to December. If that holds, the higher price is also hurting acquisition, which a rollback limited to existing customers would not fix. Have a position ready on whether new customers should be included.
- Is this still true today? The file ends in December 2025. If you have 2026 months, add them. The CFO will ask whether churn is still elevated, and a longer flat line at about 6% (or a recovery) changes the message.

## Assumptions I made

- The new price took effect with July billing. June churn is still normal at 2.5%, and the jump starts in July, so the marker sits on June and the effect shows up right after it. Confirm the effective date.
- Churn percent is the share of the opening Pro customer base lost in the month. The excess-exits estimate (about 360) uses the prior month's customer count as the base. Using the month-end count gives about 345.
- Basic and Enterprise had no price change in the period.
- I labelled the chart 2025 because that is what the file's months say.

## Chart choices

Pro is the only coloured line and is thick. Basic and Enterprise are grey context, labelled at the line ends instead of in a legend. The shaded area between the dashed Jan-Jun Pro average and the actual line shows the extra churn after the increase. The slide title is left off the PNG on purpose, so it does not repeat the title you put on the slide.
