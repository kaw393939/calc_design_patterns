from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args, **kwargs):
        if command_name in self.commands:

            self.commands[command_name].execute(*args, **kwargs)
        else:
            print(f"No such command: {command_name}")

class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        name = kwargs.get('name', 'World')
        print(f"Hello, {name}!")

class AddCommand(Command):
    def execute(self, *args, **kwargs):
        total = sum(args)
        print(f"The sum is: {total}")

handler = CommandHandler()
handler.register_command("greet", GreetCommand())
handler.register_command("add", AddCommand())

handler.execute_command("greet", name="Alice")
handler.execute_command("add", 1, 2, 3)
