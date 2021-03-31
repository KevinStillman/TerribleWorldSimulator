import pygame as pg

class Component_Base(pg.Surface):
    def __init__(self, width: int, height: int):
        super(Component_Base, self).__init__((width, height))
        self.width = width
        self.height = height

    def set_coors(self, xpos: int, ypos: int):
        self.coors = (xpos, ypos)

    def set_screen_dimensions(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
