# Training Roadmap

## Default Sequence

The project follows the four-stage order emphasized by the source skill and reference notes:

1. Reasoning RL
2. Agentic RL
3. General RL
4. On-Policy Cross-Stage Distillation

## Stage 1: Reasoning RL

Use this when the task centers on verifiable reasoning quality in math, science, code reasoning, or tool-integrated reasoning.

Key choices:

- keep rewards outcome-based and domain-verified
- prefer on-policy training here
- stabilize sparse or routed components before RL
- avoid letting one domain dominate the mixture

## Stage 2: Agentic RL

This is the center of the repository's design.

Key choices:

- decouple rollouts from training
- optimize only model-generated tokens
- use executable environments
- preserve exact generation traces
- filter stale and corrupted samples

## Stage 3: General RL

Use this for broader assistant behavior once specialized agent competence exists.

Reward families should cover:

- foundational correctness
- emotional intelligence
- task-specific quality

The source guidance suggests combining rule-based, outcome-model, and generative-model signals instead of betting on just one.

## Stage 4: Cross-Stage Distillation

Use this to recover capabilities weakened by later RL stages.

Key choices:

- keep teacher checkpoints from earlier stages
- sample prompts from earlier-stage distributions
- distill on-policy
- treat this as recovery, not replacement

## Evaluation Priorities Across Stages

- executable success before style polish
- tail-latency visibility for long rollouts
- failure-reason logging
- reward-hacking audits
- regression checks against earlier-stage capabilities

