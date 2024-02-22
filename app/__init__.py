from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.operations import SplitWord, RemoveSpace

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        
        # Register the SplitWord command
        self.command_handler.register_command("split", SplitWord())
        self.command_handler.register_command("spaceRemover", RemoveSpace())

    def start(self):
        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Process, Loop
            user_input = input(">>> ").strip()
            if user_input == "exit":
                break
            self.command_handler.execute_command(user_input)
