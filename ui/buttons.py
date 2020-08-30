import pygame.font
from src.colors import Crimson
from src.colors import Black
from ui.component_base import Component_Base


class PlayButton:
    ''' play button to start the sim '''

    def __init__(self, baseui):
        ''' tws arg is 'self' from the game_loop object '''
        self.screen = baseui
        self.screen_rect = baseui.screen_width, baseui.screen_height
        # just place holders
        self.x_coors, self.y_coors = 0, 0
        self.width, self.height = 150, 50
        self.button_color = Crimson
        self.text_color = Black
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self._build_button()

    def set_coors(self, x: int, y: int):
        ''' set buttons x and y position '''
        self.x_coors, self.y_coors = x, y

    def _build_button(self):
        ''' crate the button and set its position '''
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.text_image = self.font.render(
            "Play", True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        ''' draw button to screen '''

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
