import pytest
from calculator import App
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from calculator.commands import CommandHandler

# Test for Add Command
def test_add_command(capfd):
    command = AddCommand()
    result = command.execute(5, 3)
    assert result == 8, " correctly add two numbers"

# Test for Subtract Command
def test_subtract_command(capfd):
    command = SubtractCommand()
    result = command.execute(10, 4)
    assert result == 6, " correctly subtract two numbers"

# Test for Multiply Command
def test_multiply_command(capfd):
    command = MultiplyCommand()
    result = command.execute(6, 7)
    assert result == 42, " correctly multiply two numbers"

# Test for Divide Command
def test_divide_command(capfd):
    command = DivideCommand()
    result = command.execute(8, 2)
    assert result == 4, "correctly divide two numbers"

# Test for Division by Zero
def test_divide_by_zero_command(capfd):
    command = DivideCommand()
    result = command.execute(9, 0)
    assert result == "Error: Division by zero"
    
# Test for Menu Command
def test_menu_command():
    # Simulate a command handler with registered commands
    command_handler = CommandHandler()
    
    # Register plugins/commands
    command_handler.register_command("add", AddCommand())
    command_handler.register_command("subtract", SubtractCommand())
    command_handler.register_command("multiply", MultiplyCommand())
    command_handler.register_command("divide", DivideCommand())
    
    # Create the MenuCommand with the registered commands
    command = MenuCommand(command_handler)
    
    # Execute the menu command and get the result
    result = command.execute()

    # Assert that all expected commands are listed in the result
    assert "add" in result, "add command should be listed"
    assert "subtract" in result, "subtract command should be listed"
    assert "multiply" in result, "multiply command should be listed"
    assert "divide" in result, "divide command should be listed"
    
    
  