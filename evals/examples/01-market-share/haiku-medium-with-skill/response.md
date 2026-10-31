# Board chart: 2026 market share by vendor

**Context**

```
Audience:  Board of directors
Ask:       Note that we are third at 18% and endorse a plan to close the 3-point gap to Contoso
Mechanism: Sent document (board update pack)
Big Idea:  We are third with 18% share, 6 points behind Northwind and 3 behind Contoso,
           so the board should back a plan to close the gap to Contoso.
```

**Chart:** `<workspace>/01-market-share/with_skill_haiku/chart.png` (1600 x 960)

The chart is a horizontal bar chart sorted by share, with "Us" in the accent blue and every other vendor in grey. The title states the takeaway, and the two gap annotations sit next to our bar. The eye lands first on our blue bar, then on its gap annotation.

**Assumptions**

- The request did not name the audience or the ask. I assumed a board, and that the ask is to note our third place and back a plan to close the gap to Contoso. If the board is being asked for something else, the title and annotation are the only parts to change.
- "Us" is the vendor named "Us" in the file, and the figures are 2026 share of revenue as given (they sum to 100%).
- "Others" stays as the last bar, regardless of its value, so it does not compete with the named vendors.
- Bars start at zero, and no pie chart or secondary axis is used.

Script: `<workspace>/01-market-share/with_skill_haiku/make_chart.py`
