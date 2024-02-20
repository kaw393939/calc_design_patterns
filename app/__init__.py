from app.commands import CommandHandler
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("hello", GreetCommand())

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            if user_input[0].lower() == "exit":
                print("Exiting...")
                break
            command_name = user_input[0]
            command_args = user_input[1:]
            self.command_handler.execute_command(command_name, *command_args)



