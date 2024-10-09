# Homework5: Command Pattern and plugins Project Setup
- The purpose of this project is to create a continually running, dynamic command-line application that starts as a single-execution script and develops into a fully working application. 
1. Create directory and use touch command create files.
2. Integrate these concepts with existing program to add four basic commands: add, subtract, multiply, and divide, making calculator interactive.
3. Make a menu command that, when the application launches and the user inputs "menu," shows the available commands from the command dictionary.
4. Plugin Architecture:
 - refactor program to enable plugins to load automatically, making it simple to add commands without requiring manual updates.
## Instructions:
1. create clone the repo.
2. First Deactivate the virtual environment with the command "deactivate" and then activate it again command.
  i. source venv/bin/activate
3. Install the required libraries.
  - Update the requirements file with pip freeze > requirements.txt.

Note When someone copies / clones my repository they will install the specfic library / dependency requirements for my project using the command:

-> pip install -r requirments.txt
-> Finally, Open VScode and test code.
   i. code .

## Testing

1. pytest
2. pytest --cov
3. python main.py

## Output:
1. hpatel:~/Webdeploy_projects2024/HW5_Calculator_design_pattern$ python main.py
- Hello World. Type 'exit' to exit.
-  ->> exit
-  Exiting...

2. hpatel:~/Webdeploy_projects2024/HW5_Calculator_design_pattern$ python main.py
-  Type 'exit' to exit.
-  Available commands: add, subtract, multiply, divide, menu
-  ->> menu
-  Available commands: add, subtract, multiply, divide, menu
-  ->> add
-  Error: 'add' requires two numeric arguments.
-  ->> add 5 6
-  11.0
-  ->> add e 3
   Error: Both arguments must be numbers.
-  ->> subtract 10 4
-  6.0
-  ->> multiply 2 5
-  10.0
-  ->> divide 10 3
-  3.3333333333333335
-  ->> divide 10 0
-  Error: Division by zero
-  --> divide 1
   Error: 'divide' requires two numeric arguments.
-  ->> goodmornig
-  No such command: goodmornig
-  ->> exit
-  Goodbye!
-  Exiting...

## Other commands used during project
 1. mv oldfile newfilename
 2. git remote remove origin
 3. rm -rf .pytest_cache
 4. To add multiple specific files: git add path/to/file1.py path/to/file2.py path/to/file3.py
 5. coverage report -m