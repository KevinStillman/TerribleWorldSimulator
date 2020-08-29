import pygame as pg
import sys

from ui.component_img import Component_Img
from ui.component_text import Component_Text


class Home_Window(pg.Surface):
    """docstring for Home_Window."""

    def __init__(self, w: int, h: int, screen_width: int, screen_height: int):
        super(Home_Window, self).__init__((w, h))
        self.w = w
        self.h = h
        self.screen_width = screen_width
        self.screen_height = screen_height

        # load our image and font
        self._load_assets()

        self.img = Component_Img(int(w * .75), int(h * .75))
        self.img.set_img(self.worldmap)
        # Centers the image
        self.img.set_coors((screen_width - self.img.img_width) / 2 + 50, 0)

        self.text = Component_Text(screen_width, int(screen_height * .33))
        self.text.set_text("Lorem ipsum.")
        self.text.set_coors(0, self.img.img_height)

    def _load_assets(self):
        self.arial = pg.font.SysFont("Arial", 25)
        try:
            self.worldmap = pg.image.load('./src/img/worldmap.png')
        except:
            print("World map loading error.")

    def update(self):
        # Draw background
        self.fill((255, 255, 255))

        # Drawing the Image
        self.img.update()
        self.blit(self.img, (self.img.coors))

        # Draw the Info tab
        # later we'll need to function to retrieve and parse the trackable stats
        self.text.update()
        self.blit(self.text, self.text.bounding_rect)
