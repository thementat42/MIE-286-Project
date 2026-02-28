import random

from input_box import InputBox
import pygame as pg
import json

def get_problems(filename = "problems.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_percentage_error(problem: dict[str, str|int], user_solution: int):
    correct_solution = int(problem["solution"])
    return abs((user_solution - correct_solution)/correct_solution)

def draw_problem(problem: dict[str, str], screen: pg.Surface, font: pg.font.Font, location = (50, 50), colour = (255, 255, 255)):
    problem_surface = font.render(problem["problem"], True, colour)
    screen.blit(problem_surface, location)

def main():
    pg.init()
    _font = pg.font.Font(None, 32)
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    input_box = InputBox(100, 100, 140, 32, _font)
    input_boxes = [input_box]
    done = False
    problems = get_problems()
    current_problem = random.choice(problems)
    result = None

    while not done:
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q and pressed[pg.K_LSHIFT] and pressed[pg.K_LALT]:
                done = True
            for box in input_boxes:
                result = box.handle_event(event)
        
        if result is not None and result != "":
            print(f"Answered {result}")
            print(get_percentage_error(current_problem, int(result)))
            result = None
            current_problem = random.choice(problems)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        draw_problem(current_problem, screen, _font)
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()

if __name__ == "__main__":
    main()