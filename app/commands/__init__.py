from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_instance: Command):
        self.commands[command_name] = command_instance

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

    def list_commands(self):
        for index, command_name in enumerate(self.commands, start=1):
            print(f"{index}. {command_name}")

    def get_command_by_index(self, index: int):
        try:
            command_name = list(self.commands.keys())[index]
            return command_name
        except IndexError:
            return None


