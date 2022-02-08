import subprocess
import sys

from skeleton_says import __version__


def test_cli_version() -> None:
    cmd = [sys.executable, "-m", "skeleton_says", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__


def test_cli_says_hello() -> None:
    cmd = [sys.executable, "-m", "skeleton_says", "Hello"]
    assert "Hello" in subprocess.check_output(cmd).decode()
