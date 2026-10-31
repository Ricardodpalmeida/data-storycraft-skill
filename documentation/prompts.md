# Prompts

The exact text each benchmark run received, copied from the run logs. Local paths are replaced by placeholders; nothing else was edited.

| Placeholder | Stands for |
|---|---|
| `<skill>` | The skill folder, `skill/data-storycraft` in this repository |
| `<workspace>` | The benchmark workspace: `inputs/` plus one output folder per run |
| `<repo>` | The local clone of this repository |
| `<skill-draft-1>`, `<skill-draft-2>` | Earlier working copies of the skill, used in iterations 1 and 2 |
| `<python>` | The Python interpreter on the Windows machine that ran Codex |

Models, reasoning levels and the rest of the protocol are in [evaluation.md](evaluation.md).

## Claude: control vs with skill

Each run was a fresh subagent that received one of these prompts and nothing else. Claude Sonnet and Claude Haiku received the same text; only the output folder changes (`with_skill_haiku`, `without_skill_haiku`).

Apart from the output folder, the two arms differ in three places: the skill line, the extra `notes.md` output and the closing instruction. Below, lines marked `-` appear only in the control prompt and lines marked `+` only in the skill prompt (churn scenario shown; the other two follow the same pattern).

```diff
 Execute this task as if a real user asked it.
 
+- Skill path: <skill> (read SKILL.md first and follow it; open the reference files it points to only when needed; do not modify the skill)
 - Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
 - Input files: <workspace>/inputs/churn_by_plan.csv (read-only)
-- Save outputs to: <workspace>/iteration-3/churn-chart-for-cfo/without_skill/outputs/
-- Outputs to save: the chart PNG, any script, and your final reply to the user as response.md.
+- Save outputs to: <workspace>/iteration-3/churn-chart-for-cfo/with_skill/outputs/
+- Outputs to save: the chart PNG, any script, your final reply to the user as response.md, and notes.md listing every skill file you read, in order.
 
-Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them. Do not read anything under <repo>, <skill-draft-2> or <skill-draft-1>, and do not load any skill.
+Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them.
```

| | With skill | Control |
|---|---|---|
| Skill access | Reads `SKILL.md` first and follows it, opens references only when needed, never modifies the skill | Told not to read the skill folders and not to load any skill |
| Extra output | `notes.md` listing every skill file read, in order, so loading can be audited | None |
| Everything else | Same user message, same inputs, same output list, same "do not ask questions" rule | Same |

The control prompt names three folders because two earlier drafts of the skill (`<skill-draft-1>`, `<skill-draft-2>`) were still on disk during the runs.

### Full prompts, iteration 3

<details>
<summary><code>churn-chart-for-cfo</code>, with skill</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill> (read SKILL.md first and follow it; open the reference files it points to only when needed; do not modify the skill)
- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only)
- Save outputs to: <workspace>/iteration-3/churn-chart-for-cfo/with_skill/outputs/
- Outputs to save: the chart PNG, any script, your final reply to the user as response.md, and notes.md listing every skill file you read, in order.

Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary><code>churn-chart-for-cfo</code>, control</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only)
- Save outputs to: <workspace>/iteration-3/churn-chart-for-cfo/without_skill/outputs/
- Outputs to save: the chart PNG, any script, and your final reply to the user as response.md.

Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them. Do not read anything under <repo>, <skill-draft-2> or <skill-draft-1>, and do not load any skill.
```

</details>

<details>
<summary><code>fix-confusing-slide</code>, with skill</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill> (read SKILL.md first and follow it; open the reference files it points to only when needed; do not modify the skill)
- Task (user's words): "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
- Input files: <workspace>/inputs/bad_slide.py and <workspace>/inputs/bad_slide.png (read-only)
- Save outputs to: <workspace>/iteration-3/fix-confusing-slide/with_skill/outputs/
- Outputs to save: the fixed PNG, the fixed script, your final reply to the user as response.md, and notes.md listing every skill file you read, in order.

Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary><code>fix-confusing-slide</code>, control</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words): "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
- Input files: <workspace>/inputs/bad_slide.py and <workspace>/inputs/bad_slide.png (read-only)
- Save outputs to: <workspace>/iteration-3/fix-confusing-slide/without_skill/outputs/
- Outputs to save: the fixed PNG, the fixed script, and your final reply to the user as response.md.

Use Python/matplotlib. Do not ask questions; make reasonable assumptions and state them. Do not read anything under <repo>, <skill-draft-2> or <skill-draft-1>, and do not load any skill.
```

</details>

