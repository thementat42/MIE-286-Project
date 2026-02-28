import random

from input_box import InputBox, COLOUR_ACTIVE, COLOUR_INACTIVE
import pygame as pg
import json

def get_problems(filename = "problems.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_percentage_error(problem: dict[str, str], user_solution):
    correct_solution = problem["solution"]
    return abs((user_solution - correct_solution)/correct_solution)

def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    input_box = InputBox(100, 100, 140, 32, pg.font.Font(None, 32))
    input_boxes = [input_box]
    done = False
    problems = get_problems()
    current_problem = random.choice(problems)
    result = None

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                result = box.handle_event(event)
        
        if result is not None:
            print(f"Answered {result}")
            print(get_percentage_error(current_problem, float(result)))
            result = None
            current_problem = random.choice(problems)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()