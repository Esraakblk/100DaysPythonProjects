from art import logo

# Define mathematical operations
def subtract(n1, n2):
    return n1 - n2

def add(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

# Dictionary to map operations
operations = {
    "-": subtract,
    "+": add,
    "/": divide,
    "*": multiply
    }
def calculate():
    """Main function to perform calculations."""
    print(logo)
    should_accumulate = True # Flag to control whether to continue calculations

    num1 = float(input("What's the first number?: "))
    
    while should_accumulate:
         # Display available operations
        for symbol in operations:
            print(symbol)

        operation_symbol= input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer =operations[operation_symbol](num1,num2) # Perform the calculation
        
        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

        if choice == "y":
            num1 = answer# Use the current result as the new starting number

        elif choice == "n":
            should_accumulate = False  # Break the loop for a new calculation
            print("\n"*20)  # Clear the console
            calculate() # Restart the calculator

calculate()
        
    