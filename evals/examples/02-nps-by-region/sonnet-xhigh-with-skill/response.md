```
Audience:  Leadership team at the quarterly business review, with the regional heads in the room
Ask:       Agree a root-cause review of the Nordics NPS decline, with a named owner and a recovery plan at the next review
Mechanism: Both, a live walk-through in the review and the deck circulated afterwards
Big Idea:  Nordics NPS has fallen every month since March, from 46 to 24, while the other six regions held steady,
           so we recommend a root-cause review with a named owner; please approve it.
```

The chart is in `chart.png` (1600 x 960). The script that builds it, `make_chart.py`, is in the same folder.

Title on the chart: "Nordics NPS has fallen every month since March, from 46 to 24".

The eye lands first on the thick orange Nordics line, because it is the only colored element and the only one that moves away from the pack, and the action title above it says the same thing in words.

What the data shows, all checked against the file:

- Nordics went 44, 45, 46 from January to March, then lost 3 points a month from April to August, 2 a month from September to November and 1 in December. That is 9 declines in a row and 22 points off the March peak.
- The other six regions each stayed within 3 points of their January score all year, so none of them contradicts the story. UK (down 2.4) and DACH (down 1.1) end slightly lower than they started, and both moves sit inside their normal month to month swings.

Choices I made without asking:

- I used orange for Nordics because the news is negative, and grey for everything else, with the region names written at the end of each line instead of a legend.
- The vertical axis runs from 20 to 50 so the six steady lines stay readable. It is a line chart, so a non-zero start does not distort lengths, and the footnote says where the axis starts.
- I put the ask in the context block above and kept it off the chart. If your real ask is different (for example funding or a specific action), change that line and the talk track, since the chart does not need to change.

Two things to confirm before this goes in front of the room:

1. The file has November and December 2026, but today is 31 October 2026, so those two months cannot be actuals yet. I plotted all twelve months as supplied. If they are forecasts, the headline claim still holds through October (Nordics 46 to 27, down 19), and the title and the "down 22" callout should use those numbers instead.
2. The Nordics series is whole numbers falling in an almost straight line, while the other six have one decimal and ordinary noise. That can be real, but someone will ask whether it is a small sample, a survey method change or modeled values. The chart shows what happened, not why, so the cause is the first thing the review should settle.
