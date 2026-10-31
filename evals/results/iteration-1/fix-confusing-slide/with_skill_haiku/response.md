**Biggest problem:** The slide carries two unrelated stories, and its dual-axis chart with a truncated revenue axis makes flat revenue look like it rises with headcount.

**Context**

Audience: Sales leadership at the QBR.
Ask (my assumption): Review revenue per rep before approving further hires.
Big Idea: Adding 17 sales reps since Q1 2024 has barely grown revenue, so productivity needs review before more hiring.

**What is wrong**

| Lesson | Issue | Why it hurts | Fix |
|---|---|---|---|
| Context | The title "Market Overview 2025" names a topic, not a point. The market share pie and the revenue chart are two stories on one slide. The data runs Q1 2024 to Q4 2025, so "2025" is also wrong. | The audience cannot tell what to take away. | Action title that states the takeaway. One message per slide. |
| Visual | Pie chart for market share. Revenue bars and the reps line share one chart on two y-axes. | Pies hide comparisons. A second y-axis implies a relationship that the scale choice creates. | Drop the pie. Split reps and revenue into two panels on one quarter axis. |
| Design | Revenue axis starts at $4.0M, not zero. The reps axis runs from about 37 to 56. | The Q4 24 bar at $4.6M looks six times taller than the Q1 24 bar at $4.1M. The real gap is 12%. | Bars start at zero. |
| Clutter | Eight rainbow bar colors and five pie colors that mean nothing. Dashed gridlines, two boxed legends, 45 degree quarter labels, "24.0%" decimals, an exploded slice and a shadow. | Every element competes for attention, and the color carries no meaning. Diagonal text is slower to read. | Grey for context, one accent for the message. No gridlines, border or legend. Horizontal labels. |
| Focus | Nothing is emphasized. The eye lands on the exploded Supplier B slice (31%). "Us" (20%, third of five) looks like every other slice. | Attention goes to a point that does not matter for this message. | One accent on revenue, the outcome that did not move. Label only the start, the peak and the end. |
| Story | No ask and no takeaway. The top-right legend sits on the final reps point. | A reader can conclude that revenue rose with reps, which the data does not show. | A proposed next step on the slide. The title and subtitle carry the evidence. |

**Redesign**

Two stacked panels on one quarter axis. Both have zero baselines, no y-axis, and labels only where they carry the story.

- Top: sales reps per quarter in grey bars. Labels on 38 reps (Q1 24) and 55 reps (Q4 25). Header: +17 reps (+45%) since Q1 24.
- Bottom: quarterly revenue in $M in the accent blue. Labels on $4.1M (Q1 24), $4.6M peak (Q4 24) and $4.2M (Q4 25). Header: +2% since Q1 24.
- Title: Adding 17 sales reps since Q1 2024 has barely grown revenue.
- Subtitle: Full-year 2025 revenue was up 1% on 2024, while average sales headcount rose 25%.
- Bottom line: Proposed next step: review revenue per rep before approving further hires.
- Footnote: units and a source placeholder.

The eye lands on the title, then on the flat blue revenue bars under the rising grey ones.

Files:
- Fixed slide: evals-workspace/iteration-1/fix-confusing-slide/with_skill_haiku/outputs/fixed_slide.png
- Script (rerun it to regenerate the PNG; it derives every headline number from the data and asserts it): evals-workspace/iteration-1/fix-confusing-slide/with_skill_haiku/outputs/fixed_slide.py

**Check these before the QBR**

- The ask and the Big Idea are my inference. If the decision is different, change the bottom line and the Big Idea.
- I wrote "barely grown" because full-year growth is 1% and Q4 25 is 2% above Q1 24. "Has not grown" would overstate it.
- The data shows revenue did not follow headcount. It does not show that reps are the cause. Ramp time, market conditions or territory design could explain it. Present it as a question to investigate, not a verdict on the sales team.
- I assumed revenue is quarterly revenue in $M and sales reps is the quarter's rep count. Please confirm both.
- The source footnote is a placeholder.
- Revenue per rep (quarterly revenue divided by reps) fell from about $108k in Q1 24 to $76k in Q4 25, down 29%. I kept it off the slide. It is a good backup if the discussion turns to productivity.
- I dropped the market share pie because it answers a different question. If it must stay in the QBR, give it its own slide: sorted horizontal bars with Us in the accent. On this data, Us is third at 20%, behind Supplier B (31%) and Supplier A (24%). I can build that slide if you want it.
