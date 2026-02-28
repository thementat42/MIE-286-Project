import json
import random

def calculate_answer(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2

def generate_problem():
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)
    num1 = random.randint(2, 9)  # 1-digit number
    num2 = random.randint(2, 99)  # 2-digit number

    if op == '/':
        # Ensure the division results in an integer
        num1, num2 = num2, random.randint(2, 9)
        num1 *= num2
    if op == '-':
        num1, num2 = max(num1, num2), min(num1, num2) # make sure num1 > num2
    solution = calculate_answer(num1, num2, op)
    if solution == 0:
        generate_problem()  # an answer of 0 makes errors infinity
    return num1, num2, op, solution

def generate_problems(filename = "problems.json"):
    with open(filename, 'r') as f:
        data: list = json.load(f)
        for i in range(100):
            num1, num2, op, solution = generate_problem()
            data.append({"problem" : f"{num1} {op} {num2}", f"solution" : solution})
    with open(filename, 'w') as f:
        json.dump(data, f)

generate_problems()
