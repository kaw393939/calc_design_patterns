from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        """
        Greet a user by name with an optional custom greeting message.
        If no name is provided, defaults to "World".
        If no custom greeting is provided, defaults to "Hello".
        """
        # Default values
        name = "World"
        greeting = "Hello"
        
        # If a name is provided as an argument, use it
        if args:
            name = args[0]
        
        # If a custom greeting is provided as a keyword argument, use it
        if 'greeting' in kwargs:
            greeting = kwargs['greeting']

        print(f"{greeting}, {name}!")
