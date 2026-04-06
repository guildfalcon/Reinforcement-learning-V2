---
name: agentic-reinforcement
description: Design, critique, or implement reinforcement-learning systems for long-horizon language agents using the GLM-5 asynchronous RL recipe. Use when Codex needs to plan agentic RL infrastructure, convert tasks into verifiable environments, choose GRPO/PPO-style policy optimization, control asynchronous off-policy bias, prevent reward hacking, manage long contexts, or recover earlier capabilities with cross-stage distillation in coding, terminal, search, reasoning, or structured-generation agents.
---

# Agentic Reinforcement

## Overview

Ground decisions in the GLM-5 paper, "GLM-5: from Vibe Coding to Agentic Engineering" (arXiv:2602.15763v2), and treat it as an engineering recipe for reinforcement learning in tool-using, long-horizon agents rather than as a generic RLHF note.

Prefer systems that maximize verified environment feedback, asynchronous rollout throughput, and optimization stability over elegant but hard-to-operate RL variants.

Read [references/glm5-foundation.md](references/glm5-foundation.md) when you need section-by-section paper details, environment recipes, or paper-grounded terminology.

## Work In This Order

1. Classify the request into one or more RL stages: Reasoning RL, Agentic RL, General RL, or Cross-Stage Distillation.
2. Define a verifiable environment before proposing an algorithm.
3. Specify the rollout architecture, especially where inference, orchestration, verification, and training are decoupled.
4. Choose the policy objective and off-policy controls.
5. Design rewards and sample filters.
6. Define stability guardrails, throughput guardrails, and evaluation gates.
7. Separate paper-grounded recommendations from your extrapolations.

If the user asks for a complete training recipe, present it in that same order.

## Start From These Operating Beliefs

- Treat verifiable environments as the center of the system. In GLM-5, real gains come from executable SWE, terminal, search, and rendering environments, not from preference labels alone.
- Treat long-horizon agent RL as a systems problem before it is an optimization problem. Throughput, tail latency, version skew, cache locality, and environment crashes materially change learning quality.
- Prefer asynchronous rollout-training decoupling for agent tasks. The paper is explicit that naive synchronous RL wastes GPUs during long rollouts.
- Preserve exact token trajectories. GLM-5 treats Token-in-Token-out as a core stability mechanism, not an implementation detail.
- Accept limited off-policy bias only when it buys tractable large-scale training, then control it with clipping, sample dropping, and version-age filters.
- Sequence stages instead of collapsing all objectives into one monolithic RL run. GLM-5 uses Reasoning RL, then Agentic RL, then General RL, then On-Policy Cross-Stage Distillation.
- Assume reward hacking will happen anywhere a signal can be gamed. Build evaluators that execute, render, or verify state instead of trusting surface-form heuristics.
- Optimize for tail latency in rollouts, not just average throughput. One straggling long trajectory can determine wall-clock progress.

## Map The Request To The Right RL Stage

### Reasoning RL

Use this stage when the task is primarily about verifiable reasoning quality in math, science, code reasoning, or tool-integrated reasoning.

Default to the paper's reasoning recipe:

- Start from a GRPO-style backbone.
- Use IcePop-style training/inference mismatch handling.
- Remove unnecessary KL regularization if the goal is faster improvement and the stability budget allows it.
- Keep training on-policy.
- Use binary outcome rewards from domain-specific judges or evaluation systems.
- Mix domains instead of overfitting one narrow reasoning stream.

If sparse attention or retrieval indexers are involved, treat deterministic routing or top-k behavior as mandatory for RL stability.

### Agentic RL

Use this stage when the task involves coding agents, terminal agents, search agents, browser agents, or any tool-using system that learns through multi-turn interaction with an environment.

Default to the paper's agentic recipe:

- Decouple generation and training through a central orchestrator.
- Preserve token-exact rollout records with a TITO gateway.
- Use clipped token-level importance control to tolerate asynchronous off-policy data.
- Record policy versions during trajectory generation and drop stale samples.
- Build large numbers of executable, grounded environments.
- Optimize latency and cache locality as first-class training concerns.

