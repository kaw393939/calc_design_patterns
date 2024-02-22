from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self, *args, **kwargs):
        """Print a goodbye message."""
        print("Goodbye")
