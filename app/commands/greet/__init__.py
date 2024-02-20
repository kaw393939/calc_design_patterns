from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args):
        if args:
            for arg in args:
                print(f"Hello, {arg}!")
        else:
            print("Hello, World!")