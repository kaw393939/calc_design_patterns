from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.help import HelpCommand
from app.commands.operations import Addition, Subtraction, Division, Multiplication, Power, Modulus

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        # Register commands here


    def start(self):
        self.command_handler.register_command("greet", CommandHandler.create_command(GreetCommand))
        self.command_handler.register_command("goodbye", CommandHandler.create_command(GoodbyeCommand))
        self.command_handler.register_command("exit", CommandHandler.create_command(ExitCommand))
        self.command_handler.register_command("help", CommandHandler.create_command(HelpCommand, command_handler=self.command_handler))
        
        self.command_handler.register_command("add", CommandHandler.create_command(Addition))
        self.command_handler.register_command("subtract", CommandHandler.create_command(Subtraction))
        self.command_handler.register_command("multiply", CommandHandler.create_command(Multiplication))
        self.command_handler.register_command("divide", CommandHandler.create_command(Division))
        self.command_handler.register_command("power", CommandHandler.create_command(Power))
        self.command_handler.register_command("mod", CommandHandler.create_command(Modulus))

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Process, Loop
            self.command_handler.execute_command(input(">>> ").strip())



