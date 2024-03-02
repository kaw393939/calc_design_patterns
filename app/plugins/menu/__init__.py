import sys
from app.commands import Command, CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        commands = list(self.command_handler.commands.keys())
        # Print the menu dynamically based on registered commands
        print("\nMain Menu:")
        for index, command_name in enumerate(commands, start=1):
            print(f"{index}. {command_name.capitalize()}")
        print("Enter the number of the command to execute, or '0' to exit.")

        try:
            selection = int(input("Selection: "))
            if selection == 0:
                sys.exit("Exiting program.")  # Gracefully exit if the user selects '0'
            command_name = commands[selection - 1]  # Adjust for zero-based indexing
            self.command_handler.execute_command(command_name)
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
        except KeyError:
            print("Selected command could not be executed.")
