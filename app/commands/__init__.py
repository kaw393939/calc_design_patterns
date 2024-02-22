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
        args = []
        kwargs = {}

        # Separate args and kwargs
        for part in parts[1:]:
            if '=' in part:
                key, value = part.split('=', 1)
                kwargs[key] = value
            else:
                args.append(part)

        if command_name in self.commands:
            command = self.commands[command_name]
            command.execute(*args, **kwargs)
        else:
            print(f"Unknown command: {command_name}")

