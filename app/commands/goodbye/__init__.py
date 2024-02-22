from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self, *args, **kwargs):
        print("Goodbye")
