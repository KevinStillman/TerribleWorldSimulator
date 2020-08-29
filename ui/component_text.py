import pygame as pg
import sys

pg.init()

arial = pg.font.SysFont("Arial",25)

class Component_Text(pg.Surface):
    def __init__(self, text_width: int, text_height: int):
        super(Component_Text, self).__init__((text_width, text_height))
        self.text_width = text_width
        self.text_height = text_height

    def set_coors(self, xpos: int, ypos: int):
        self.coors = (xpos, ypos)

        self.bounding_rect = self.text.get_rect()
        self.bounding_rect.x = xpos
        self.bounding_rect.y = ypos

    def set_text(self, text: str, text_font = arial):
        self.text = text_font.render(text, False, (0,0,0))

    def update(self):
        self.fill((255,255,255))
        self.blit(self.text, self.text.get_rect())
