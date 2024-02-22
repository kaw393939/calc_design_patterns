from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split(" ")
            command_name = user_input[0]
            args = user_input[1:]  # Split the rest of the input for arguments
            self.command_handler.execute_command(command_name, *args)

if __name__ == "__main__":
    app = App()
    app.start()
