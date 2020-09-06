import pygame.font
from src.colors import Firebrick, Black
from ui.component_base import Component_Base


class Component_Button(Component_Base):
    ''' play button to start the sim '''

    def __init__(self, label: str, button_width: int, button_height: int, baseui):
        ''' tws arg is 'self' from the game_loop object '''
        super(Component_Button, self).__init__(button_width, button_height)

        self.screen = baseui
        self.screen_rect = baseui.screen_width, baseui.screen_height
        # just place holders
        self.x_coors, self.y_coors = 0, 0
        self.button_color = Firebrick
        self.text_color = Black
        self.font = pygame.font.SysFont(None, 48, bold=True)
        self.button_label = label

        self._build_button()

    def set_coors(self, x: int, y: int):
        ''' set buttons x and y position '''
        self.x_coors, self.y_coors = x, y
        self.rect.x = x
        self.rect.y = y

        self.text_rect.center = self.rect.center

    def _build_button(self):
        ''' create the button and set its position '''
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.text = self.font.render(
            self.button_label, True, self.text_color, self.button_color)

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def draw_button(self):
        ''' draw button to screen '''

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text, self.text_rect)
