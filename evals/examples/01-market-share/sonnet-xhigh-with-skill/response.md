```
Audience:  Board of directors
Ask:       Endorse closing the 3-point gap to Contoso as our next share target
Mechanism: Both: shown live in the board meeting and circulated in the pack, so the chart has to read on its own
Big Idea:  We are third with 18% share, exactly 3 points behind Contoso and 3 ahead of Fabrikam, so one place up or down is a 3-point move either way; we recommend the board backs closing the gap to Contoso as our next share target.
```

Your chart is at `<workspace>/01-market-share/with_skill/chart.png` (1600 x 960 px). The script that builds it from market_share.csv is `make_chart.py` in the same folder.

The eye lands first on the blue "Us" bar and its large 18%, because it is the only color and the biggest number on an otherwise grey page. The bold title at the top left then says the same thing in words.

**What the chart does**

- Horizontal bars, sorted from largest to smallest, all starting at zero. Others sits last because it is a catch-all bucket (it is also the smallest, so the order is the same either way).
- Everything is grey except Us, in one blue. Values are labeled directly on the bars, so there is no legend, no gridlines and no value axis to decode.
- The title carries the takeaway. The single blue note on the Us row gives the reason it matters: ranks 1st to 5th (24, 21, 18, 15, 12) are each exactly 3 points apart.
- Both axes are titled in one grey header row, and the footnote gives the source and what Others contains.
- Every number in the title and note is computed from the CSV and checked in the script.

**Assumptions I made, since I did not ask**

- The ask is mine. You did not say what the board should do, so I assumed "endorse closing the gap to Contoso". Swap in your real ask in the Big Idea and the speaker notes. The chart itself makes no claim about the ask, so it stays valid.
- The audience is the board, and the chart is both presented live and sent as a pre-read.
- I read share_of_revenue_pct as share of total market revenue and labeled the axis that way. If your board means units or customers, change the axis title.
- The footnote cites the file name as the source. Replace it with the official source name.

The file is a single-year snapshot, so the chart says where we rank, not whether we are gaining or losing, and the footnote states that. If you have 2025 shares, a before and after slopegraph would let the title carry direction, which boards usually ask about first.
