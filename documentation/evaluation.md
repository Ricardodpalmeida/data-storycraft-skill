# Evaluation protocol

The benchmark answers one question: does an agent with the skill communicate data measurably better than the same agent without it?

## Design

| Element | Choice |
|---|---|
| Comparison | The same model with and without the skill (paired arms) |
| Isolation | Every run is a fresh agent or subagent that shares no context with any other run |
| Inputs | The same user message and the same files in both arms |
| Only variable | The skill: read and followed in one arm, forbidden in the other |
| Scoring | 22 binary assertions across three scenarios, plus a visual check of every chart |
| Reporting | Totals with and without the four assertions that test the skill's own conventions |

## Models and reasoning levels

Both arms of every pair ran the same model at the same reasoning effort, so the skill is the only difference. Every agent ran at `xhigh`, and Claude Haiku ran a second time at `medium` to test a weaker setting. Model IDs and effort come from the run logs (Claude subagent transcripts and Codex session rollouts), not from configuration defaults.

| Agent | Model | Reasoning effort | Harness |
|---|---|---|---|
| Claude Sonnet | `claude-sonnet-5-5` | `xhigh` | Claude Code agent harness v2.1.316, one background subagent per run |
| Claude Haiku | `claude-haiku-5-5` | `xhigh` | Claude Code agent harness v2.1.316, one background subagent per run |
| Claude Haiku | `claude-haiku-5-5` | `medium` | Same, with the effort set explicitly on each run |
| Codex | `gpt-6-astra` | `xhigh` | Codex desktop app on Windows (`codex-cli 0.166.0-alpha.5.1`), one orchestrator thread spawning subagents, at most three at a time |

Claude runs at `xhigh` inherited it from the orchestrating session and Codex subagents from the orchestrating thread; the `medium` runs set it explicitly. Two supporting roles sat outside the comparison: Codex's automatic tool-approval reviewer (`codex-auto-review`, `low`), which did no task work, and the author and grader (`claude-opus-5-5`, `xhigh`).

## Scenarios

| Scenario | Request | Inputs | Assertions |
|---|---|---|---|
| `churn-chart-for-cfo` | A chart and slide text arguing that a June price increase drives Pro churn and should be rolled back | `churn_by_plan.csv` | 8 |
| `fix-confusing-slide` | A critique and a redesigned PNG of a slide meant to show that adding reps has not grown revenue | `bad_slide.py`, `bad_slide.png` | 7 |
| `exec-deck-storyline-pt` | Text for a six-slide deck, requested in Portuguese, asking an executive committee to approve a rollout | `pilot_findings.md` | 7 |

