from app.commands import Command


class GreetCommand(Command):
    def execute(self, **kwargs):
        message = kwargs.get('message', 'World')
        greeting = kwargs.get('greeting', 'Hello')
        print(f"{greeting}, {message}!")