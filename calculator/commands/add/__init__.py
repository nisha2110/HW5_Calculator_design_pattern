from calculator.commands import Command


class AddCommand(Command):
    """Command for addition."""
    def execute(self, *args):
        return args[0] + args[1]