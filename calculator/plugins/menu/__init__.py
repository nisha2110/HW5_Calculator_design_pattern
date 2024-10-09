import sys
from calculator.commands import Command

class MenuCommand(Command):
           
    def __init__(self, command_handler):
        self.command_handler = command_handler
        
    def execute(self):
        available_commands = self.command_handler.get_registered_commands()
        return "Available commands: " + ", ".join(available_commands)