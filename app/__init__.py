from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self): 
        self.command_handler = CommandHandler()
 

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True:  
            input_text = input(">>> ").strip()
            parts = input_text.split()
            if not parts:
                continue 
            command_name = parts[0]
            args = parts[1:]

            kwargs = {arg.split('=')[0]: arg.split('=')[1] for arg in args if '=' in arg}
            args = [arg for arg in args if '=' not in arg]

            self.command_handler.execute_command(command_name, *args, **kwargs)
