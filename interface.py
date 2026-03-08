from enum import Enum
import os
import random
import sys
import time

from button import Button
from problem_generator import PROBLEM_KEY, SOLUTION_KEY, INCORRECT_KEY_1, INCORRECT_KEY_2
import pygame as pg
import json

USER_ANSWER_KEY = "user_answer"
CORRECT_KEY = "correct"
ANSWERED_KEY = "answered"
TIME_KEY = "time_taken"
TIME_LIMIT_SECONDS = 10
NUM_QUESTIONS = 20

AnswerType = dict[str, str|int|float|None|bool]

class Mode(Enum):
    BASELINE = 0
    LOSS_BASED = 1
    GAIN_BASED = 2

def get_problems(filename: str = "problems.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def get_new_points(current_points: int, mode: Mode, correct: bool|None):
    if correct is None:
        return (current_points - 1) if mode == Mode.GAIN_BASED else current_points
    match mode:
        case Mode.BASELINE: return current_points
        case Mode.LOSS_BASED: return current_points - (correct is False)
        case Mode.GAIN_BASED: return current_points + (correct is True)

def draw_problem(problem: dict[str, str|int], screen: pg.Surface, font: pg.font.Font, location: tuple[int,int] = (50, 50), colour: tuple[int, int, int] = (255, 255, 255)):
    problem_surface = font.render(str(problem[PROBLEM_KEY]), True, colour)
    screen.blit(problem_surface, location)

def make_log_entry(problem: dict[str, str|int], user_answer: int|None, time_taken: float) -> AnswerType:
    prob = problem[PROBLEM_KEY]
    sol = int(problem[SOLUTION_KEY])
    answered = user_answer is not None
    if answered:
        is_correct = user_answer == sol
    else:
        is_correct = False
    
    return {
        PROBLEM_KEY: prob,
        SOLUTION_KEY: sol,
        USER_ANSWER_KEY: user_answer if user_answer is not None else 0,
        CORRECT_KEY: is_correct,
        ANSWERED_KEY: answered,
        TIME_KEY: time_taken
    }

def interface(output_filename: str = "x.test.json", mode: Mode = Mode.BASELINE):
    pg.init()
    _font = pg.font.Font(None, 32)
    screen = pg.display.set_mode((640, 480))
    done = False

    problems = get_problems()
    current_problem = random.choice(problems)
    result = None
    answers: list[AnswerType] = []
    points = 20 if mode == Mode.LOSS_BASED else 0

    choices = [current_problem[SOLUTION_KEY], current_problem[INCORRECT_KEY_1],current_problem[INCORRECT_KEY_2]]
    random.shuffle(choices)

    button1 = Button(x = 100, y = 100, w = 140, h = 32, font = _font, answer = choices[0])
    button2 = Button(x = 100, y = button1.rect.y + button1.rect.h + 100, w = 140, h = 32, font = _font, answer = choices[1])
    button3 = Button(x = 100, y = button2.rect.y + button2.rect.h + 100, w = 140, h = 32, font = _font, answer = choices[2])
    buttons = [button1, button2, button3]

    problem_start = pg.time.get_ticks()

    while not done:
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q and pressed[pg.K_LSHIFT] and pressed[pg.K_LALT]:
                sys.exit(1)
            for button in buttons:
                result = button.handle_event(event)
                if result is not None: break
        
        elapsed_milliseconds = pg.time.get_ticks() - problem_start
        remaining = TIME_LIMIT_SECONDS - (elapsed_milliseconds/1000.0)

        if remaining <= 0 or result is not None:
            time_taken = (TIME_LIMIT_SECONDS if (remaining <= 0 and result is None) else elapsed_milliseconds) 
            answer = make_log_entry(current_problem, result, time_taken)
            answers.append(answer)
            result = None

            points = get_new_points(points, mode, answer[USER_ANSWER_KEY] == answer[SOLUTION_KEY])
            problem_start = pg.time.get_ticks()

            current_problem = random.choice(problems)
            choices = [current_problem[SOLUTION_KEY], current_problem[INCORRECT_KEY_1],current_problem[INCORRECT_KEY_2]]
            random.shuffle(choices)
            for answer, button in zip(choices, buttons):
                button.set_answer(answer)

        
        screen.fill((30, 30, 30))
        draw_problem(current_problem, screen, _font)
        for button in buttons:
            button.draw(screen)
        timer_surface = _font.render(f"Time: {max(0, remaining):.1f}s", True, (255, 255, 255))
        timer_pos = (screen.get_width() - timer_surface.get_width() - 20, 20)
        screen.blit(timer_surface, timer_pos)
        if mode != Mode.BASELINE:
            points_surface = _font.render(f"Points: {points}", True, (255, 255, 255))
            points_pos = (screen.get_width() - points_surface.get_width() - 20, 20 + timer_surface.get_height())
            screen.blit(points_surface, points_pos)

        pg.display.flip()

        if (len(answers) == NUM_QUESTIONS):
            screen.fill((30, 30, 30))
            done_text = _font.render("Test Complete!", True, (0, 255, 0))
            done_pos = (screen.get_width() - done_text.get_width() - 20, 20)
            screen.blit(done_text, done_pos)
            pg.display.flip()
            time.sleep(5)
            done = True
        


    if not os.path.isdir("data"):
        os.mkdir("data")
    with open(os.path.join("data", output_filename), 'w') as f:
        f.write(json.dumps(answers, indent = 4))

if __name__ == "__main__":
    interface()