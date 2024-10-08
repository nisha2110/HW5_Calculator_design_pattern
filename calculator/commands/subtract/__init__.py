from calculator.commands import Command


class SubtractCommand(Command):
    """Command for subtraction."""
    def execute(self, *args):
        if len(args) < 2:
            return "Error: Two arguments are required for subtraction."
        return args[0] - args[1]