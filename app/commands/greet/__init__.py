from app.commands import Command


class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        name = kwargs.get('name', 'there')
        print(f"Hello, {name}!")
