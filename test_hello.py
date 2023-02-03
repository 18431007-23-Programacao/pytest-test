import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
        [
            ("Sergio", "Olá Sergio!"),
            ("ana", "Olá ana!"),
            ("António", "Olá António!"),
            ("123", "Olá 123!"),
            ("", "Olá !"),
        ],
)

def test_hello(monkeypatch: MonkeyPatch, test_input: str, expected_output: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("hello", None)
        importlib.import_module(name="hello")

    assert mocked_stdout.getvalue().strip() == expected_output
