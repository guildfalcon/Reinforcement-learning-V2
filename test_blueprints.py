from agentic_reinforcement.blueprints import build_domain_blueprint, build_project_roadmap


def test_builds_supported_domains() -> None:
    for domain in ["swe", "terminal", "search", "structured-generation"]:
        blueprint = build_domain_blueprint(domain)
        assert blueprint.environment.task_unit
        assert blueprint.objective.objective
        assert blueprint.architecture.components
        assert blueprint.evidence.paper_grounded


def test_roadmap_has_expected_stage_order() -> None:
    roadmap = build_project_roadmap()
    assert [stage.value for stage in roadmap.stages] == [
        "Reasoning RL",
        "Agentic RL",
        "General RL",
        "On-Policy Cross-Stage Distillation",
    ]


def test_unknown_domain_raises_helpful_error() -> None:
    try:
        build_domain_blueprint("vision")
    except ValueError as exc:
        assert "Supported domains" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported domain.")

