from app.commands import Command


class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        name = ' '.join(args) if args else 'Guest'
        print(f"Hello, {name}!")