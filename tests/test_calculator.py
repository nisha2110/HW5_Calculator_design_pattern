import pytest
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

def test_app_start_unknown_command(capfd, monkeypatch):
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
    