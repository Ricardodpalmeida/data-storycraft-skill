# Before-and-after examples

The pairs in the README come from real runs, not mock-ups. Each example is one request run twice by the same model at the same reasoning level, once without the skill and once with it, each in a fresh agent that saw only its prompt and its input file.

## Runs

| Example | Input | Claude Haiku · medium | Claude Sonnet · xhigh |
|---|---|---|---|
| `01-market-share` | `market_share.csv` | Pair | Pair |
| `02-nps-by-region` | `nps_by_region.csv` | Pair | Pair |
| `03-ad-spend` | `ad_spend_signups.csv` | Pair | Not finished |
| `04-engagement-survey` | `engagement_survey.csv` | Pair | Pair |
| `05-mobile-checkouts` | `mobile_checkouts.csv` | Pair | Pair |
| `06-feature-satisfaction` | `feature_satisfaction.csv` | Pair | Not finished |

The two Sonnet runs marked "Not finished" stopped when the account reached its usage limit, so those pairs are left out rather than shown half done. The README also uses three pairs from the benchmark (`evals/results`): the churn chart and the slide fix on Claude Haiku at medium, the slide fix on Codex and the churn chart on Claude Sonnet.

Each folder holds `chart.png` and the agent's reply as `response.md`; skill runs also hold `notes.md`, the skill files they opened. All data is synthetic.

## Requests

| Example | User message |
|---|---|
| `01-market-share` | Here's our 2026 market share by vendor (market_share.csv); we're "Us". Make me a chart for the board update. |
| `02-nps-by-region` | Here's monthly NPS by region for 2026 (nps_by_region.csv). Make me a chart for the quarterly business review. |
| `03-ad-spend` | Here's our monthly ad spend and sign-ups for 2026 (ad_spend_signups.csv). Make me a chart showing both for the marketing review. |
| `04-engagement-survey` | These are our employee survey results, % favourable by theme for 2025 and 2026 (engagement_survey.csv). Make me a chart comparing the two years for the leadership team. |
| `05-mobile-checkouts` | Mobile share of checkouts went from 41% in 2024 to 68% in 2026 (mobile_checkouts.csv). Make me a chart for the e-commerce update. |
| `06-feature-satisfaction` | Here are the results of our feature satisfaction survey, % of respondents per answer for five features, n = 1,240 (feature_satisfaction.csv). Make me a chart for the product team. |

## Prompt

The same wrapper as the benchmark ([documentation/prompts.md](../../documentation/prompts.md)). Lines marked `+` appear only in the skill arm and lines marked `-` only in the control arm.

```diff
 Execute this task as if a real user asked it.

+- Skill path: <skill> (read SKILL.md first and follow it; open the reference files it points to only when needed; do not modify the skill)
 - Task (user's words): "<user message>"
 - Input files: <workspace>/inputs/<file> (read-only)
 - Save outputs to: <workspace>/<example>/<arm>/
-- Outputs to save: the chart as chart.png at 1600 x 960 pixels, the script, and your final reply to the user as response.md.
+- Outputs to save: the chart as chart.png at 1600 x 960 pixels, the script, your final reply to the user as response.md, and notes.md listing every skill file you read, in order.

-Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them. Read only your input file and write only to your output folder. Do not read anything under <repo>, <skill-draft-2>, <skill-draft-1> or <benchmark-workspace>, and do not load any skill.
+Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them. Read only your input file and write only to your output folder.
```

Models and reasoning levels were read back from the run logs: `claude-haiku-5-5` at `medium` and `claude-sonnet-5-5` at `xhigh`, identical in both arms of every pair.