All data is synthetic and each set hides a trap. The [README](../README.md#benchmarks) describes what each file contains and where the trap is. Inputs are in [evals/inputs](../evals/inputs) and the scenario definitions in [evals/scenarios](../evals/scenarios).

## Assertions

Assertions marked *method format* test conventions the skill introduces. No control group can be expected to follow them, so results are reported with and without them.

**churn-chart-for-cfo**

| # | Assertion | Type |
|---|---|---|
| 1 | Response states the audience, the ask and a one-sentence Big Idea | Method format |
| 2 | Chart title is an action title naming Pro churn and the June price increase | Outcome |
| 3 | Pro series is highlighted while Basic and Enterprise are de-emphasized in grey | Outcome |
| 4 | Lines are labeled directly with no separate legend | Outcome |
| 5 | Chart has no gridlines or chart border, and no top or right spines | Outcome |
| 6 | Y-axis values carry a % unit and the y-axis is titled | Outcome |
| 7 | The June price increase is annotated on the chart | Outcome |
| 8 | Response gives explicit slide text including the rollback ask | Outcome |

**fix-confusing-slide**

| # | Assertion | Type |
|---|---|---|
| 1 | Response names a single biggest problem first | Method format |
| 2 | The 3D, shadowed pie chart is replaced by a sorted bar chart or text | Outcome |
| 3 | The secondary y-axis is removed (direct labels or separate panels sharing the x-axis) | Outcome |
| 4 | The truncated revenue bar axis (starting at 4.0) is fixed, or the bars are replaced by a line | Outcome |
| 5 | Rainbow colors are replaced by grey plus a single accent | Outcome |
| 6 | The new chart has an action title stating that reps grew while revenue stayed flat | Outcome |
| 7 | Numbers in titles and annotations match the source data (reps 38 to 55, revenue about 4.1M to 4.2M) | Outcome |

**exec-deck-storyline-pt**

| # | Assertion | Type |
|---|---|---|
| 1 | Deck states a one-sentence Big Idea with the 180k EUR ask | Method format |
| 2 | Every slide title is an action title (a full takeaway sentence, not a topic label) | Outcome |
| 3 | The ask appears up front (executive summary or first slides), not only at the end | Outcome |
| 4 | Executive summary points mirror the following slide titles | Method format |
| 5 | The billing escalation risk (+15%) is acknowledged with its mitigation, not hidden | Outcome |
| 6 | Final slide contains an explicit call to action for approval of 180k EUR | Outcome |
| 7 | All figures match the source notes (38%, 22%, 4.2 vs 4.3, 1.4M, 180k, nine markets) | Outcome |

## Run protocol

1. The inputs sit read-only in a shared workspace. Each run writes only to its own folder, `<scenario>/<arm>/outputs/`.
2. All runs of a round start in parallel, each in a fresh context, with the prompt in [prompts.md](prompts.md) as their only instruction. No run may ask questions; each states its assumptions instead.
3. Skill runs write `notes.md`, listing every skill file they opened in order. It confirms the skill was loaded and shows which references each task pulled in.
4. Control prompts forbid reading the skill folders and loading any skill. Control subagents in Codex were never given the skill path.
5. Claude token counts and wall time come from each subagent's completion report. Codex elapsed times come from the orchestrator and are approximate; Codex did not expose token counts.

## Grading

- Each assertion is pass or fail, judged by reading the reply and the deliverables, opening every PNG, and checking every number in titles and annotations against the inputs.
- Grades are stored in [results/iteration-3/grading.json](../evals/results/iteration-3/grading.json) and [results/codex/grading.json](../evals/results/codex/grading.json), in the assertion order above.
- All outputs are kept under [evals/results](../evals/results), so any grade can be checked.

## Rounds

| Round | Skill version | Configurations | Purpose |
|---|---|---|---|
| 1 | First version | Sonnet with skill, Haiku with skill, Sonnet control | Baseline and gap finding |
| 2 | After the round 1 fixes | The two cells that missed | Confirm each fix |
| 3 | After the verbosity cut (4,781 words) | Sonnet and Haiku, each with its own control | Final Claude measurement |
| Haiku medium | Same as round 3 | Claude Haiku at `medium` with skill and control | Weaker setting |
| Codex | Same as round 3 | Codex with skill and Codex control | Cross-vendor check |

Scores and findings per round are in [evals/RESULTS.md](../evals/RESULTS.md).

## Limitations

- Each configuration ran once per scenario, so a difference of one assertion is within noise.
- The grader also wrote the skill and the assertions, and knew which arm produced each output. An independent, blind grader is the obvious next step.
- Three synthetic scenarios cannot represent all data-communication work.
- The Claude runs inherited the account's saved writing preferences (for example, no em dashes) in both arms. This affects style equally across arms, and no assertion tests it.
- Codex subagents were launched by an orchestrating thread rather than one by one from the harness, and its elapsed times include launch overhead.
- Round 1 had no Haiku control; round 3 adds it.

## Reproducing

1. Replace the placeholders in each prompt (`<skill>`, `<workspace>` and the others listed in [prompts.md](prompts.md)) with your own paths.
2. Start each prompt from [prompts.md](prompts.md) in a fresh session of the agent under test, with the files from [evals/inputs](../evals/inputs).
3. Grade each output against the assertions above, and compare arms within the same model.
