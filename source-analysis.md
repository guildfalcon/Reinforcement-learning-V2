# Source Analysis

## What The Provided `readme.md` Contributes

The supplied `readme.md` is useful as a positioning document. It clearly states the theme of the project:

- long-horizon language-agent RL
- GLM-5 as the conceptual anchor
- executable environments over preference-only tuning
- asynchronous rollouts, TITO, and reward-hacking defenses as key differentiators

That makes it strong as an opening pitch.

## What The Provided `readme.md` Is Missing

The file is short and appears incomplete:

- it ends mid quick-start block
- the emoji headings are garbled, which suggests an encoding issue
- it does not define a repository structure
- it does not explain how a user should translate the ideas into code
- it does not separate paper-backed claims from implementation guesses

So it is a good abstract, but not yet a full GitHub project README.

## What The Provided `SKILL.md` Adds

The `SKILL.md` is the real foundation. It contributes the engineering logic needed to turn the pitch into a repository:

- a required order of reasoning
- stage selection across Reasoning RL, Agentic RL, General RL, and Distillation
- a concrete environment-spec template
- paper-grounded architecture components
- explicit off-policy controls for async RL
- reward design principles by domain
- guidance on filtering corrupted samples
- a strong stance on TITO and context management
- a discipline for labeling paper-grounded claims vs reasonable extensions vs open questions

## Main Synthesis

The two files fit together in a complementary way:

- `readme.md` explains why the project should exist
- `SKILL.md` explains how the project should be structured and reasoned about

That is why this repository uses the README material for the public-facing story, but uses the skill material to drive the actual package, docs, and architecture.

## Repository Design Decisions Made From That Analysis

### Decision 1

The project centers on blueprints, not a fake production trainer.

Reason:
The source material is strongest on architecture, evaluation, environment design, and training workflow. Pretending to ship a complete distributed trainer would overstate what the documents actually specify.

### Decision 2

The package exposes explicit data models for environment specs, objectives, architecture, and evidence buckets.

Reason:
The skill repeatedly emphasizes structure and ordering. Representing that structure in code makes the repo reusable instead of purely descriptive.

### Decision 3

The docs separate paper-grounded guidance from extensions and open questions.

Reason:
The skill is unusually explicit that rigor matters here. The repository preserves that discipline.

### Decision 4

The project includes domain blueprints for SWE, terminal, search, and structured generation.

Reason:
Those are the four environment families emphasized in the source material, so they should appear directly in the starter project.

## Practical Outcome

The final repository is intentionally a serious starter kit:

- polished enough for GitHub
- honest about the underlying source material
- structured for extension into a real research codebase
- useful on day one for planning agentic RL systems

