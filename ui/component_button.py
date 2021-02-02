import pygame
from src.colors import Firebrick, Black
from ui.component_base import Component_Base


class Component_Button(pygame.Surface):
    ''' play button to start the sim '''

    def __init__(self, label: str, button_width: int, button_height: int):
        ''' tws arg is 'self' from the game_loop object '''
        super().__init__((button_width, button_height))

        # just place holders
        self.x_coors, self.y_coors = 0, 0
        self.button_color = Firebrick
        self.text_color = Black
        self.font = pygame.font.SysFont(None, 48, bold=True)
        self.button_label = label
        
        self._build_button(button_width, button_height)

    def set_coors(self, x: int, y: int):
        ''' set buttons x and y position '''
        self.x_coors, self.y_coors = x, y
        self.rect.x = x
        self.rect.y = y

        self.text_rect.center = self.rect.center

    def _build_button(self, width: int, height: int):
        ''' create the button and set its position '''
        self.rect = pygame.Rect(0, 0, width, height)

        self.text = self.font.render(
            self.button_label, True, self.text_color, self.button_color
            )

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

        self.fill(self.button_color)
        self.blit(self.text, self.text_rect)
