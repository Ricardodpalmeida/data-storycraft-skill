# Evaluation results

## Setup

| Scenario | Input | Output asked for | Assertions |
|---|---|---|---|
| `churn-chart-for-cfo` | `inputs/churn_by_plan.csv` | Chart PNG and slide text arguing for rolling back a price increase | 8 |
| `fix-confusing-slide` | `inputs/bad_slide.py`, `inputs/bad_slide.png` (3D pie, dual axis, truncated bars, rainbow colors) | Critique and a redesigned PNG | 7 |
| `exec-deck-storyline-pt` | `inputs/pilot_findings.md` (Portuguese prompt) | Text for a 6-slide deck asking an executive committee to approve a rollout | 7 |

The inputs are synthetic and each hides a trap: a causal claim the churn data cannot prove, a slide that commits every classic charting mistake at once, and pilot notes whose savings estimate does not reconcile with their own numbers. The README's [test data table](../README.md#benchmarks) describes each one.

Every run was an independent agent that saw only the user prompt, the inputs and, in the skill arm, the skill folder. Control runs were told not to read the skill or load any skill. The scenarios and assertions are in `scenarios/<name>/eval_metadata.json`; the exact prompts for each arm, the models and the reasoning levels are in [documentation/](../documentation/). Charts were checked visually and numbers against the inputs. Within each pair, both arms used the same model at the same reasoning effort (`xhigh`, plus one Claude Haiku round at `medium`), so the skill is the only difference. Each configuration ran once per scenario, so differences of one assertion are within noise.

Four assertions check conventions the skill itself introduces, and a control group cannot be expected to follow them: the Big Idea block in the churn and deck scenarios, "biggest problem first" in the review, and an executive summary that mirrors the slide titles. The tables report totals with and without them.

## Iteration 4 (weak models, 0.2.1 and 0.2.2)

An external run on gpt-6-luna at reasoning effort `low` (Codex, both arms in fresh contexts, skill 0.2.0) scored 17/22 with the skill and 13/22 without. The five misses with the skill each traced to the skill text:

| Miss | Cause in 0.2.0 | Fix in 0.2.1 |
|---|---|---|
| Churn title dropped "price increase" | Nothing said that naming the event is not a causal claim | Keep the event in the title; causal caveats go in the footnote |
| Gridlines kept | "Keep very light grey gridlines only if readers must trace values" read as permission | No exception; label the values readers need |
| Rollback ask only in speaker notes | No rule on where the ask goes | Slide text is one block that ends with the ask |
| Review listed issues without a biggest problem | Template only, no check | Name the biggest problem before any list; added to the final check |
| Executive summary did not mirror the titles | "Mirrors the slide titles" was too abstract | Write the titles first, then reuse them as the summary bullets |

The final check also gained a reconciliation question (none of the Luna decks flagged that 1.4M did not match €0.90 × 2.1M). SKILL.md grew by about 80 words and one line.

A/B check on Claude Haiku at reasoning effort `low`, the same model and effort in every arm:

| Scenario | 0.2.1 | 0.2.0 | No skill |
|---|---|---|---|
| churn-chart-for-cfo | 8/8 | 8/8 | 5/8 |
| fix-confusing-slide | 7/7 | 7/7 | 6/7 |
| exec-deck-storyline-pt | 7/7 | 6/7 | 4/7 |
| **Total** | **22/22** | **21/22** | **15/22** |
| Without the 4 method-format assertions | 18/18 | 18/18 | 15/18 |

Haiku at low already passed most of what Luna missed, so this run mainly shows that 0.2.1 fixes the summary mirroring and does not regress anything. Outputs and grades: `results/iteration-4/`.

A second external Luna round (same model, `low`, one fresh agent per version, same 22 assertions) put both versions side by side:

| | 0.2.1 | 0.2.0 (rerun) | No skill (first round) |
|---|---|---|---|
| churn-chart-for-cfo | 6/8 | 6/8 | 4/8 |
| fix-confusing-slide | 7/7 | 6/7 | 5/7 |
| exec-deck-storyline-pt | 6/7 | 6/7 | 4/7 |
| **Total** | **19/22** | **18/22** | **13/22** |

One point is within run-to-run noise: 0.2.0 itself scored 17 in the first round and 18 in the second. The signal per rule:

