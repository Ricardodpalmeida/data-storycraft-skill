# Ad spend vs. sign-ups, 2026

The chart is saved at `<workspace>/03-ad-spend/without_skill_haiku/chart.png` (1600 x 960 px). The script that builds it is `<workspace>/03-ad-spend/without_skill_haiku/make_chart.py`.

**Headline for the review:** ad spend more than tripled from January to December (EUR 40k to EUR 130k, +225%), while sign-ups moved only from 510 to 600 (+18%). Sign-ups have stayed in a narrow 510 to 605 band all year.

**What the data shows**

- January to May: spend rose by EUR 4k and sign-ups by 45. Each EUR 1k bought about 12.6 sign-ups.
- June to December: spend rose by EUR 70k and sign-ups by only 20. The marginal return was about 0.3 sign-ups per extra EUR 1k.
- Cost per sign-up went from about EUR 78 in January to about EUR 217 in December. Sign-ups peaked in November (605) and dipped slightly in December (600), while spend was still climbing.

This pattern points to strong diminishing returns from the spend increases starting in June. It does not prove causation on its own, since seasonality, pricing, or channel mix could also play a part, but it is the first question I would bring to the review.

**Assumptions**

- The `ad_spend_eur_thousands` column is in thousands of euros, so 40 means EUR 40,000.
- `signups` is a monthly count of new sign-ups.
- Both axes start at zero, so the flat sign-up line is not exaggerated visually. Spend is on the left axis (bars) and sign-ups on the right axis (line).
- The growth percentages compare January with December, the first and last months in the file.
- The file contains only 2026 data, so no year-over-year comparison is shown.
