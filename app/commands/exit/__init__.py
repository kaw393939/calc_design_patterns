import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        exit_message = kwargs.get('message', 'Exiting...')
        exit_bye = kwargs.get('hello', 'Bye. Have a great day.')
        print(exit_message, exit_bye)
        sys.exit()