| Rule | Luna, 0.2.0 (two runs) | Luna, 0.2.1 | Reading |
|---|---|---|---|
| No gridlines | Failed twice | Passed | The removed exception helped |
| Ask in the slide text | Failed, then passed | Passed | Unclear |
| Biggest problem first | Failed, then passed | Passed | Unclear |
| Title names the June price increase | Failed twice | Failed | The 0.2.1 wording did not land |
| Summary mirrors the titles | Failed, then passed | Failed | Unclear |

0.2.1 also labelled only the highlighted line, leaving the grey ones unnamed. Neither version flagged the savings figure that does not reconcile.

0.2.2 sharpens the rules that still slipped:

- The title example now names an event in another domain ("Support tickets doubled after the March release"), and the final check asks for the event in the title.
- Every series gets a direct label, grey ones included.
- The reconciliation check says to recompute every total, saving or growth figure from its inputs.
- The abstract "mirror the titles" rule became a short deck skeleton whose summary bullets are the later titles. The wording alone ("one bullet per later slide") still failed once on Claude Haiku at low.
- The Big Idea template asks for the concrete ask, with its amount or date.

Regression on Claude Haiku at reasoning effort `low` with 0.2.2: churn 8/8 and slide 7/7. With the skeleton, the deck mirrored the titles in 3 of 3 runs, and all three flagged that the savings figure does not reconcile. One of the three left the €180k amount out of the Big Idea, which led to the last template change (not yet rerun). Outputs and grades: `results/iteration-5/`.

0.2.2 is 146 lines and about 1,290 words, against 134 lines and 1,125 words for 0.2.0.

### 0.2.3 draft (branch `skill-023`)

Structural nudges for the gaps Luna left open, about 30 more words: a `Check` line in the context block that recomputes each total, saving or growth from its parts before writing; the deck skeleton now says "last slide included"; and two final-check items, one for a direct label on every series and one for the ask in the slide text itself. Regression on Claude Haiku at `low`: 22/22, with the Check line filled in all three runs and the savings mismatch flagged in the deck. Outputs: `results/iteration-6/`. Not yet run on Luna.

### Luna, three runs per arm (0.2.2 against 0.2.0 and a fresh control)

External run: nine fresh gpt-6-luna agents at reasoning effort `low`, three per arm, each running the three scenarios in order, graded with the same strict reading as the earlier Luna rounds.

| Arm | Mean /22 | Range /22 | Mean without method-format /18 | Range /18 |
|---|---|---|---|---|
| 0.2.2 | 19.3 | 19 to 20 | 16.3 | 16 to 17 |
| 0.2.0 | 15.0 | 13 to 17 | 13.3 | 12 to 15 |
| No skill | 12.7 | 12 to 13 | 12.7 | 12 to 13 |

The worst 0.2.2 run beat the best 0.2.0 run. Runs passing each rule, out of three:

| Rule | 0.2.2 | 0.2.0 | No skill |
|---|---|---|---|
| Title names the June price increase | 3 | 0 | 1 |
| No gridlines | 2 | 0 | 0 |
| Ask in the slide text | 2 | 2 | 3 |
| Biggest problem first | 3 | 1 | 0 |
| Summary mirrors the later titles in order | 1 | 0 | 0 |
| Every series labelled directly | 1 | 0 | 0 |

Still open on 0.2.2: one deck left the last slide out of the summary and another reordered it, two churn charts left the grey lines unlabelled (one with a legend), one slide used two accents, one churn reply put the rollback ask outside the slide text, and one run misstated a June value. None of the nine decks flagged that €0.90 × 2.1M is about €1.89M rather than €1.4M, so the recompute instruction in the final check does not reach Luna. Every 0.2.x change was motivated by these three scenarios, so the next useful test is a set of new scenarios the skill was not tuned on.

## Iteration 3 (paired control groups)

Skill revised for verbosity and duplication before this run: 6,504 to 4,781 words (26% fewer), SKILL.md from 164 to 134 lines. Models: `claude-sonnet-5-5` and `claude-haiku-5-5`, both arms at reasoning effort `xhigh`.

| Scenario | Sonnet, skill | Sonnet, control | Haiku, skill | Haiku, control |
|---|---|---|---|---|
| churn-chart-for-cfo | 8/8 | 4/8 | 8/8 | 5/8 |
| fix-confusing-slide | 7/7 | 5/7 | 7/7 | 7/7 |
| exec-deck-storyline-pt | 7/7 | 5/7 | 7/7 | 5/7 |
| **Total** | **22/22** | **14/22** | **22/22** | **17/22** |
| Without the 4 method-format assertions | 18/18 | 14/18 | 18/18 | 16/18 |
| Average tokens per run | 121.0k | 94.9k | 128.1k | 100.1k |
| Average seconds per run | 289 | 145 | 214 | 125 |

