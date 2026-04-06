from agentic_reinforcement.cli import main


def test_blueprint_command_renders_domain_blueprint(capsys) -> None:
    exit_code = main(["blueprint", "--domain", "swe"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Software Engineering Agentic RL" in captured.out
    assert "## Environment" in captured.out


def test_roadmap_command_renders_default_roadmap(capsys) -> None:
    exit_code = main(["roadmap"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "## Stages" in captured.out
    assert "Agentic RL" in captured.out
