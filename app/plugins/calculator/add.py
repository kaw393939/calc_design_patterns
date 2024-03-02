from app.commands import Command

class Add(Command):
    def execute(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"The result is {a + b}")
