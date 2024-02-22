from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True:
            input_text = input(">>> ").strip()
            if not input_text:
                continue
            
            # Splitting the input to extract the command and its arguments
            parts = input_text.split()
            command_name = parts[0]
            args_list = parts[1:]
            
            # Separating positional arguments from keyword arguments
            args = [arg for arg in args_list if '=' not in arg]
            kwargs = {k: v for k, v in (arg.split('=') for arg in args_list if '=' in arg)}

            # Execute the command with args and kwargs
            self.command_handler.execute_command(command_name, *args, **kwargs)
