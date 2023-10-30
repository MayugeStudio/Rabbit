# --- Standard Library ---
import json

# --- Third Party Library ---
from click.testing import CliRunner

# --- First Party Library ---
from rabbit_todo.cmd.cli import cli
from rabbit_todo.common.messages import ERROR_NOT_FOUND
from rabbit_todo.common.messages import SuccessMessage
from rabbit_todo.io.io_config.path_config import ROOT_DIR_PATH


def test_add_task():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["add", "Test Task 1"])  # type: ignore

        assert result.exit_code == 0
        assert SuccessMessage.add_task("Test Task 1") in result.output
        with ROOT_DIR_PATH.joinpath("tasks.json").open("r", encoding="utf-8") as file:
            file_content = json.load(file)
        tasks = file_content["tasks"]
        assert len(tasks) == 1
        assert tasks[0]["id"] == 0
        assert tasks[0]["name"] == "Test Task 1"


def test_remove_task():
    runner = CliRunner()
    with runner.isolated_filesystem():
        runner.invoke(cli, ["add", "Test Task 1"])  # type: ignore
        result = runner.invoke(cli, ["remove", "0"])  # type: ignore

        with ROOT_DIR_PATH.joinpath("tasks.json").open("r", encoding="utf-8") as file:
            file_content = json.load(file)
        tasks = file_content["tasks"]
        assert result.exit_code == 0
        assert SuccessMessage.remove_task("Test Task 1") in result.output
        assert len(tasks) == 0


def test_remove_not_found():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["remove", "0"])  # type: ignore

        assert result.exit_code == 1
        assert ERROR_NOT_FOUND in result.output


def test_done_task():
    runner = CliRunner()
    with runner.isolated_filesystem():
        runner.invoke(cli, ["add", "Test Task 1"])  # type: ignore
        result = runner.invoke(cli, ["done", "0"])  # type: ignore

        assert result.exit_code == 0
        assert SuccessMessage.mark_as_complete("Test Task 1") in result.output
        with ROOT_DIR_PATH.joinpath("tasks.json").open("r", encoding="utf-8") as file:
            file_content = json.load(file)

        tasks = file_content["tasks"]
        assert len(tasks) == 1
        assert tasks[0]["completed"] is True


def test_done_task_not_found():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["done", "0"])  # type: ignore

        assert result.exit_code == 1
        assert ERROR_NOT_FOUND in result.output


def test_list_tasks():
    runner = CliRunner()
    with runner.isolated_filesystem():
        runner.invoke(cli, ["add", "Test Task 1"])  # type: ignore
        runner.invoke(cli, ["add", "Test Task 2"])  # type: ignore
        result = runner.invoke(cli, ["list"])  # type: ignore

        assert result.exit_code == 0
        expected1 = "[ ]: ID - 0   Test Task 1"
        expected2 = "[ ]: ID - 1   Test Task 2"
        expected = f"{expected1}\n{expected2}\n"
        assert result.output == expected
