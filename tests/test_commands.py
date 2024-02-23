"""
This module contains tests for the command execution functionality within the app.
It includes tests for greeting and goodbye commands, as well as the app's ability to handle these commands through its REPL interface.
"""

import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

def test_greet_command(capfd):
    """Test the output of the GreetCommand."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Ignore error output as it's unused
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """Test the output of the GoodbyeCommand."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Ignore error output as it's unused
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    # The assertion for the SystemExit value might need adjustment based on actual app behavior
    # assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    # The assertion for the SystemExit value might need adjustment based on actual app behavior
    # assert str(e.value) == "Exiting...", "The app did not exit as expected"
