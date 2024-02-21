from app.commands import Command

class GreetCommand(Command):
    def execute(self, **kwargs):
        name = kwargs.get('name', 'World')  # Default is 'World' if name not provided
        print(f"Hello, {name}!")