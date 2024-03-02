import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand
class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            # print(f"Found plugin: {plugin_name}")  # Debugging print
            if is_pkg and plugin_name != "menu":  # Ensure it's a package
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())
                            # print(f"Registered command: {plugin_name}")  # Debugging print
                except Exception as e:
                    print(f"Error loading plugin {plugin_name}: {e}")  # Print any errors
        
        # Since menu command would need a seperate argument - which is list of all registered command we have to manually register it.
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

    def print_main_menu(self):
        print("\nAvailable commands:")
        self.command_handler.list_commands()
        print("Type the number of the command to execute, or type 'exit' to exit.")

    def start(self):
        self.load_plugins()
        self.print_main_menu()
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                break
            try:
                index = int(user_input) - 1
                if index < 0:  # Refresh the main menu if '0' or an invalid negative number is entered
                    self.print_main_menu()
                    continue
                command_name = self.command_handler.get_command_by_index(index)
                if command_name:
                    self.command_handler.execute_command(command_name)
                    self.print_main_menu()  # Print the main menu again after command execution
                else:
                    print("Invalid selection. Please enter a valid number.")
            except ValueError:
                print("Only numbers are allowed, wrong input.")


