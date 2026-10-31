# Revised slide: "Adding sales reps has not grown revenue"

Files:
- Fixed PNG: <workspace>/iteration-3/fix-confusing-slide/without_skill_haiku_medium/outputs/fixed_slide.png
- Fixed script: <workspace>/iteration-3/fix-confusing-slide/without_skill_haiku_medium/outputs/fixed_slide.py

## What was wrong with the original

1. No single message. The slide shows two unrelated charts (market share and revenue vs reps) under a generic title ("Market Overview 2025"). The audience cannot tell what to take away.
2. The pie chart competes with the point. It shows market share in five rainbow colors, with arbitrary explode offsets. "Us" is a purple slice among others, and nothing marks it as the focus.
3. The revenue bars are truncated and multicolored. The y-axis starts at 4.0, so a 4.1 to 4.6 move looks like a huge swing. Each bar has a different color, which carries no meaning, and the legend shows a single red patch for a multicolor series.
4. The dual y-axes are arbitrary. The revenue axis runs 4.0 to 4.7 and the reps axis runs about 37 to 56. Changing either range changes how steep the line looks, so the visual "relationship" is an artifact of scaling.
5. The reps line is clipped at the top of the plot (Q4 25 touches the edge), and the title "Market Overview 2025" does not match the 2024 to 2025 data.

## What the fixed slide does

- Puts the message in the title: sales reps grew 45% while revenue is roughly flat.
- Indexes both series to Q1 2024 = 100 and uses one shared y-axis, so growth rates are compared directly and no axis choice manufactures a trend.
- Uses a neutral grey for the input (reps) and a single dark blue for the outcome (revenue), so the eye goes to revenue.
- Labels the line ends directly ("Sales reps: 55 (+45%)", "Revenue: $4.2M (+2%)") instead of a legend.
- Keeps a 16:9 canvas and a dark-on-light palette suitable for projection.

## Numbers used

- Sales reps: 38 (Q1 24) to 55 (Q4 25), +45%.
- Revenue: $4.1M (Q1 24) to $4.2M (Q4 25), +2%. Peak was $4.6M in Q4 24, then it fell back.

## Assumptions

- The revenue and sales rep figures are the ones in the original script, and they are correct and comparable (same period, same basis). I did not verify them against source systems.
- The market share pie was removed from this slide because it does not support the adding-reps message. If sales leadership needs it, it belongs in a backup slide or a separate slide after this one. I can rebuild it in the same style.
- No source line was added because the data origin was not given. Add one (for example, "Source: finance revenue ledger, CRM headcount") before the QBR.
- Revenue is in $M as in the original. The index means growth is shown as a percentage, so the currency does not affect the comparison.
- "Revenue" is treated as the revenue measure the original script labeled; if it is booked revenue versus bookings, the title should say which.

## Notes on the script

- The original saved `bad_slide.png` relative to the current directory. The fixed script saves to its own folder.
- I used a matplotlib `Agg` backend so it runs headless. Dollar signs in the subtitle are plain text, not math markup.
