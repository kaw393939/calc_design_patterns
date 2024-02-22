from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self, *args, **kwargs):
        name = kwargs.get('name')
        print(f"Goodbye {name if name else 'friend'}")