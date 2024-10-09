import pkgutil
import importlib
from calculator.commands import CommandHandler
from calculator.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

            
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'calculator.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                       
                    except TypeError:
                        continue
                     
    def print_available_commands(self):
        # Get available commands from the command handler
        available_commands = self.command_handler.get_registered_commands()
        print("Available commands: " + ", ".join(available_commands))
        
    def start(self):
         # Register commands here
        self.load_plugins()
        
        print("Type 'exit' to exit.")
        print("Type 'menu' to see all available commands.")
        while True: #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().lower()
            if user_input == 'exit':
                print("Goodbye!")
                raise SystemExit("Exiting...")    
            elif user_input == 'menu':
                self.print_available_commands()          
            else:
                parts = user_input.split()
                command_name = parts[0]
                # Check if command is valid
                if command_name not in self.command_handler.commands:
                    print(f"No such command: {command_name}")
                    continue
                # Ensure correct number of arguments (2 numbers expected for math commands)
                if len(parts) != 3:
                    print(f"Error: '{command_name}' requires two numeric arguments.")
                    continue
                # Check if the arguments are valid numbers
                try:
                    arg1, arg2 = float(parts[1]), float(parts[2])
                except ValueError:
                    print("Error: Both arguments must be numbers.")
                    continue

                # Execute the command if arguments are valid
                result = self.command_handler.execute_command(command_name, arg1, arg2)
                if result:
                    print(result)
                