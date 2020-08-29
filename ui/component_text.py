import pygame as pg
from ui.component_base import Component_Base
import sys

from src.colors import Black, White

class Component_Text(Component_Base):
    def __init__(self, text_width: int, text_height: int):
        super(Component_Text, self).__init__(text_width, text_height)
        self.arial = pg.font.SysFont("Arial", 25)
        self.text_width = text_width
        self.text_height = text_height

    def set_coors(self, xpos: int, ypos: int):
        self.coors = (xpos, ypos)

        self.bounding_rect = self.text.get_rect()
        self.bounding_rect.x = xpos
        self.bounding_rect.y = ypos

    def set_text(self, text: str):
        self.text = self.arial.render(text, False, (0, 0, 0))

    def set_border(self, border_width: int = 5):
        self.border_width = border_width
        # Draw border

        pg.draw.line(self, Black, (0,0), (self.screen_width, 0), border_width)
        pg.draw.line(self, Black, (0,0), (0,self.text_height), border_width)
        pg.draw.line(self, Black, (self.screen_width, 0), (self.screen_width, self.text_height), border_width)
        pg.draw.line(self, Black, (0, self.text_height), (self.screen_width, self.text_height), border_width)

    def do_text_wrap(self):
        pass

    def update(self):
        self.fill(White)

        self.blit(self.text, self.text.get_rect())
        self.set_border()
