import pygame as pg
from src.colors import Black, White, Red, Crimson
from ui.component_base import Component_Base

class Component_Button2(Component_Base):
    ''' play button to start the sim '''

    def __init__(self, button_width: int, button_height: int):
        ''' tws arg is 'self' from the game_loop object '''
        super(Component_Button, self).__init__(button_width, button_height)

        # just place holders
        self.x_coors, self.y_coors = 0, 0
        self.button_width = button_width
        self.button_height = button_height
        self.button_color = Crimson
        self.text_color = Black
        self.font = pg.font.SysFont("Arial", 48, bold=True)

    def set_label(self, label: str):
        #For the text and background
        self.label = label
        self.text = self.font.render(label, False, self.text_color, self.button_color)
        self.text_rect = self.text.get_rect()

        #For the inflated box
        self.box = pg.Rect(0,0,self.button_width, self.button_height)
        self.box.center = self.text_rect.center
        self.box.fill(self.button_color)

    def set_coors(self, x: int, y: int):
        ''' set buttons x and y position '''
        self.x_coors, self.y_coors = x, y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        ''' draw button to screen '''

        self.blit(self.box)
        self.blit(self.text)
