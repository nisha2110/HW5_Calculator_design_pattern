from calculator.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) < 2:
            return "Error: Multiply command requires two numeric arguments."
        try:
            return args[0] * args[1]
        except TypeError:
            return "Error: Invalid input. Please provide two numbers."