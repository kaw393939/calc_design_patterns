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

    def execute_command(self, command_name: str, *args):
        if command_name in self.commands:
            self.commands[command_name].execute(*args)
        else:
            print(f"No such command: {command_name}")

