import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

def test_greet_command_with_kwargs(capfd):
    command = GreetCommand()
    command.execute(name="DJ", greeting="Greetings")
    out, err = capfd.readouterr()
    assert out.strip() == "Greetings, DJ!"

def test_goodbye_command_with_kwargs(capfd):
    command = GoodbyeCommand()
    command.execute(world="World", bye="Goodbye")
    out, err = capfd.readouterr()
    assert out.strip() == "Goodbye, World!"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"


