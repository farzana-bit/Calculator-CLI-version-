CLI Calculator in Python

 This is a simple Command-Line Interface (CLI) calculator written in Python. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. The application runs in a loop, allowing users to perform multiple calculations until they choose to exit.

Features:

    - Addition of two numbers.

    - Subtraction of two numbers.

    - Multiplication of two numbers.

    - Division of two numbers with error handling for division by zero.

    - Input validation is used to ensure valid numerical inputs.

    - Continuous interaction with the user until the exit option is selected.

Requirements:

    Python 3.x

Usage:

    1. Clone or download the repository to your local machine.

    2. Open a terminal (or command prompt) and navigate to the project folder.

    3. Run the Python file:
        git init

How It Works:

Functions:

    - add(x, y): Adds two numbers x and y.

    - subtract(x, y): Subtracts the second number y from the first x.

    - multiply(x, y): Multiplies two numbers x and y.

    - divide(x, y): Divides the first number x by the second number y. If y is zero, an error message "Error! Division by zero." is returned.


Menu Display:

The program displays a menu with the following options:

    1. Add

    2. Subtract

    3. Multiply

    4. Divide

    5. Exit

The user is prompted to enter a choice from the menu. The program will proceed based on the selected operation.

Input Validation:

    - The program checks if the user enters a valid numerical input for both numbers. If the input is invalid (e.g., entering letters instead of numbers), the program will display an error message and prompt the user to enter valid numbers.

    - If the user chooses the division operation and enters zero as the divisor, the program will handle the division by zero error by returning a specific error message instead of crashing.

Loop and Exit:

    - The program runs in a continuous loop, allowing the user to perform multiple calculations. The loop will only terminate if the user selects the exit option (5).

    - Once the user selects 5, the program will print "Exiting the calculator. Goodbye!" and terminate.

Example Usage:

    1. Start the program and select an operation:
    Select operation:
          Select operation:
                1. Add
                2. Subtract
                3. Multiply
                4. Divide
                5. Exit
                Enter choice (1/2/3/4/5): 1
    2. Enter two numbers:
           Enter first number: 10
           Enter second number: 5
    3. The result is displayed:
           10.0 + 5.0 = 15.0




