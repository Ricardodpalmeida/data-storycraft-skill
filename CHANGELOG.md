# Changelog

## 0.2.0 (2026-10-31)

- Renamed the method credit from "Distilled from" to "Inspired by".
- Cut verbosity and duplication: 26% fewer words across the skill, SKILL.md down to 134 lines. Each rule now lives in one place, and references only add what SKILL.md does not already say.
- Declutter step now removes gridlines by default.
- New benchmark round with paired control groups on Claude Sonnet, Claude Haiku and Codex (see `evals/RESULTS.md`).
- README with banner, before/after examples, benchmark chart, MIT-0 license and author references.
- Added `scripts/make_banner.py` and `scripts/make_bench_chart.py`.
- Removed the chapter labels from the references and the reference map.
- README before-and-after pairs are now real outputs, each from one model at one reasoning level, with and without the skill; runs and prompts in `evals/examples`. Replaces the illustrative charts and `scripts/make_examples.py`.
- New benchmark round on Claude Haiku at medium reasoning: 21/22 with the skill against 16/22 without.
- New `documentation/` folder: how the skill was built, the evaluation protocol with models and reasoning levels, and the exact prompts for every arm.
- Install guide for Claude Code, Claude.ai, Codex, GitHub Copilot, Pi, Hermes Agent and OpenClaw.
- README describes the synthetic test data and the trap each scenario hides.

## 0.1.0 (2026-10-31)

First release.

- SKILL.md with mode check, a six-step workflow checklist, rules, output templates for creating and reviewing, a matplotlib starting point and a final check loop.
- Ten reference files, one per topic, loaded only when a task needs them.
- Three evaluation scenarios with inputs, assertions and graded outputs (see `evals/RESULTS.md`).
- Changes from iteration 1 of the evals:
  - The executive summary must mirror the slide titles in order, and the deck must close by restating the ask.
  - Markers and value labels are kept only on the points the message references.
  - The skill no longer prompts loading a second chart skill. It only says how to resolve conflicts when one is already loaded.