### General RL

Use this stage when the goal is broader assistant quality rather than just problem solving in a specific environment.

Organize the reward system around the paper's three dimensions:

- Foundational correctness
- Emotional intelligence
- Task-specific quality

Blend three signal families instead of relying on only one:

- Rule-based rewards for precise constraints
- Outcome reward models for efficiency
- Generative reward models for robustness against shallow exploitation

If the user wants style or conversational naturalness improvements, include high-quality human responses as anchors rather than optimizing solely against model-generated comparisons.

### On-Policy Cross-Stage Distillation

Use this stage when a later RL phase weakens earlier capabilities, or when the user wants one model to retain reasoning sharpness while gaining agentic or general behavior.

Follow the paper's sequencing logic:

- Keep teacher checkpoints from earlier SFT or RL stages.
- Sample prompts from those earlier stage distributions.
- Distill on-policy against the teachers after the main RL stages.
- Present this as recovery and capability preservation, not as a substitute for the earlier RL stages.

If the user asks for a single-stage simplification, warn that the paper treats staged optimization plus recovery as one of the main defenses against catastrophic forgetting.

## Design The Environment Before The Loss

When asked to build or critique an RL setup, write the environment spec before naming the optimizer.

Include these fields:

- `task unit`: one issue, one terminal task, one search question, one renderable page, one dialog episode
- `initial state`: repo snapshot, Docker image, search tools, browser state, HTML scaffold, prompt pack
- `action space`: plain language, tool calls, shell actions, code edits, search/open/find/python, browser steps
- `transition source`: test execution, command output, web evidence, renderer output, verifier results
- `terminal condition`: success, failure, timeout, budget exhaustion, invalid state
- `reward sources`: binary pass/fail, rubric checks, geometric metrics, verifier decisions, human or model judgments
- `anti-cheat checks`: exploit detection, sandbox crash detection, hallucinated asset detection, duplicate-output checks

If the environment is not executable or verifiable, say so clearly and downgrade claims about RL effectiveness.

## Use These Environment Patterns From The Paper

### SWE Environments

Prefer this recipe when the user wants RL for real software engineering:

- Source tasks from real issue-PR pairs.
- Filter aggressively with rule-based and LLM-based quality checks.
- Preserve task type information such as bug fix, feature work, or refactor.
- Build the runtime environment automatically from the repository's real install and dependency setup.
- Generate executable test commands.
- Parse logs into Fail-to-Pass and Pass-to-Pass signals.
- Keep the task statement aligned with the test patch so the agent is not rewarded for irrelevant code changes.

Use this pattern when the user says things like "train on real repos," "make the coding agent robust," or "learn from actual software tasks."

### Terminal Environments

Prefer this recipe when the user wants shell-centric or DevOps-style agent training:

- Start from seed tasks grounded in real terminal workflows.
- Synthesize drafts at scale.
- Convert drafts into concrete Dockerized tasks with machine-checkable test scripts.
- Refine tasks against rubrics for build reliability, spec-test consistency, and exploit resistance.
- Keep only tasks that successfully self-validate.

Use this pattern when the task requires file operations, process management, package installs, build systems, or CLI debugging.

### Search Environments

Prefer this recipe when the user wants deep research or multi-hop browsing agents:

- Build or simulate a web knowledge graph from collected pages and trajectories.
- Generate questions that require multi-hop evidence chains.
- Filter out items solvable without tools.
- Filter out items solvable by a weak early agent in only a few steps.
- Run bidirectional verification on candidate answers and ground truth.
- Manage context explicitly once tool traces become long.

If the user asks about search-agent RL, always discuss context management and judge reliability. The paper shows that both materially affect performance.

### Structured Generation Environments

Prefer this recipe when the task involves HTML, slides, UI, or other renderable structured outputs:

- Evaluate the static output for syntax and declarative structure.
- Execute or render the output.
- Inspect runtime geometry, layout metrics, or execution properties.
- Add perceptual or composition-level signals only after the lower-level checks are trustworthy.
- Harden the evaluator against exploitative shortcuts.

Use this pattern when the user wants RL for layout quality, visual composition, or interactive artifact generation.

