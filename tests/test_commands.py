import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

def test_greet_command(capfd):
    command = GreetCommand()

    # Test without args and kwargs
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

    # Test with args and kwargs
    command.execute("Alice", greeting="Hi")
    out, err = capfd.readouterr()
    assert out == "Hi, Alice!\n", "The GreetCommand should print 'Hi, Alice!'"

def test_goodbye_command(capfd):
    command = GoodbyeCommand()

    # Test without args and kwargs
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

    # Test with args and kwargs
    command.execute("See you", farewell="Adios")
    out, err = capfd.readouterr()
    assert out == "See you\n", "The GoodbyeCommand should print 'See you'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...\nExit Code: 0", "The app did not exit as expected"
