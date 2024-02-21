from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self, *args):
        if args:
            for arg in args:
                print(f"Goodbye, {arg}!")
        else:
            print("Goodbye")

