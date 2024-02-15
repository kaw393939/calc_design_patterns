class App():
    def __init__(self) -> None:
        print("Hello World")

    @classmethod
    def create(cls):
        return cls()
