from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, input_str):
        parts = input_str.split()
        command_name = parts[0]
        args = parts[1:]  # Remaining parts are arguments

        if command_name in self.commands:
            command = self.commands[command_name]
            command.execute(*args)  # Pass arguments as *args
        else:
            print(f"Unknown command: {command_name}")

