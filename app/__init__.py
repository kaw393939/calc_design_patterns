class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")

        