import sys
from app.commands import Command


class EmailCommand(Command):
    def execute(self):
        print(f'I will email you')