<details>
<summary><code>exec-deck-storyline-pt</code>, with skill</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill> (read SKILL.md first and follow it; open the reference files it points to only when needed; do not modify the skill)
- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-3/exec-deck-storyline-pt/with_skill/outputs/
- Outputs to save: deck.md, your final reply to the user as response.md, and notes.md listing every skill file you read, in order.

Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary><code>exec-deck-storyline-pt</code>, control</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-3/exec-deck-storyline-pt/without_skill/outputs/
- Outputs to save: deck.md and your final reply to the user as response.md.

Do not ask questions; make reasonable assumptions and state them. Do not read anything under <repo>, <skill-draft-2> or <skill-draft-1>, and do not load any skill.
```

</details>

### Claude Haiku at medium reasoning

The Haiku medium round reused the iteration 3 prompts word for word. Only the output folder changed, to `with_skill_haiku_medium` and `without_skill_haiku_medium`, and each run set its reasoning effort to `medium`.

## Codex: one orchestrator prompt

Codex ran the same three tasks from a single prompt pasted into a fresh Codex desktop thread. The orchestrating thread did no task work: it spawned seven subagents in fresh contexts, three with the skill, three controls and one for the README banner texture, at most three at a time. The arm-specific text is the two quoted "extra instruction" paragraphs; control subagents never received the skill path.

```text
You are orchestrating a benchmark. Do not do any of the tasks yourself, and do not open the skill folder yourself. Spawn one subagent per job below, all in parallel, each in a fresh context, and pass each subagent exactly the instructions written for it. Control subagents must never be told about the skill folder or its path.

Shared settings for every subagent:
- Workspace root: <workspace>
- Do not ask questions; make reasonable assumptions and state them in the reply.
- For charts, use Python with matplotlib at <python>
- Write only inside your own output folder. If the folder already has files from an earlier attempt (prompt.txt, events.jsonl, stderr.txt, timing.json), leave them alone.

Skill subagents get this extra instruction:
"Before starting, read <workspace>\skill\data-storycraft\SKILL.md and follow it. Open its reference files only when needed and do not modify the skill. Also write notes.md in your output folder listing every skill file you read, in order."

Control subagents get this extra instruction:
"Do not open anything under <workspace>\skill and do not use any skill."

Tasks (each runs twice: once as a skill subagent, once as a control subagent):

TASK churn. Output folders: runs\churn-chart-for-cfo\with_skill\ and runs\churn-chart-for-cfo\without_skill\
User message: "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
Input: inputs\churn_by_plan.csv (read-only). Save the chart PNG, the script, and the reply to the user as response.md.

TASK slide. Output folders: runs\fix-confusing-slide\with_skill\ and runs\fix-confusing-slide\without_skill\
User message: "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
Inputs: inputs\bad_slide.py and inputs\bad_slide.png (read-only). Save the fixed PNG, the fixed script, and the reply as response.md.

TASK deck. Output folders: runs\exec-deck-storyline-pt\with_skill\ and runs\exec-deck-storyline-pt\without_skill\
User message: "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
Input: inputs\pilot_findings.md (read-only). Save deck.md and the reply as response.md.

Seventh subagent, banner. Output folder: banner\
"Use your image generation tool (not code, not SVG, not matplotlib) to create two background plates for a GitHub README header about a skill that turns cluttered business charts into clear ones. Save them as banner\paper-light.png and banner\paper-dark.png, landscape, at the widest size the tool supports.
paper-light.png: a flat, top-down, evenly lit macro photograph of uncoated off-white report paper, the kind used for printed annual reports. Faint fibres and a very slight tooth. In the right half, a ghost of offset-printed grey halftone dots forming the faint, out-of-focus impression of a line chart showing through from the back of the sheet. No legible text, numbers, logos, hands, desk, object shadows or vignette, and no colour cast beyond a neutral warm white.
paper-dark.png: the same composition on matte charcoal card stock (near-black, neutral, not blue), with the halftone ghost in dark grey.
Both sit behind large typography, so keep contrast low and detail even across the frame. Avoid glow, bokeh, gradients, sparkles, 3D renders, illustrations and anything that looks like a stock image."

