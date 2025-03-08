import os

import pytest

from actions import core


os.environ["INPUT_TEST"] = " TRUE "
os.environ["INPUT_FALSE"] = " untrue "
os.environ["GITHUB_OUTPUT"] = os.environ.get("GITHUB_OUTPUT") or "output.txt"
os.environ["GITHUB_ENV"] = os.environ.get("GITHUB_ENV") or "output.txt"
os.environ["GITHUB_PATH"] = os.environ.get("GITHUB_PATH") or "output.txt"
os.environ["GITHUB_STATE"] = os.environ.get("GITHUB_STATE") or "output.txt"
os.environ["GITHUB_STEP_SUMMARY"] = os.environ.get("GITHUB_STEP_SUMMARY") or "output.txt"


def test_print():
    core.debug("debug")
    core.info("info")
    core.notice("notice")
    core.warn("warn")
    with pytest.raises(SystemExit):
        core.set_failed("test")
    core.mask("test")
    core.start_group("test")
    core.end_group()
    core.start_indent()
    core.info("indent")
    core.end_indent()
    core.info("dedent")
    core.stop_commands()
    core.info("::warning::Just kidding")
    core.start_commands()
    with core.group("Title") as p:
        core.info("with group")
        p("core.info")
    core.info("no group")
    core.command("debug", "test")


def test_outputs():
    core.set_output("test", "value")
    core.set_env("test", "value")
    core.summary("test")
    core.add_path("/dev/null")
    core.set_state("STATE_test", "value")
    os.environ["STATE_test"] = "value"


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", low=True) == os.environ["INPUT_TEST"].strip().lower()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    assert core.get_bool("test")
    with pytest.raises(ValueError):
        core.get_input("asdf", req=True)
    with pytest.raises(ValueError):
        core.get_bool("asdf", req=True)
    with pytest.raises(ValueError):
        core.get_list("asdf", req=True)
    assert isinstance(core.get_list("test", split="\n"), list)
    assert len(core.get_list("test", split="\n")) == 1
    assert not core.get_bool("false")


def test_getters():
    assert core.get_state("STATE_test") == "value"
    assert len(core.get_random(20)) == 20
    assert not core.is_debug()
