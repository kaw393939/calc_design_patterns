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

    def execute_command(self, command_input: str):
        command_parts = command_input.split()
        command_name = command_parts[0]
        command_args = command_parts[1:]
        
        if command_name in self.commands:
            command_instance = self.commands[command_name]
            command_instance.execute(*command_args)
        else:
            print(f"No such command: {command_name}")
