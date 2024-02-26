import sys
from app.commands import Command


class GeorgeCommand(Command):
    def execute(self, context = []):
        print(f'Hello George')