from typer.testing import CliRunner
import pytest

from todo import (
    __app_name__,
    __version__,
    cli,
)

runner = CliRunner()

def test_version():
    # result = runner.invoke(cli.app, ["--version"])
    result = runner.invoke(cli.app, ['--version', '-v', '--help'], terminal_width=60)
    assert result.exit_code == 0
    assert f"Awesome CLI {__app_name__} Version: {__version__}\n" in result.stdout


