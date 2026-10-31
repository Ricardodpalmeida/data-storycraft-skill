The new slide is ready. It now says one thing: reps are up 45% since Q1 2024, revenue is up 2%, and revenue per rep has fallen 29%.

Files are in evals-workspace/iteration-3/fix-confusing-slide/without_skill/outputs/

- fixed_slide.png (1999 x 1125, 16:9)
- fixed_slide.py (regenerates the PNG, every percentage on the slide is computed from the data in the script)

**What was wrong with the original**

Your director is right, and it comes down to a few things.

- The title was "Market Overview 2025". That is a topic, not a message, and the revenue chart covers 2024 and 2025 anyway. Nobody could tell what they were supposed to conclude.
- The slide had two unrelated charts side by side. The market share pie has nothing to do with "adding reps hasn't grown revenue", so half the slide was competing with your point.
- The right chart put revenue on one axis and reps on another. With two independent scales, where the line sits against the bars is arbitrary, so the picture can't show whether revenue followed headcount. The reps line also ran off the top of the plot, so the Q4 25 point was clipped.
- The revenue axis started at $4.0M instead of zero. That made a 12% move from Q1 24 to Q4 24 look like a bar six times taller, and made normal quarter-to-quarter movement look dramatic.
- Every bar was a different color with no meaning, and the pie used red, orange, yellow, green and purple plus exploded slices and shadows. The eye goes to the colors instead of the data.
- Legends sat on top of the data, the quarter labels were rotated 45 degrees, and a dashed grid ran both ways. All of that is noise.
- The script also imported a 3D toolkit it never used, which is harmless but worth knowing is dead code.

**What I changed**

- The title is now the finding: "Reps are up 45% since Q1 2024. Revenue is up 2%." The subtitle gives the consequence, 17 more reps and revenue per rep down 29%.
- The pie is gone. If sales leadership needs market share, it should be its own slide.
- Reps and revenue are now two lines on one shared scale, both indexed to Q1 24 = 100. No second axis, no truncated bars. Reps climbs to 145, revenue sits near 102, and the gap is the whole story. The end labels carry the real numbers (38 to 55 reps, $4.1M to $4.2M), so nobody has to decode the index.
- A second, smaller panel shows revenue per rep ($108K down to $76K per quarter, axis from zero). It is the number that turns "revenue is flat" into "each added rep is producing less".
- Colors are two distinct hues (navy for reps, orange for revenue) plus gray for the derived metric. Lines are labeled directly instead of using legends. Quarters are horizontal with the year underneath.

**Assumptions I made**

- Sales reps is headcount in the quarter, and revenue per rep is quarterly revenue divided by that quarter's headcount. The footnote says so.
- I used 16:9 instead of the original 14 x 6 shape so it drops into a slide without cropping.
- The script gives no data source, so I did not add a source line. Add yours before it goes out.
- "Since Q1 2024" uses the first and last quarters. That endpoint choice is generous to revenue, because Q1 24 is the lowest revenue quarter in the series. A full-year view gives the same answer: FY25 revenue was $17.4M against $17.2M in FY24 (+1%), with average headcount up 25% (40.75 to 51).

**Two questions to expect in the room**

- Why did revenue peak at $4.6M in Q4 24? Through Q4 24 revenue roughly tracked headcount (reps +16%, revenue +12%). Since then reps are up 11 (+25%) and revenue is down 9%. That is arguably a sharper version of your point, and the chart shows it.
- Aren't new reps still ramping? That is the most likely pushback. The data cannot rule it out, and the slide does not claim to explain why revenue is flat, only that it is. Having the average ramp time for a new rep ready would help.
