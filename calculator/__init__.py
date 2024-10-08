from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self._register_commands()

    def _register_commands(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler.commands))

    def start(self):
        print("Type 'exit' to exit.")
        print(self.command_handler.execute_command("menu"))  # Show menu at the start

        while True:
            user_input = input(">>> ").strip().lower()
            if user_input == 'exit':
                print("Goodbye!")
                raise SystemExit("Exiting...")  # this is raising SystemExit
                break
            elif user_input == 'menu':
                print(self.command_handler.execute_command("menu"))
                      
            else:
                try:
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
                    else:
                        arg1, arg2 = float(parts[1]), float(parts[2])
                        result = self.command_handler.execute_command(command_name, arg1, arg2)
                        print(result)
                   
                except ValueError:
                    print("Error: Invalid number format. Try again.")