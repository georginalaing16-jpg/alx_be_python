# Prompt User to enter first and second numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Prompt User to enter an operator
operation = input("Choose the operator (+, -, *, /): ")
# Perform calculation based on the operator using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator. Please choose one of +, -, *, or /.")
