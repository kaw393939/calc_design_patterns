
import pkgutil
import importlib
from app.commands import Command

class OpenAICommand(Command):
    def __init__(self, plugins_package='app.plugins.openai'):
        self.plugins_package = plugins_package
        self.operations = self.load_operations()

    def load_operations(self):
        operations = {}
        plugin_paths = [self.plugins_package.replace('.', '/')]
        found_plugins = pkgutil.iter_modules(plugin_paths)
        # Sort plugins by name to ensure consistent order
        sorted_plugins = sorted(found_plugins, key=lambda x: x[1])
        for index, (finder, name, ispkg) in enumerate(sorted_plugins, start=1):
            if ispkg:
                continue  # Skip sub-packages
            try:
                plugin_module = importlib.import_module(f"{self.plugins_package}.{name}")
                for attribute_name in dir(plugin_module):
                    attribute = getattr(plugin_module, attribute_name)
                    if issubclass(attribute, Command) and attribute is not Command:
                        # Use numeric keys for operations based on their sorted order
                        operations[str(index)] = attribute()
            except (ImportError, TypeError) as e:
                print(f"Error loading plugin {name}: {e}")
        return operations
    def execute(self):
        while True:
            print("OPEN AI Operations:")
            # Sorted ensures the display is in numeric order
            for key in sorted(self.operations.keys(), key=int):
                print(f"{key}. {self.operations[key].__class__.__name__}")
            print("0. Back")

            choice = input("Select an operation: ")
            if choice == '0':
                break  # Exit to the main menu

            operation = self.operations.get(choice)
            if operation:
                operation.execute()
            else:
                print("Invalid selection. Please try again.")


