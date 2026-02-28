import random

from input_box import InputBox
from problem_generator import PROBLEM_KEY, SOLUTION_KEY
import pygame as pg
import json

USER_ANSWER_KEY = "user_answer"
ERROR_KEY = "percent_error"
ANSWERED_KEY = "answered"

AnswerType = dict[str, str|int|float|None|bool]

def get_problems(filename: str = "problems.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_percentage_error(correct_solution: int, user_solution: int) -> float:
    return abs((user_solution - correct_solution)/correct_solution)

def draw_problem(problem: dict[str, str|int], screen: pg.Surface, font: pg.font.Font, location: tuple[int,int] = (50, 50), colour: tuple[int, int, int] = (255, 255, 255)):
    problem_surface = font.render(str(problem[PROBLEM_KEY]), True, colour)
    screen.blit(problem_surface, location)

def make_log_entry(problem: dict[str, str|int], user_answer: int|None) -> AnswerType:
    prob = problem[PROBLEM_KEY]
    sol = int(problem[SOLUTION_KEY])
    answered = user_answer is not None
    if answered:
        error = get_percentage_error(sol, user_answer)
    else:
        error = None
    return {
        PROBLEM_KEY: prob,
        SOLUTION_KEY: sol,
        USER_ANSWER_KEY: user_answer if user_answer is not None else 0,
        ERROR_KEY: error,
        ANSWERED_KEY: answered
    }


def main(output_filename: str = "test.json"):
    pg.init()
    _font = pg.font.Font(None, 32)
    screen = pg.display.set_mode((640, 480))
    #clock = pg.time.Clock()
    input_box = InputBox(100, 100, 140, 32, _font)
    input_boxes = [input_box]
    done = False
    problems = get_problems()
    current_problem = random.choice(problems)
    result = None
    answers: list[AnswerType] = []

    while not done:
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q and pressed[pg.K_LSHIFT] and pressed[pg.K_LALT]:
                done = True
            for box in input_boxes:
                result = box.handle_event(event)
        
        if result is not None and result != "":
            answers.append(x := make_log_entry(current_problem, int(result)))
            print(x)
            result = None
            current_problem = random.choice(problems)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        draw_problem(current_problem, screen, _font)
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
    
    with open(output_filename, 'w') as f:
        f.write(json.dumps(answers, indent = 4))

if __name__ == "__main__":
    main()