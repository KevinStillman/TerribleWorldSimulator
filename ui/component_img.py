import pygame as pg
from ui.component_base import Component_Base
import sys

from src.colors import Black

class Component_Img(Component_Base):
    def __init__(self, img_width: int, img_height: int):
        super(Component_Img, self).__init__(img_width, img_height)
        self.img_width = img_width
        self.img_height = img_height
        self.img_coors = (0, 0)

    # Base method
    # def set_coors(self, xpos: int, ypos: int):
    #     self.coors = (xpos, ypos)

    # Base Method
    # def set_screen_dimensions(self, screen_width: int, screen_height: int):
    #     self.screen_width = screen_width
    #     self.screen_height = screen_height

    def set_img(self, img: pg.Surface):
        self.img = img

        pg.transform.scale(self.img, (self.img_width, self.img_height))

    def scale_img(self, xscale: int, yscale: int):
        pg.transform.scale(self.img, (xscale, yscale))

    def update(self):
        self.fill(Black)
        self.blit(self.img, self.coors)
