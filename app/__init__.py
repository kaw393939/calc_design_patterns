from app.commands import CommandHandler
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            self.command_handler.execute_command(user_input)



