import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        """Exit the application."""
        print("Exiting...")
        sys.exit(0)
