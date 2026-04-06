from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class RLStage(str, Enum):
    REASONING = "Reasoning RL"
    AGENTIC = "Agentic RL"
    GENERAL = "General RL"
    DISTILLATION = "On-Policy Cross-Stage Distillation"


class Domain(str, Enum):
    SWE = "swe"
    TERMINAL = "terminal"
    SEARCH = "search"
    STRUCTURED = "structured-generation"


@dataclass(slots=True)
class EnvironmentSpec:
    task_unit: str
    initial_state: str
    action_space: list[str]
    transition_source: list[str]
    terminal_condition: list[str]
    reward_sources: list[str]
    anti_cheat_checks: list[str]


@dataclass(slots=True)
class ObjectiveSpec:
    objective: str
    off_policy_controls: list[str]
    sample_filters: list[str]


@dataclass(slots=True)
class ArchitectureSpec:
    components: list[str]
    dataflow: list[str]
    stability_guardrails: list[str]
    throughput_guardrails: list[str]


@dataclass(slots=True)
class EvidenceBuckets:
    paper_grounded: list[str] = field(default_factory=list)
    reasonable_extensions: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)


@dataclass(slots=True)
class DomainBlueprint:
    name: str
    domain: Domain
    stage_focus: list[RLStage]
    environment: EnvironmentSpec
    architecture: ArchitectureSpec
    objective: ObjectiveSpec
    reward_stack: list[str]
    evaluation_gates: list[str]
    failure_modes: list[str]
    evidence: EvidenceBuckets


@dataclass(slots=True)
class ProjectRoadmap:
    stages: list[RLStage]
    operating_beliefs: list[str]
    component_stack: list[str]
    evaluation_priorities: list[str]
    known_risks: list[str]
