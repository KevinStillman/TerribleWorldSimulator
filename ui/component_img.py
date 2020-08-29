import pygame as pg
import sys

pg.init()

class Component_Img(pg.Surface):
    def __init__(self, img_width: int, img_height: int):
        super(Component_Img, self).__init__((img_width, img_height))
        self.img_width = img_width
        self.img_height = img_height
        self.img_coors = (0,0)

    def set_coors(self, xpos: int, ypos: int):
        self.coors = (xpos, ypos)

    def set_screen_dimensions(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def set_img(self, img: pg.Surface):
        self.img = img

        pg.transform.scale(self.img, (self.img_width, self.img_height))

    def scale_img(self, xscale: int, yscale: int):
        pg.transform.scale(self.img, (xscale, yscale))

    def update(self):
        self.fill((0,0,0))
        self.blit(self.img, self.coors)
