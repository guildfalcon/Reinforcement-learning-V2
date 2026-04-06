# Agentic Reinforcement

Agentic Reinforcement is a well-structured starter repository for designing long-horizon reinforcement-learning systems for tool-using language agents. It turns the ideas in the provided `SKILL.md` and `readme.md` into a usable GitHub project with docs, code primitives, examples, and tests.

The project is intentionally opinionated:

- verifiable environments come before optimizer choices
- asynchronous rollout and training decoupling are first-class
- token-in-token-out (TITO) trajectory capture is treated as a stability requirement
- sample staleness, reward hacking, and infrastructure noise are explicit design concerns
- staged RL is preferred over collapsing all training objectives into one run

## Why This Repo Exists

The source `readme.md` captures the high-level pitch well, but it is short, partially truncated, and missing the implementation-facing structure needed for a serious repository. The source `SKILL.md` is much richer: it defines the workflow, environment specs, architecture primitives, reward design rules, and the distinction between paper-grounded guidance and extrapolation.

This repository turns that material into:

- a documented project skeleton
- reusable Python data models for RL system design
- default blueprints for SWE, terminal, search, and structured generation
- a small CLI to render planning-ready blueprints
- tests to keep the starter package honest

## Core Ideas

### 1. Stage The Training

The default roadmap follows four stages:

1. Reasoning RL
2. Agentic RL
3. General RL
4. On-Policy Cross-Stage Distillation

### 2. Design The Environment Before The Loss

Each environment should define:

- task unit
- initial state
- action space
- transition source
- terminal condition
- reward sources
- anti-cheat checks

### 3. Treat Async RL As A Systems Problem

This repository assumes a paper-grounded agentic RL stack built around:

- multi-task rollout orchestrator
- rollout workers
- inference router
- TITO gateway
- trainer
- verifier and evaluator services
- policy version ledger
- fault monitor

### 4. Keep Claims Honest

The docs deliberately separate:

- paper-grounded claims
- reasonable extensions
- open questions

That keeps the repo useful for research planning without pretending the paper resolved every engineering detail.

## Quick Start

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .[dev]
pytest
python -m agentic_reinforcement.cli blueprint --domain swe
```

## Project Structure

```text
.
|-- .github/workflows/ci.yml
|-- docs/
|   |-- architecture.md
|   |-- environments.md
|   |-- source-analysis.md
|   `-- training-roadmap.md
|-- examples/
|   `-- swe_blueprint.json
|-- src/agentic_reinforcement/
|   |-- __init__.py
|   |-- blueprints.py
|   |-- cli.py
|   |-- models.py
|   `-- rendering.py
|-- tests/
|   |-- test_blueprints.py
|   `-- test_cli.py
|-- CONTRIBUTING.md
|-- LICENSE
`-- pyproject.toml
```

## CLI Example

Render a paper-aligned planning blueprint for one domain:

```bash
agentic-rl blueprint --domain search
```

Render the default repository-wide roadmap:

```bash
agentic-rl roadmap
```

## Documentation

- [Source Analysis](docs/source-analysis.md)
- [Architecture](docs/architecture.md)
- [Environment Patterns](docs/environments.md)
- [Training Roadmap](docs/training-roadmap.md)

## What This Repository Is And Is Not

This repository is:

- a strong GitHub-ready starter for agentic RL system design
- a compact implementation of reusable planning primitives
- a clean foundation for a larger research or engineering codebase

This repository is not:

- a full distributed trainer
- a production rollout cluster
- a claim that all thresholds and algorithms are fully specified by the source documents

## Roadmap

- add JSON or TOML config loading for blueprint composition
- add architecture export to Mermaid
- add benchmark fixtures for latency and staleness simulations
- add richer verifier interfaces for domain-specific tasks

## Attribution

This project is inspired by the provided `SKILL.md` guidance and the GLM-5 paper framing it references. The repository content separates source-backed recommendations from implementation-friendly extensions where appropriate.