When all seven subagents have finished:
1. Check that each output folder has its required files. If a subagent failed, rerun that one job once.
2. Do not judge or edit the outputs.
3. Write runs\summary.md with one line per job: name, completed or failed, elapsed time, and tokens used if you can see them.
4. Reply with "done" and the summary.
```

## Earlier iterations

Iterations 1 and 2 used the same structure with slightly different wording, with the skill at `<skill-draft-1>` and then `<skill-draft-2>`. They are kept for completeness.

<details>
<summary>Iteration 1, <code>churn-chart-for-cfo</code>, with skill, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/churn-chart-for-cfo/with_skill/outputs/
- Outputs to save: the chart PNG, any script you wrote, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Use Python/matplotlib (already installed; pip install --break-system-packages if something is missing). Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>churn-chart-for-cfo</code>, with skill, Haiku</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/churn-chart-for-cfo/with_skill_haiku/outputs/
- Outputs to save: the chart PNG, any script you wrote, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Use Python/matplotlib (already installed; pip install --break-system-packages if something is missing). Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>churn-chart-for-cfo</code>, control, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/churn-chart-for-cfo/without_skill/outputs/
- Outputs to save: the chart PNG, any script you wrote, and your final reply to the user saved as response.md.

Use Python/matplotlib (already installed; pip install --break-system-packages if something is missing). Do not ask questions; make reasonable assumptions and state them. Do not read anything under <skill-draft-1>.
```

</details>

<details>
<summary>Iteration 1, <code>fix-confusing-slide</code>, with skill, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words): "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
- Input files: <workspace>/inputs/bad_slide.py and <workspace>/inputs/bad_slide.png (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/fix-confusing-slide/with_skill/outputs/
- Outputs to save: the fixed PNG, the fixed script, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Use Python/matplotlib (already installed). Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>fix-confusing-slide</code>, with skill, Haiku</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words): "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
- Input files: <workspace>/inputs/bad_slide.py and <workspace>/inputs/bad_slide.png (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/fix-confusing-slide/with_skill_haiku/outputs/
- Outputs to save: the fixed PNG, the fixed script, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Use Python/matplotlib (already installed). Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>fix-confusing-slide</code>, control, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words): "My director says this slide is confusing. Here's the script that generates it (bad_slide.py) and the current output (bad_slide.png). What's wrong with it? Fix it and give me the new PNG. It's for the quarterly business review with sales leadership; the point is that adding reps hasn't grown revenue."
- Input files: <workspace>/inputs/bad_slide.py and <workspace>/inputs/bad_slide.png (read-only, do not modify)
- Save outputs to: <workspace>/iteration-1/fix-confusing-slide/without_skill/outputs/
- Outputs to save: the fixed PNG, the fixed script, and your final reply to the user saved as response.md.

Use Python/matplotlib (already installed). Do not ask questions; make reasonable assumptions and state them. Do not read anything under <skill-draft-1>.
```

</details>

<details>
<summary>Iteration 1, <code>exec-deck-storyline-pt</code>, with skill, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-1/exec-deck-storyline-pt/with_skill/outputs/
- Outputs to save: deck.md, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>exec-deck-storyline-pt</code>, with skill, Haiku</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-1> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-1/exec-deck-storyline-pt/with_skill_haiku/outputs/
- Outputs to save: deck.md, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 1, <code>exec-deck-storyline-pt</code>, control, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-1/exec-deck-storyline-pt/without_skill/outputs/
- Outputs to save: deck.md, and your final reply to the user saved as response.md.

Do not ask questions; make reasonable assumptions and state them. Do not read anything under <skill-draft-1>.
```

</details>

<details>
<summary>Iteration 2, <code>churn-chart-for-cfo</code>, with skill, Sonnet</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-2> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words): "I've attached churn_by_plan.csv. Next week I'm presenting to our CFO and I want to show that the June price increase on the Pro plan is driving churn, and that we should roll it back for existing customers. Make me the chart (PNG) and tell me what to put on the slide."
- Input files: <workspace>/inputs/churn_by_plan.csv (read-only, do not modify)
- Save outputs to: <workspace>/iteration-2/churn-chart-for-cfo/with_skill/outputs/
- Outputs to save: the chart PNG, any script you wrote, and your final reply to the user saved as response.md. Also write notes.md listing every skill file you read (from any skill), in order.

Use Python/matplotlib (already installed). Do not ask questions; make reasonable assumptions and state them.
```

</details>

<details>
<summary>Iteration 2, <code>exec-deck-storyline-pt</code>, with skill, Haiku</summary>

```text
Execute this task as if a real user asked it.

- Skill path: <skill-draft-2> (read SKILL.md first and follow it; open the reference files it points to only when needed)
- Task (user's words, Portuguese): "Tenho as notas da análise do piloto em pilot_findings.md. Estrutura-me um deck de 6 slides para o comité executivo aprovar o rollout. Só preciso da estrutura e do texto de cada slide, sem design. Guarda em deck.md."
- Input files: <workspace>/inputs/pilot_findings.md (read-only)
- Save outputs to: <workspace>/iteration-2/exec-deck-storyline-pt/with_skill_haiku/outputs/
- Outputs to save: deck.md, and your final reply to the user saved as response.md. Also write notes.md listing which skill files you read, in order.

Do not ask questions; make reasonable assumptions and state them.
```

</details>
