import json
import random

PROBLEM_KEY = "problem"
SOLUTION_KEY = "solution"

def calculate_answer(num1: int, num2: int, op: str) -> int:
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2
    else:
        # unreachable
        return 0

def generate_problem() -> tuple[int, int, str, int]:
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
        return generate_problem()  # an answer of 0 makes errors infinity
    return num1, num2, op, solution

def generate_problems(filename: str = "problems.json"):
    with open(filename, 'r') as f:
        data: list[dict[str, str|int]] = json.load(f)
        for _ in range(100):
            num1, num2, op, solution = generate_problem()
            data.append({PROBLEM_KEY : f"{num1} {op} {num2}", SOLUTION_KEY : solution})
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    generate_problems()
