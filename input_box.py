# Source - https://stackoverflow.com/a/46390412

import pygame as pg
COLOUR_INACTIVE = pg.Color('lightskyblue3')
COLOUR_ACTIVE = pg.Color('dodgerblue2')


class InputBox:
    def __init__(self, x: float, y: float, w: float, h: float, font: pg.font.Font, text : str=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOUR_ACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.font = font

    def handle_event(self, event: pg.event.Event) -> str|None:
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     # If the user clicked on the input_box rect.
        #     if self.rect.collidepoint(event.pos):
        #         # Toggle the active variable.
        #         self.active = not self.active
        #     else:
        #         self.active = False
        #     # Change the current color of the input box.
        #     self.color = COLOUR_ACTIVE if self.active else COLOUR_INACTIVE
        tmp = None
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                tmp = self.text
                self.text = ''
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.unicode.isdigit():
                    self.text += event.unicode
            # Re-render the text.
            self.txt_surface = self.font.render(self.text, True, self.color)
            return tmp

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen: pg.Surface):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

