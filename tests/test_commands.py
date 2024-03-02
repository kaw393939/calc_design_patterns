from app.commands import Command
import pytest
from app import App
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand


def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Assuming '6' is the index for the 'greet' command based on the error output
    inputs = iter(['6', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()

    # Capture and assert the expected output
    captured = capfd.readouterr()
    # Adjust the assertion based on the actual expected output of 'greet'
    assert "Hello, World!" in captured.out



def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()  # Start the application without expecting SystemExit

    # Capture and assert the expected output
    captured = capfd.readouterr()
    # Assert that the menu was displayed
    # This depends on what output 'menu' command produces; for example:
    assert "Available commands:" in captured.out

from unittest.mock import MagicMock
from app.plugins.calculator import CalculatorCommand

# Mock operation classes
class MockAddCommand(Command):
    def execute(self):
        print("Performing addition")

class MockSubtractCommand(Command):
    def execute(self):
        print("Performing subtraction")

@pytest.fixture
def mock_operations(monkeypatch):
    # Mock the load_operations method to return a fixed set of operations
    def mock_load_operations(self):
        return {'1': MockAddCommand(), '2': MockSubtractCommand()}
    monkeypatch.setattr(CalculatorCommand, "load_operations", mock_load_operations)

def test_calculator_display_operations_and_exit(capfd, monkeypatch, mock_operations):
    # Simulate user selecting '0' to exit the operations menu
    monkeypatch.setattr('builtins.input', lambda _: '0')
    calculator_cmd = CalculatorCommand()
    calculator_cmd.execute()

    captured = capfd.readouterr()
    assert "\nCalculator Operations:" in captured.out
    assert "1. MockAddCommand" in captured.out
    assert "2. MockSubtractCommand" in captured.out
    assert "0. Back" in captured.out

# inputs = iter(['1', '0'])
# monkeypatch.setattr('builtins.input', lambda _: next(inputs, 'default_value'))

def test_calculator_execute_operation(capfd, monkeypatch):
    # Simulate user selecting an operation ('1'), entering two numbers, and then choosing to exit ('0')
    inputs = ['1', '2', '3', '0']  # Example: '1' to select the first operation, '2' and '3' as operands, '0' to exit
    input_generator = (input for input in inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

    calculator_cmd = CalculatorCommand()
    calculator_cmd.execute()

    captured = capfd.readouterr()
    # Adjust the assertion to match the actual expected result output
    assert "The result is 5.0" in captured.out

from unittest.mock import MagicMock
import sys
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand

# Mock commands to register with the CommandHandler
class MockCommand(Command):
    def execute(self):
        print("Mock command executed.")

@pytest.fixture
def command_handler_with_commands():
    handler = CommandHandler()
    handler.register_command('test', MockCommand())
    handler.register_command('help', MockCommand())
    return handler

def test_menu_command_display_and_exit(capfd, monkeypatch, command_handler_with_commands):
    # Mock input to select '0' and exit
    monkeypatch.setattr('builtins.input', lambda _: '0')
    # Mock sys.exit to prevent the test from exiting
    mock_exit = MagicMock()
    monkeypatch.setattr(sys, 'exit', mock_exit)
    
    menu_cmd = MenuCommand(command_handler_with_commands)
    menu_cmd.execute()

    captured = capfd.readouterr()
    assert "\nMain Menu:" in captured.out
    assert "1. Test" in captured.out
    assert "2. Help" in captured.out
    assert "Enter the number of the command to execute, or '0' to exit." in captured.out
    mock_exit.assert_called_once_with("Exiting program.")  # Verify sys.exit was called

def test_menu_command_invalid_selection(capfd, monkeypatch, command_handler_with_commands):
    # Simulate an invalid selection followed by exit
    inputs = iter(['999', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Mock sys.exit to prevent the test from exiting
    monkeypatch.setattr(sys, 'exit', MagicMock())

    menu_cmd = MenuCommand(command_handler_with_commands)
    menu_cmd.execute()

    captured = capfd.readouterr()
    assert "Invalid selection. Please enter a valid number." in captured.out

import pytest
from unittest.mock import MagicMock
from app.commands import Command
from app.plugins.openai import OpenAICommand

# Mock OpenAI operations
class MockChatCommand(Command):
    def execute(self):
        print("Chat operation executed.")

@pytest.fixture
def openai_command_with_operations(monkeypatch):
    # Mock the load_operations method to return a set of mock operations
    def mock_load_operations(self):
        return {'1': MockChatCommand()}
    monkeypatch.setattr(OpenAICommand, "load_operations", mock_load_operations)
    return OpenAICommand()

def test_openai_command_display_and_exit(capfd, monkeypatch, openai_command_with_operations):
    # Simulate user selecting '0' to exit
    monkeypatch.setattr('builtins.input', lambda _: '0')
    openai_command_with_operations.execute()

    captured = capfd.readouterr()
    assert "OPEN AI Operations:" in captured.out
    assert "1. MockChatCommand" in captured.out
    assert "0. Back" in captured.out

def test_openai_command_execute_operation(capfd, monkeypatch, openai_command_with_operations):
    # Simulate user selecting operation '1' and then exiting with '0'
    inputs = ['1', '0']
    input_generator = (input for input in inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

    openai_command_with_operations.execute()

    captured = capfd.readouterr()
    assert "Chat operation executed." in captured.out
