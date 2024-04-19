# "Simple Calculator V 1.0"
# Developed by "Sampath Tharanga"


#Define function for addition
def add(x, y):
    return x + y

#Define function for substraction
def subtract(x, y):
    return x - y

#Define function for multiplication
def multiply(x, y):
    return x * y

#Define function for division
def devision(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y
    
# Main function to get user inputs
def calculator():
    print("Simple Calculator V 1.0")
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division \n")

    #Take input from the user
    choice = input("Enter your choice (1/2/3/4):")

    #Check user choice is valid or not
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", devision(num1, num2))
    else:
        print("Invalid Input!")

#Call the calculator function
calculator()