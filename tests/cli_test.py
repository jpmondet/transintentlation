import sys
import os
from click.testing import CliRunner

sys.path.append(os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))

from transintentlation.cli import cli


def test_cli_default_success():
    runner = CliRunner()
    result = runner.invoke(cli, ["./tests/configs/intent.cfg", "./tests/configs/n9k.cfg"])
    assert result.exit_code == 0
