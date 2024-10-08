import pytest
from calculator import App
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand

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
def test_menu_command(capfd):
    # Create a dummy commands dictionary for testing
    commands = {
        "add": "AddCommand",
        "subtract": "SubtractCommand",
        "multiply": "MultiplyCommand",
        "divide": "DivideCommand"
    }

    # Pass the dummy command dictionary to the MenuCommand
    command = MenuCommand(commands)
    
    # Capture the output
    result = command.execute()
    captured = capfd.readouterr()

    # Assert that the expected commands are listed in the output
    assert "add" in result and "subtract" in result, "Display available commands"
    assert "multiply" in result and "divide" in result, "Display all available commands"
