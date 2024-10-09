from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, *args):
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            return f"No such command: '{name}'"
        
    # Add this method to return a list of registered commands
    def get_registered_commands(self):
        return list(self.commands.keys())  # Return the list of command names
