import sys
from calculator.commands import Command

class MenuCommand(Command):
    def __init__(self, commands):
        self.commands = commands
        
    def execute(self):
        return "Available commands: " + ", ".join(self.commands.keys())