from calculator.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        if args[1] == 0:
            return "Error: Division by zero"
        return args[0] / args[1]