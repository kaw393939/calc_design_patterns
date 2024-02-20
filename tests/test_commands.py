import pytest
from app import App
from app.commands import CommandHandler
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.help import HelpCommand

def test_greet_command(capfd):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GreetCommand should print 'Hello, World!'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"


from app.commands.help import HelpCommand

def test_help_command_output(capfd):
    # Create a CommandHandler instance and register some sample commands including the HelpCommand
    command_handler = CommandHandler()
    command_handler.register_command("help", HelpCommand(command_handler))
    command_handler.register_command("greet", GreetCommand())
    # Execute the HelpCommand
    help_command = HelpCommand(command_handler)
    help_command.execute()
    # Capture and evaluate the output
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- help" in out
    assert "- greet" in out