What the control groups missed:

- Sonnet's churn chart kept a topic title ("Monthly churn rate by plan, 2025"), light gridlines and no axis titles.
- Sonnet's redesigned slide used navy and orange as two competing accents.
- Haiku's churn chart had an action title but kept gridlines and had no axis titles.
- Both controls skipped the Big Idea and wrote executive summaries that did not mirror the slide titles.

Both control groups were strong on the basics (no pies, no dual axes, direct labels, causation caveats), so the skill's gain is in the last mile: takeaway titles, a single accent, removed gridlines, axis titles and deck structure. The skill costs about 27% more tokens and roughly twice the time, mostly spent reading references and running the final check.

Outputs: `results/iteration-3/`, grades: `results/iteration-3/grading.json`.

## Claude Haiku at medium reasoning (same scenarios, same skill version)

A weaker setting: `claude-haiku-5-5` at reasoning effort `medium` in both arms, with the iteration 3 prompts unchanged apart from the output folder.

| Scenario | Haiku medium, skill | Haiku medium, control |
|---|---|---|
| churn-chart-for-cfo | 8/8 | 6/8 |
| fix-confusing-slide | 7/7 | 5/7 |
| exec-deck-storyline-pt | 6/7 | 5/7 |
| **Total** | **21/22** | **16/22** |
| Without the 4 method-format assertions | 18/18 | 16/18 |

The skill run lost one point because its Big Idea sentence left out the €180k ask, which sat on the Ask line instead. The control kept gridlines on the churn chart, wrote a slide subtitle saying revenue stayed between $4.2M and $4.6M when Q1 2024 was $4.1M, skipped the Big Idea and wrote an executive summary that did not mirror the slide titles. Outputs: `results/iteration-3/*/with_skill_haiku_medium/` and `*/without_skill_haiku_medium/`.

## Codex (same scenarios, same skill version)

Codex CLI 0.166.0-alpha (`gpt-6-astra`, reasoning effort `xhigh`), run from the Codex desktop app on Windows. An orchestrating thread spawned seven fresh subagents (three with the skill, three controls that were never told about the skill folder, and one for the banner texture), at most three at a time. Token counts were not exposed.

| Scenario | Codex, skill | Codex, control |
|---|---|---|
| churn-chart-for-cfo | 8/8 | 5/8 |
| fix-confusing-slide | 7/7 | 6/7 |
| exec-deck-storyline-pt | 7/7 | 5/7 |
| **Total** | **22/22** | **16/22** |
| Without the 4 method-format assertions | 18/18 | 15/18 |
| Elapsed time per run (approx.) | 2m 43s to 4m 59s | 1m 57s to 3m 25s |

The Codex control kept light gridlines, colored Enterprise brown instead of grey, used blue and orange as two accents on the redesigned slide, skipped the Big Idea, and wrote an executive summary that did not mirror the slide titles. Outputs: `results/codex/`.

## Iteration 2 (targeted re-runs after fixes)

| Scenario | Configuration | Result |
|---|---|---|
| exec-deck-storyline-pt | Skill, Haiku | 7/7 (was 6/7). Slide 1 bullets repeat the titles of slides 2 to 5 in order. |
| churn-chart-for-cfo | Skill, Sonnet | 8/8 (was 7/8). No second chart skill loaded; 124k tokens against 145k. |

## Iteration 1 (first version)

| Scenario | Sonnet, skill | Haiku, skill | Sonnet, control |
|---|---|---|---|
| churn-chart-for-cfo | 7/8 | 7/8 | 4/8 |
| fix-confusing-slide | 7/7 | 7/7 | 5/7 |
| exec-deck-storyline-pt | 6/7 | 6/7 | 4/7 |
| **Total** | **20/22** | **20/22** | **13/22** |

It surfaced two gaps that were then fixed. No configuration made the executive summary mirror the slide titles, because that guidance sat only in a reference file. And a sentence inviting a separate chart skill made runs load it, adding about 30% more tokens. The "no gridlines" assertion also failed everywhere because the first version allowed light gridlines, so the declutter step was tightened.
