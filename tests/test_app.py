import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    app.start()  # Start the application without expecting SystemExit

    # Since there's no SystemExit, we can directly assert on the output if needed
    captured = capfd.readouterr()
    # Add assertions here if there's specific output expected upon exiting




def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['999', 'exit'])  # Use a command that's expected to be invalid
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()  # Start the application without expecting SystemExit

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Invalid selection. Please enter a valid number." in captured.out or "Only numbers are allowed, wrong input." in captured.out

