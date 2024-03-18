import pytest
from unittest.mock import patch
import project  # Assuming your main code is in a file named 'main.py'

def test_some_func():
    with patch("builtins.print") as mocked_print:
        project.some_func()
        mocked_print.assert_called_once()

def test_somes_func():
    with patch("builtins.print") as mocked_print:
        project.somes_func()
        mocked_print.assert_called_once()

def test_somed_func():
    with patch("builtins.print") as mocked_print:
        project.somed_func()
        mocked_print.assert_called_once()
