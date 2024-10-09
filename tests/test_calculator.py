import pytest
import pytest
from unittest.mock import patch, MagicMock
from calculator import App

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calculator = App()
    with pytest.raises(SystemExit) as e:
        calculator.start()
    assert e.type == SystemExit
    
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.out  

def test_calculator_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    calculator = App()
    with pytest.raises(SystemExit) as excinfo:
        calculator.start()
        
     # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

@pytest.fixture
def app():
    return App()

def test_load_plugins(app):
    app.load_plugins()  # Test loading plugins, should not raise any errors

def test_print_available_commands(app):
    with patch('builtins.print') as mocked_print:
        app.command_handler.get_registered_commands = MagicMock(return_value=["add", "subtract"])
        app.print_available_commands()
        mocked_print.assert_called_once_with("Available commands: add, subtract, menu")

def test_start_exit_command(app):
    with patch('builtins.input', side_effect=['exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_called_with("Goodbye!")

def test_start_menu_command(app):
    with patch('builtins.input', side_effect=['menu', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_any_call("Available commands: menu")  # check for menu call

def test_start_invalid_command(app):
    with patch('builtins.input', side_effect=['invalid_command', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_called_with("No such command: invalid_command")

def test_start_command_with_invalid_arguments(app):
    with patch('builtins.input', side_effect=['add a b', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_called_with("Error: 'add' requires two numeric arguments.")

def test_calculator_start_command_with_extra_arguments(app):
    """Test that the REPL handles extra arguments correctly."""
    with patch('builtins.input', side_effect=['add 1 2 3', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_called_with("Error: 'add' requires two numeric arguments.")

def test_calculator_start_command_with_no_arguments(app):
    """Test that the REPL handles no arguments correctly."""
    with patch('builtins.input', side_effect=['add', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_called_with("Error: 'add' requires two numeric arguments.")

def test_calculator_start_command_with_valid_arguments(app):
    """Test command with valid arguments."""
    # Mock a valid command plugin, e.g., 'add'
    with patch('builtins.input', side_effect=['add 1 2', 'exit']):
        with patch('builtins.print') as mocked_print:
            with pytest.raises(SystemExit):
                app.start()
                mocked_print.assert_any_call("Result of add: 3.0")
                
                
                    
    