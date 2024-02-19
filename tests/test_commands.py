import pytest
from app import App
from app.commands import GreetCommand  # Adjust the import according to your project structure

def test_greet_command(capfd):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"


def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()  # Assuming App.start() is now a static method based on previous discussions
    out, err = capfd.readouterr()
    
    # Corrected assertion to match the actual output
    assert "Hello, World!" in out
    assert "Exiting..." in out

