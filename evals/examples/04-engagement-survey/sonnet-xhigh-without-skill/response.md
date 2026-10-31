The chart is ready at `<workspace>/04-engagement-survey/without_skill/chart.png` (1600 x 960 px).

The story for leadership is that Career growth fell from 66% to 51% favourable, a drop of 15 points, and it is now our lowest-scoring theme. It was fourth highest last year. The other seven themes all went up, by 2 to 5 points, with Tools (+5) and Recognition (+4) improving the most. The title and subtitle say exactly that, so the chart can go on a slide without extra explanation.

I used a dumbbell chart, one row per theme, with a grey dot for 2025 and a blue dot for 2026. Both values are printed next to the dots and the change in points sits in a column on the right, so nobody has to read values off the axis. Career growth is the only row in red, which makes it the first thing the eye lands on. Rows are sorted by change, with the biggest decline at the top, rather than alphabetically or by score.

A few assumptions and things to know:

- I kept "favourable" and the theme names exactly as they appear in the file, and treated the values as whole-number percentage points, so "change" means percentage points, not percent change.
- The x axis starts at 45%, not 0%, so the gaps are easier to see. This is noted in the footnote on the chart. Distances between dots are still comparable across rows.
- The file has no response counts or margins of error, so I could not test significance. The 15 point drop in Career growth is large, but if the number of respondents per theme is small it is worth confirming before the meeting. The 2 to 3 point gains on the other themes are modest and I described them only as improvements, not as clear wins.
- The data shows what moved, not why. If leadership asks about the Career growth drop, the next useful cuts would be by department, tenure or level, plus any free-text comments from the survey.

Files in `<workspace>/04-engagement-survey/without_skill/`:

- `chart.png` is the chart.
- `make_chart.py` is the matplotlib script that reads the CSV and produces it. Run it with `python3 make_chart.py` to regenerate if the numbers change.
- `response.md` is this note.
