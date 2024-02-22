from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        if self.args:
            print(f"Hello, {self.args[0]}!")
        else:
            print("Hello, World!")