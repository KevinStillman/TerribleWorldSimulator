import pygame as pg
import sys

pg.init()

arial = pg.font.SysFont("Arial", 25)

class Home_Window(pg.Surface):
    """docstring for Home_Window."""

    def __init__(self, w: int, h: int, screen_width: int, screen_height: int):
        super(Home_Window, self).__init__((w,h))
        self.w = w
        self.h = h
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.img_width = int( w * .75)
        self.img_height = int( h * .75)
        self.img = pg.image.load('./src/img/worldmap.png')
        self.img = pg.transform.scale(self.img, ( self.img_width, self.img_height))
        self.img_coors = ( (screen_width - self.img_width) / 2, 0)

    def update(self):
        #Draw background
        self.fill((255,255,255))

        #Drawing the Image
        self.blit(self.img, (self.img_coors))

        #Draw the Info tab
        #later we'll need to function to retrieve and parse the trackable stats
        info_tab = arial.render("Lorem Ipsum dolor sit amet...", False, (0,0,0))

        text_bounding_rect = info_tab.get_rect()
        text_bounding_rect.x = 0
        text_bounding_rect.y = self.img_height

        self.blit(info_tab, text_bounding_rect)
