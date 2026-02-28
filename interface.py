from enum import Enum
import os
import random

from input_box import InputBox
from problem_generator import PROBLEM_KEY, SOLUTION_KEY
import pygame as pg
import json

USER_ANSWER_KEY = "user_answer"
ERROR_KEY = "percent_error"
ANSWERED_KEY = "answered"
TIME_KEY = "time_taken"
TIME_LIMIT_SECONDS = 10

AnswerType = dict[str, str|int|float|None|bool]

class Mode(Enum):
    BASELINE = 0
    LOSS_BASED = 1
    GAIN_BASED = 2

def get_problems(filename: str = "problems.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_percentage_error(correct_solution: int, user_solution: int) -> float:
    return abs((user_solution - correct_solution)/correct_solution)

def draw_problem(problem: dict[str, str|int], screen: pg.Surface, font: pg.font.Font, location: tuple[int,int] = (50, 50), colour: tuple[int, int, int] = (255, 255, 255)):
    problem_surface = font.render(str(problem[PROBLEM_KEY]), True, colour)
    screen.blit(problem_surface, location)

def make_log_entry(problem: dict[str, str|int], user_answer: int|None, time_taken: float) -> AnswerType:
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
        ANSWERED_KEY: answered,
        TIME_KEY: time_taken
    }


def main(output_filename: str = "x.test.json", mode: Mode = Mode.BASELINE):
    pg.init()
    _font = pg.font.Font(None, 32)
    screen = pg.display.set_mode((640, 480))
    input_box = InputBox(100, 100, 140, 32, _font)
    input_boxes = [input_box]
    done = False
    problems = get_problems()
    current_problem = random.choice(problems)
    result = None
    answers: list[AnswerType] = []

    problem_start = pg.time.get_ticks()

    while not done:
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q and pressed[pg.K_LSHIFT] and pressed[pg.K_LALT]:
                done = True
            for box in input_boxes:
                result = box.handle_event(event)
        
        elapsed_milliseconds = pg.time.get_ticks() - problem_start
        remaining = TIME_LIMIT_SECONDS - (elapsed_milliseconds/1000.0)

        if remaining <= 0 and mode != Mode.BASELINE:
            answers.append(x := make_log_entry(current_problem, None, TIME_LIMIT_SECONDS))
            print(x)
            result = None
            current_problem = random.choice(problems)
        elif result is not None and result != "":
            answers.append(x := make_log_entry(current_problem, int(result), elapsed_milliseconds))
            print(x)
            result = None
            current_problem = random.choice(problems)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        draw_problem(current_problem, screen, _font)
        for box in input_boxes:
            box.draw(screen)
        timer_surface = _font.render(f"Time: {max(0, remaining):.1f}s", True, (255, 255, 255))
        timer_pos = (screen.get_width() - timer_surface.get_width() - 20, 20)
        screen.blit(timer_surface, timer_pos)

        pg.display.flip()
    
    if not os.path.isdir("data"):
        os.mkdir("data")
    with open(os.path.join("data", output_filename), 'w') as f:
        f.write(json.dumps(answers, indent = 4))

if __name__ == "__main__":
    main()