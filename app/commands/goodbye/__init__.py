from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self, *args, **kwargs):
        goodbye_message = kwargs.get('message', 'Goodbye')
        goodbye_bye = kwargs.get('hello', 'See You Soon.')
        print(goodbye_message)