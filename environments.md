# Environment Patterns

## First Principle

The environment must be specified before the optimizer. Every domain blueprint in this repository uses the same core fields:

- task unit
- initial state
- action space
- transition source
- terminal condition
- reward sources
- anti-cheat checks

## SWE

Best for:

- issue-to-PR tasks
- code-fixing agents
- real repository workflows

Backbone signals:

- executable test success
- fail-to-pass and pass-to-pass tracking
- diff relevance

Primary risks:

- rewarding irrelevant code changes
- infra failures masquerading as learning signal
- stale trajectories spanning too many policy versions

## Terminal

Best for:

- DevOps workflows
- shell-heavy task execution
- process and filesystem management

Backbone signals:

- machine-checkable test scripts
- reproducible container state
- exploit-resistance rubrics

Primary risks:

- brittle task specifications
- environment flakes
- accidental reward for unsafe shortcuts

## Search

Best for:

- multi-hop research tasks
- browse-and-synthesize agents
- evidence-grounded answer generation

Backbone signals:

- verified answer correctness
- evidence consistency
- tool-use necessity

Primary risks:

- context sprawl
- judge variability
- tasks solvable without retrieval

## Structured Generation

Best for:

- HTML slides
- UI layouts
- renderable structured artifacts

Backbone signals:

- static validity
- runtime geometry
- perceptual quality

Primary risks:

- whitespace or truncation exploits
- over-optimizing shallow metrics
- unstable perceptual evaluation

