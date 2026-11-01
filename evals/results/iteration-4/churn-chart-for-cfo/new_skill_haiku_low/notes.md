# Notes

## Skill files read, in order

1. <skill>/SKILL.md
2. <skill>/reference/context.md
3. <skill>/reference/designing.md

Other reference files in the skill (choosing-visuals, decluttering, focusing-attention, model-visuals, storytelling, worked-example, case-studies, practice-and-teams) were not opened. The dataviz skill was not opened; the chart uses the matplotlib starting point and emphasis rules from SKILL.md.

## Other input read

- <workspace>/inputs/churn_by_plan.csv (read-only, not modified)

## Key numbers (computed from the CSV)

- Pro churn: mean 2.3% (Jan to Jun 2025), mean 5.7% (Jul to Dec 2025). Peak 6.1% (Sep). Dec 5.8%.
- Basic churn: mean 4.18% both periods. Enterprise churn: mean 0.93% both periods.
- Pro active customers: 1,950 (Jun) to 1,512 (Dec), down 438 (about 22%).
- Implied Pro churned customers per month (churn % x active): about 45 before July, about 88 to 106 after July.

## Assumptions

- Price increase effective June 2025; first affected month July 2025.
- Churn % is monthly, as a share of customers on each plan.
- Data ends Dec 2025; no 2026 data was provided.
- Rendering: matplotlib 3.11.2, Agg backend, 200 dpi.
