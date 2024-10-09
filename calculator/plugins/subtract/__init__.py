from calculator.commands import Command


class SubtractCommand(Command):
    """Command for subtraction."""
    def execute(self, *args):
        return args[0] - args[1]