from calculator.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        return args[0] * args[1]
        