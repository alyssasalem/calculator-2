"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# while loop to keep running it
# input 
# tokenize input
# check errors in input
# how many tokens
# call on a bunch of functions based on first token

while True:
    input_string = input("What is your equation:")
    tokens = input_string.split(" ")
    operation = tokens[0]
    result = None

    if tokens[0] == "q":
        print("Exiting calculator")
        break
        #arithmetic functions

    # Checks input
    #Check for input errors
    if len(tokens) > 3 or len(tokens) < 2:
        print("Invalid input!!")
        continue
    num1 = tokens[1]        #Assigns first input number to num1
    # If statement checks for less than three arguments
    if len(tokens) < 3:
        
        num2 = "0"            #Assigns second number to 0 if no second number
    else:
        # Assigns second input number to num2
        num2 = tokens[2]

    if not num1.isdigit() or not num2.isdigit():
        print("Those aren't digits")
        continue

    if operation == "+":
        result = add(float(num1), float(num2))
    elif operation == "-":
        result = subtract(float(num1), float(num2))
    elif operation == "*":
        result = multiply(float(num1), float(num2))
    elif operation =="/":
        result = divide(float(num1), float(num2))
    elif operation == "square":
        result = square(float(num1))
    elif operation == "cube":
        result = cube(float(num1))    
    elif operation == "pow":
        result = power(float(num1), float(num2))
    elif operation == "mod":
        result = mod(float(num1), float(num2))
    else:
        print("Not an operation.")
        continue



    # Prints result of calculations
    print(result)
