from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self):
        if self.args:
            print(f"Goodbye, {self.args[0]}!")
        else:
            print("Goodbye")