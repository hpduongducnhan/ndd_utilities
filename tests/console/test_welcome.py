# -*- coding: utf-8 -*-
# """Tests for `modern_python_boilerplate`.cli module."""
# from typing import List

# import pytest
# from click.testing import CliRunner

# import source
# from source.console import welcome


# @pytest.mark.parametrize(
#     "options,expected",
#     [
#         ([], "source.console.welcome.main"),
#         (["--help"], "Usage: main [OPTIONS]"),
#         (["--version"], f"main, version { source.__version__ }\n"),
#     ],
# )
# def test_command_line_interface(options: List[str], expected: str) -> None:
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(welcome, options)
#     assert result.exit_code == 0
#     assert expected in result.output