## Use A Paper-Grounded Agentic RL Architecture

When designing the system, default to the following components:

- `multi-task rollout orchestrator`: route tasks across workloads and keep generation decoupled from optimization
- `rollout workers`: run environments, tool loops, and task-specific logic
- `inference router`: serve generation requests and preserve placement or affinity decisions
- `TITO gateway`: capture exact token IDs, decoded token stream, and rollout metadata
- `trainer`: consume trajectory fragments and compute policy updates
- `verifier/evaluator services`: execute tests, parse logs, check answers, render layouts
- `policy version ledger`: record which model versions contributed to each trajectory
- `fault monitor`: detect unhealthy rollout servers and reroute retries

Explain the dataflow explicitly whenever the user asks for implementation or architecture help.

## Treat TITO As Non-Negotiable In Async RL

Prefer token-in-token-out over text-in-text-out whenever the trainer learns from streamed or truncated trajectories.

Protect against these failure modes:

- whitespace or normalization drift after re-tokenization
- shifted action boundaries
- mismatched truncation points
- corrupted correspondence between sampled actions and optimized tokens
- delayed or lossy reconstruction of streamed trajectories

If a proposed system only stores final text and re-tokenizes later, call out the risk directly. In the GLM-5 recipe, this is a structural instability source, not a minor bookkeeping problem.

## Control Off-Policy Bias The GLM-5 Way

When the user needs an asynchronous training objective, start from the paper's pragmatic strategy:

- reuse rollout-time log probabilities as the behavior proxy
- avoid historical checkpoint replay unless the user explicitly wants the added complexity
- compute token-level importance ratios against the current policy
- apply double-sided clipping or masking instead of trusting all tokens equally
- remove tokens that fall outside the trust region from gradient computation

Describe this as a controlled-bias trade: the system accepts some off-policy approximation to avoid impossible checkpoint bookkeeping during long rollouts.

Also enforce sample-age controls:

- log the policy versions involved in each trajectory
- drop trajectories whose oldest contributing version is too stale
- surface the staleness threshold as a tunable hyperparameter

## Filter Bad Samples Aggressively

Drop or quarantine samples for reasons that do not reflect model quality:

- environment crash
- sandbox collapse
- broken dependency install unrelated to the task
- renderer failure
- network or infra flake

For grouped methods such as GRPO, handle missing members deliberately:

- repeat valid samples only if enough of the group remains meaningful
- otherwise drop the group

State plainly that noisy execution failures are not useful "exploration"; they are corrupted supervision.

## Optimize Systems For Tail Latency

When the user asks how to scale rollouts, center the answer on tail latency.

Apply the paper's systems levers where relevant:

- use no-queue or low-queue serving
- provision enough distributed KV cache for bursty rollouts
- use FP8 inference when compatible with the deployment stack
- use multi-token prediction where small-batch decoding dominates
- disaggregate prefill and decode for multi-turn workloads
- keep rollout-level affinity so repeated prefixes reuse KV cache

If the proposal mixes prefills and decodes on the same long-horizon serving pool, flag the likely interference cost.

## Preserve Cache Locality Under Data Parallelism

If the system uses data parallel or multi-rank inference, keep all requests from the same rollout on the same rank whenever possible.

Prefer:

- stable rollout-to-rank mapping
- consistent hashing for affinity
- lightweight rebalancing only when needed

Avoid designs that force repeated cross-rank cache misses for every new agent turn.

## Harden Sparse Or Routed Components For RL

If the model uses sparse attention, retrieval indexers, or routers:

- prefer deterministic top-k selection in RL
- freeze unstable routing or indexer parameters unless there is strong evidence they can be trained safely
- treat training-inference consistency as a first-class stability requirement

This comes directly from the paper's DSA RL discussion: non-deterministic top-k behavior produced severe degradation and entropy collapse.

## Design Rewards As A Stack, Not A Scalar

If the user asks for a reward function, decompose it into layers.

For agentic coding or terminal tasks:

- use executable success or failure as the backbone
- add structured sub-signals only when they predict final task quality
- parse logs into meaningful state changes, not just string matches

