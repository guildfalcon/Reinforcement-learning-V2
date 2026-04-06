from __future__ import annotations

from .models import DomainBlueprint, ProjectRoadmap


def render_blueprint_markdown(blueprint: DomainBlueprint) -> str:
    lines = [
        f"# {blueprint.name}",
        "",
        f"- Domain: `{blueprint.domain.value}`",
        f"- Stage focus: {', '.join(stage.value for stage in blueprint.stage_focus)}",
        "",
        "## Environment",
        f"- Task unit: {blueprint.environment.task_unit}",
        f"- Initial state: {blueprint.environment.initial_state}",
        f"- Action space: {', '.join(blueprint.environment.action_space)}",
        f"- Transition source: {', '.join(blueprint.environment.transition_source)}",
        f"- Terminal condition: {', '.join(blueprint.environment.terminal_condition)}",
        f"- Reward sources: {', '.join(blueprint.environment.reward_sources)}",
        f"- Anti-cheat checks: {', '.join(blueprint.environment.anti_cheat_checks)}",
        "",
        "## Architecture",
        f"- Components: {', '.join(blueprint.architecture.components)}",
        f"- Dataflow: {' -> '.join(blueprint.architecture.dataflow)}",
        f"- Stability guardrails: {', '.join(blueprint.architecture.stability_guardrails)}",
        f"- Throughput guardrails: {', '.join(blueprint.architecture.throughput_guardrails)}",
        "",
        "## Objective",
        f"- Objective: {blueprint.objective.objective}",
        f"- Off-policy controls: {', '.join(blueprint.objective.off_policy_controls)}",
        f"- Sample filters: {', '.join(blueprint.objective.sample_filters)}",
        "",
        "## Rewards",
    ]
    lines.extend(f"- {item}" for item in blueprint.reward_stack)
    lines.extend(["", "## Evaluation Gates"])
    lines.extend(f"- {item}" for item in blueprint.evaluation_gates)
    lines.extend(["", "## Failure Modes"])
    lines.extend(f"- {item}" for item in blueprint.failure_modes)
    lines.extend(["", "## Evidence Buckets", "### Paper-Grounded"])
    lines.extend(f"- {item}" for item in blueprint.evidence.paper_grounded)
    lines.extend(["", "### Reasonable Extensions"])
    lines.extend(f"- {item}" for item in blueprint.evidence.reasonable_extensions)
    lines.extend(["", "### Open Questions"])
    lines.extend(f"- {item}" for item in blueprint.evidence.open_questions)
    return "\n".join(lines)


def render_roadmap_markdown(roadmap: ProjectRoadmap) -> str:
    lines = [
        "# Agentic Reinforcement Project Roadmap",
        "",
        "## Stages",
    ]
    lines.extend(f"- {stage.value}" for stage in roadmap.stages)
    lines.extend(["", "## Operating Beliefs"])
    lines.extend(f"- {item}" for item in roadmap.operating_beliefs)
    lines.extend(["", "## Component Stack"])
    lines.extend(f"- {item}" for item in roadmap.component_stack)
    lines.extend(["", "## Evaluation Priorities"])
    lines.extend(f"- {item}" for item in roadmap.evaluation_priorities)
    lines.extend(["", "## Known Risks"])
    lines.extend(f"- {item}" for item in roadmap.known_risks)
    return "\n".join(lines)
