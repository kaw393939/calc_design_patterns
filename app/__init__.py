from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.operations import SayHello, SayName, NameSplit

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        # Register commands here


    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

        #creating more commands
        self.command_handler.register_command("sayHello", SayHello())
        self.command_handler.register_command("sayName", SayName())
        self.command_handler.register_command("splitName", NameSplit())
        

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Process, Loop
            self.command_handler.execute_command(input(">>> ").strip())



