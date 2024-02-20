import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: 'unknown_command'" in captured.out
    assert "Exiting..." in excinfo.value.args[0]

def test_app_with_help_command(capfd, monkeypatch):
    # Simulate user entering 'help' followed by 'exit'
    inputs = iter(['help', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()

    # Expect the SystemExit exception
    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Now you can also check if the exit message or code is as expected (optional)
    # assert excinfo.value.code == SomeExpectedValue

    # Capture and verify the output before the application exits
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.out
    assert "Available commands:" in captured.out
    assert "- help" in captured.out
    # Add more assertions as necessary for other commands