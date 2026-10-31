```
Audience:  E-commerce leadership and the product and marketing teams reading the update (assumed)
Ask:       Make mobile the primary checkout experience when prioritising work (assumed, the brief gave none)
Mechanism: Both: shown on a slide in the update, and readable on its own if the deck is sent around
Big Idea:  Mobile is now the majority of checkouts (68%, up from 41% in 2024), so we should design and prioritise checkout for mobile first.
```

The chart is saved at `<workspace>/05-mobile-checkouts/with_skill/chart.png` (1600 x 960 px, white background). The script that builds it from the CSV is `make_chart.py` in the same folder.

The eye lands first on the large blue 68% at the upper right, right after the title. It is the only big accent-coloured number on an otherwise grey chart, and the line leads straight to it.

The title states the takeaway with the exact numbers, and a 0 to 100 scale keeps the size of the move honest. I labelled both values directly and dropped the y-axis, since the exact values are what matter. A light 50% line shows the minority-to-majority shift, and the dotted drop lines frame the +27 percentage points, which is the gap between 68% and 41%.

A few things to know before you present it:

I assumed the ask, since the request did not give one. If the update is asking for something else, only the Ask and Big Idea lines above change, and the chart still holds.

The file has only 2024 and 2026, so the chart shows two points and the footnote says the line implies no 2025 value. The chart also does not claim when mobile crossed 50%, only that it is above 50% in 2026 and was below it in 2024.

This is a share of checkouts, not a count. It shows mobile's portion grew, but not whether mobile checkouts increased in number or desktop and other devices shrank. Avoid saying "mobile checkouts grew 66%" from this chart. The accurate phrasing is "up 27 percentage points".

The footnote cites `mobile_checkouts.csv` as the source because that is all I was given. Swap in the name of the analytics system if you prefer.
