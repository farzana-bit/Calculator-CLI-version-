#function to add two numbers
def add(x, y):
    return x + y

#function to subtract two numbers

def subtract(x, y):
    return x - y

#function to multiply two numbers
def multiply(x, y):
    return x * y

#function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y     
    else:
        return "Error! Division by zero is not allowed."
    
#function display the menu
def display_menu():
    print("Select operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

#Main calculator function
def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice =='5':
            print("Exiting the calculator. Goodbye!")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please choose a valid option.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
               print("Invalid input. Please enter a number.")
               continue
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        

# Run the calculator
calculator()   