import pygame as pg
from input_box import COLOUR_INACTIVE, COLOUR_ACTIVE

class Button:
    def __init__(self, x: float, y: float, w: float, h: float, font: pg.font.Font, answer: int = 0) -> None:
        self.rect = pg.Rect(x, y, w, h)
        self.active = False
        self.color = COLOUR_INACTIVE
        self.answer = answer
        self.txt_surface = font.render(str(self.answer), True, self.color)
        self.font = font
    
    def handle_event(self, event: pg.event.Event) -> int|None:
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOUR_ACTIVE if self.active else COLOUR_INACTIVE
        elif event.type == pg.MOUSEBUTTONUP:   # don't actually register a press until they release
            self.active = False
            self.color = COLOUR_INACTIVE
            if self.rect.collidepoint(event.pos):
                return self.answer
    
    def set_answer(self, answer: int):
        self.answer = answer

    def draw(self, screen: pg.Surface):
        self.txt_surface = self.font.render(str(self.answer), True, self.color)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)