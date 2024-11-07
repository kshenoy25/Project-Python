import random
import time


# create variables to use as constants

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS) # choice randomly selects element from a list

    expression = str(left) + " " + operator + " " + str(right)
    result = eval(expression) # eval evaluates a string as a python expression
    return expression, result

# timer and display number of correct answers
wrong = 0
input("Press any button to start!")
print("---------------------------")

start_time = time.time() # give unix time since the epoch and time stamp in seconds

for i in range(TOTAL_PROBLEMS):
    expression, result = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        if guess == str(result):
            break
        wrong += 1 # accuracy


end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------------")
print("Nice Job! You finished in", total_time)