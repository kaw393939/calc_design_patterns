import sys
from app.commands import Command

class MenuCommand(Command):
    def __init__(self):
        # Initialize the list of commands
        self.commands = ['Discord', 'exit', 'goodbye', 'greet', 'calendar']
    
    def execute(self):
        print('Menu')
        # Iterate over the commands and print them
        for command in self.commands:
            print(f'- {command}')

# Example usage
if __name__ == "__main__":
    menu = MenuCommand()
    menu.execute()
