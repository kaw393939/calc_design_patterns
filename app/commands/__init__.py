from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_factory: Command):
        self.commands[command_name] = command_factory

    @staticmethod
    def create_command(Command):
        def command_factory(**kwargs):
            return Command(**kwargs)
        return command_factory

    def execute_command(self, user_input):
        parts = user_input.split()
        if not parts:
            print("No command entered.")
            return

        command_name = parts[0]
        kwargs = {}

        for arg in parts[1:]:
            key, value = arg.split('=')
            try:
                kwargs[key] = float(value)
            except ValueError:
                kwargs[key] = value

        if command_name not in self.commands:
            print(f"No such command: '{command_name}'")
            return

        try:
            command_factory = self.commands[command_name]
            command_instance = command_factory(**kwargs)
            command_instance.execute()
        except Exception as e:
            print(f"An error occurred while executing the command: {e}")

