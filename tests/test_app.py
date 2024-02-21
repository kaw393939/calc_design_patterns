import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    app.start()
    out, err = capfd.readouterr()

    # Updated assertion to match the actual output
    assert "Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    out, err = capfd.readouterr()

    # Updated assertion to match the actual output
    assert "Type 'exit' to exit." in out
    assert "No such command: unknown_command" in out
    assert "Exiting..." in out