For search tasks:

- verify answer correctness against evidence
- verify answer uniqueness and consistency
- standardize the judge prompt and judge model where reproducibility matters

For structured generation tasks:

- level 1: static validity and declarative constraints
- level 2: runtime geometry or rendering metrics
- level 3: perceptual or composition-level checks

Whenever possible, tell the user which layer is hardest to game and which layer is easiest to hack.

## Expect Reward Hacking And Close The Loops

When a reward seems easy to satisfy mechanically, assume the policy will discover the exploit.

Audit for the kinds of failure modes surfaced in the paper:

- hard truncation that improves a geometry metric while damaging content quality
- excessive whitespace or spacing manipulation
- duplicate artifacts that technically satisfy a count-based rule
- hallucinated assets that pass static checks but fail grounded verification

Strengthen the evaluator instead of only tweaking the loss.

## Manage Search-Agent Context Explicitly

If the task involves long browsing traces, propose context management as part of the inference design.

Start with the paper's approach:

- keep only the most recent rounds of reasoning, actions, and observations
- fold or summarize older observations
- discard the full tool-call history once a larger threshold is exceeded
- continue with a fresh context after the reset

Present this as a hierarchical context-management policy rather than as ad hoc summarization.

## Sequence Training Stages Explicitly

If the user asks for an end-to-end roadmap, default to this order:

1. Build or adapt the base model and long-context/tool-use priors.
2. Run Reasoning RL on verifiable reasoning domains.
3. Run Agentic RL on executable environments.
4. Run General RL for broader assistant quality.
5. Run On-Policy Cross-Stage Distillation to recover earlier strengths.

Do not collapse this into one mixed RL stage unless the user explicitly accepts the tradeoff.

## Produce One Of These Deliverables

### If Asked To Design A System

Return:

- stage selection
- environment specification
- architecture diagram or component list
- objective and clipping strategy
- reward stack
- filtering rules
- evaluation plan
- known failure modes
- paper-grounded components vs extrapolations

### If Asked To Critique An Existing RL Pipeline

Inspect for:

- missing verifiable environments
- synchronous rollout bottlenecks
- text-in-text-out reconstruction
- stale-sample drift
- non-deterministic routed components
- reward hacking exposure
- absent crash filtering
- absent cross-stage recovery
- no context-management plan for long-horizon search

### If Asked To Implement A Minimal Version

Keep the first version narrow:

- choose one domain
- build one executable environment type
- use one clear outcome reward
- preserve exact token trajectories
- add version-age filtering
- add environment-failure filtering
- benchmark end-to-end wall-clock efficiency before adding algorithmic complexity

## Keep Claims Honest

Separate recommendations into three buckets whenever rigor matters:

- `paper-grounded`: explicitly supported by GLM-5
- `reasonable extension`: consistent with the paper but not directly stated
- `open question`: plausible but unverified within the paper

Do this especially when the user asks for hyperparameters, exact thresholds, or implementation details that the paper only sketches qualitatively.

## Avoid These Failure Patterns

- Do not start with reward model architecture before defining the environment.
- Do not present preference optimization as a substitute for executable agent feedback when the task is agentic.
- Do not re-tokenize finalized text if the system can preserve exact token streams.
- Do not keep every asynchronous sample just because it is expensive to obtain.
- Do not trust non-deterministic sparse-selection operators in RL without testing stability.
- Do not rely on one reward channel when the output can be statically checked, executed, and perceptually judged.
- Do not ignore long-context degradation in browsing or tool-heavy agents.
- Do not claim the paper validated an idea unless it is actually described in [references/glm5-foundation.md](references/glm5-foundation.md).

## Reference Use

Read [references/glm5-foundation.md](references/glm5-foundation.md) when you need:

- the paper's stage-by-stage RL breakdown
- the exact motivation for TITO, double-sided token clipping, or DP-aware routing
- the paper's environment scaling patterns for SWE, terminal, search, or slides
- the reasoning behind context management and reward-hacking defenses

Stay concise in normal use. Load the reference only when the task needs deeper grounding.
