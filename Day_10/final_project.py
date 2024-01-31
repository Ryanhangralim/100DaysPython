from art import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y 

def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))
    
    choice = 'y'
    while choice == 'y':
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        if(operation == "+"):
            result = add(first_num, second_num)
        elif(operation == "-"):
            result = subtract(first_num, second_num)
        elif(operation == "*"):
            result = multiply(first_num, second_num)
        elif(operation == "/"):
            result = divide(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
    
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if(choice == 'y'):
            first_num = result
        elif(choice == 'n'):
            calculator()
calculator()