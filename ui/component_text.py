import pygame as pg
from ui.component_base import Component_Base
import sys
from math import ceil

from src.colors import Black, White

class Component_Text(Component_Base):
    def __init__(self, text_width: int, text_height: int):
        super(Component_Text, self).__init__(text_width, text_height)
        self.font_size = 25
        self.arial = pg.font.SysFont("Arial", self.font_size)
        self.text_width = text_width
        self.text_height = text_height

    def set_coors(self, xpos: int, ypos: int):
        self.coors = (xpos, ypos)

        self.bounding_rect = self.text.get_rect()
        self.bounding_rect.x = xpos
        self.bounding_rect.y = ypos

    def set_text(self, text: str):
        # NOTE: The text string might become a text bullet list depending on how versatile and stats
        self.text_str = text
        self.text = self.arial.render(text, False, Black)

    def set_fontsize(self, font_size: int):
        self.font_size = font_size
        self.arial = pg.font.SysFont("Arial", font_size)
        self.char_pixel_size = self.arial.size('l')

    def set_border(self, border_width: int = 5):
        self.border_width = border_width
        # Draw border

        pg.draw.line(self, Black, (0,0), (self.screen_width, 0), border_width)
        pg.draw.line(self, Black, (0,0), (0,self.text_height), border_width)
        pg.draw.line(self, Black, (self.screen_width, 0), (self.screen_width, self.text_height), border_width)
        pg.draw.line(self, Black, (0, self.text_height), (self.screen_width, self.text_height), border_width)

    # This cuts words
    def do_text_wrap(self):
        # NOTE: Text wrap functionality will change as the simulation and stats change

        '''NOTE: It's possible many high computing fucntions in c++ instead of python for quicker run-time '''
        text_lines = []
        currlinesize = 0
        currline = ''
        for char in self.text_str:
            currlinesize += self.char_pixel_size[0]

            if currlinesize >= self.screen_width:
                text_lines.append(currline)
                currline = ''
                currlinesize = 0

            currline += char
            currlinesize += self.char_pixel_size[0]
        text_lines.append(currline)

        # Render all the text lines
        line_height = ceil(self.char_pixel_size[1])
        for ind,i in enumerate(text_lines):
            # print(i)
            txt = self.arial.render(i, False, Black)
            self.blit(txt, txt.get_rect(topleft=(0, line_height * ind)))

        # exit()

    def update(self):
        self.fill(White)

        self.do_text_wrap()
        # self.blit(self.text, self.text.get_rect())
        self.set_border()
