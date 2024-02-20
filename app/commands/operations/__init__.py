from app.commands import Command

class Addition(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            print(f"The sum of {self.a} and {self.b} is {self.a + self.b}")
        except TypeError:
            print("Error: Addition operation requires numeric types.")

class Subtraction(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            print(f"The difference between {self.a} and {self.b} is {self.a - self.b}")
        except TypeError:
            print("Error: Subtraction operation requires numeric types.")

class Multiplication(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            print(f"The product of {self.a} and {self.b} is {self.a * self.b}")
        except TypeError:
            print("Error: Multiplication operation requires numeric types.")

class Division(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            if self.b == 0:
                raise ZeroDivisionError
            print(f"The quotient of {self.a} divided by {self.b} is {self.a / self.b}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError:
            print("Error: Division operation requires numeric types.")

class Power(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            print(f"{self.a} raised to the power of {self.b} is {self.a ** self.b}")
        except TypeError:
            print("Error: Power operation requires numeric types.")

class Modulus(Command):
    def __init__(self, **kwargs):
        self.a = kwargs.get('a')
        self.b = kwargs.get('b')

    def execute(self):
        try:
            print(f"The remainder of {self.a} divided by {self.b} is {self.a % self.b}")
        except ZeroDivisionError:
            print("Error: Modulus by zero is not allowed.")
        except TypeError:
            print("Error: Modulus operation requires numeric types.")
