# Python Calculator

operator = input("Enter your operator (+ - * /): ")

# accepting user inputs are string data types
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# ,3 is rounding with 3 decimal places shown after specific arithmetic operations occur

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result , 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))


else:
    print(f"{operator} is invalid operator")
