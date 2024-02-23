import sys
from app.commands import Command


class CalendarCommand(Command):
    def execute(self):
        print(f'I will check your calender.')