from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.addNumbers import AddNumbersCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddNumbersCommand())

        print("Type 'add number1 number2' to add two numbers.")
        while True:
            parts = (input(">>> ").strip()).split()
            command_name = parts[0]
            try:
                args = parts[1:]
                kwargs = {
                    "number1": args[0],
                    "number2": args[1],
                }
                self.command_handler.execute_command(command_name, **kwargs)
            except:
                self.command_handler.execute_command(command_name)
