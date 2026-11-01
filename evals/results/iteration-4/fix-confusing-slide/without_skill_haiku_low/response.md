# Revised slide: sales reps vs revenue

Fixed PNG: `<workspace>/iteration-4/fix-confusing-slide/without_skill_haiku_low/outputs/fixed_slide.png`
Fixed script: `<workspace>/iteration-4/fix-confusing-slide/without_skill_haiku_low/outputs/fixed_slide.py`

## What was wrong with the original

1. The slide had no single message. It put a market-share pie next to a revenue chart, so the audience had to work out what connects them. The title "Market Overview 2025" described a topic, not a finding.
2. The revenue axis started at 4.0 and ended at 4.7. That makes a 0.5M swing look like a collapse or a spike, and it exaggerates quarter-to-quarter noise.
3. The chart used a dual y-axis with different scales (revenue 4.0 to 4.7, reps about 37 to 56). Where the lines cross depends on the axis ranges, not the data, so the reader can make the reps line look like it tracks revenue or not at will.
4. Bar colours were a rainbow of eight unrelated colours. They encode nothing, so they compete with the data.
5. The pie used red, orange, yellow, green and purple with exploded, shadowed slices. It is hard to compare slice sizes and adds nothing to the reps-versus-revenue argument.
6. The legends were inconsistent: "Revenue" showed a red swatch that matched only the first bar, and the reps legend was placed over the plotted line.

## What changed

- The slide now carries one message in its title: average sales reps rose 25% in 2025 while average quarterly revenue rose 1%.
- The market-share pie is removed. It is not part of this claim.
- Two side-by-side panels, one per measure, each on a zero-based axis. Reps are grey (the input) and revenue is dark blue (the outcome). No dual axis, so there is no crossing to manipulate.
- Values are labelled directly on the bars, so no one has to read gridlines.
- A dashed line and 2024 / 2025 labels mark the year boundary.

## Numbers behind the headline

- Average sales reps: 40.75 in 2024 and 51.0 in 2025, up 25.2%.
- Average quarterly revenue: $4.30M in 2024 and $4.35M in 2025, up 1.2%.
- Q4 25 revenue ($4.2M) is below the Q4 24 peak ($4.6M), with 25% more reps.

## Assumptions

- The data in the original script is correct and is the source for the new slide.
- Annual averages are a fair summary. The headline uses averages rather than the Q1 24 to Q4 25 endpoints, because single quarters are noisy (Q4 24 is a clear outlier at 4.6).
- "Revenue" means quarterly revenue in $M, as labelled in the original.
- The market-share data is not needed for this message. If leadership wants it, it belongs on a separate slide.
- The slide is 14 x 6 inches at 120 dpi, as before, for consistency with the original deck.

## Caveat for the review

The chart shows that reps and revenue moved in different directions, not why. Before the QBR, be ready for the question "is it the reps' productivity, the mix of accounts, or pricing?" The slide does not answer that, and the data here cannot either.
