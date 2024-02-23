from app.commands import Command


class AddNumbersCommand(Command):
    def execute(self, **kwargs):
        try:
            number1 = int(kwargs["number1"])
            number2 = int(kwargs["number2"])
        except ValueError:
            raise ValueError(
                "Invalid input. Please provide two valid integers for 'number1' and 'number2'."
            )

        print(number1 + number2)
