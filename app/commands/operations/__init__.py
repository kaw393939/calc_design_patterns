from app.commands import Command


class SayHello(Command):
    def execute(self):
        print("Hello, nice to meet you")
    
class SayName(Command):
    def execute(self, *args):
        name = ' '.join(args)
        print(f"Your name is {name}")

class NameSplit(Command):
    def execute(self, *args):
        try:
            name = ' '.join(args)
            nameSplit = [letter for n in name.split() for letter in n]
            print(f"your name after split is {nameSplit}")
        except Exception as e:
            print(f"Error: {e}")