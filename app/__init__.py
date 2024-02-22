from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        # Register commands here


    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Process, Loop
            user_input = input(">>> ").strip()
            command_name, *args = user_input.split()  # Split input into command and arguments
            self.command_handler.execute_command(command_name,*args)