import pytest
from click.testing import CliRunner
from chromas import cli

def test_version_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert "Chromas version" in result.output


