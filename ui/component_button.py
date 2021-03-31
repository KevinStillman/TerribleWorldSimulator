import pygame
from src.colors import Firebrick, Black
from ui.component_base import Component_Base


class Component_Button(Component_Base):
    """ play button to start the sim """

    def __init__(self, label: str, button_width: int, button_height: int):
        """
        Creating a button requires a label and the buttons dims
        """
        super().__init__(button_width, button_height)

        # just place holders
        self.x_coors, self.y_coors = 0, 0
        self.button_color = Firebrick
        self.text_color = Black
        self.font = pygame.font.SysFont(None, 48, bold=True)
        self.button_label = label

        self._build_button(button_width, button_height)

    def set_position(self, x: int, y: int):
        """ set buttons x and y position """
        # call the parent method to set the coors then add code to set text position
        self.set_coors(x, y)
        # set position from coors which is stored in the parent class
        self.rect.x = self.coors[0]
        self.rect.y = self.coors[1]
        self.text_rect.center = self.rect.center
    
    def set_new_label(self, label: str=None):
        """ Set a new label for the button """
        # if there is no label passed
        # use the label string we got from the constructor
        if not label:
            self.text = self.font.render(
                self.button_label, True, self.text_color, self.button_color
            )
        else:
            self.text = self.font.render(
                label, True, self.text_color, self.button_color
            )

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center


    def _build_button(self, width: int, height: int):
        """ create the button and set its position """
        self.rect = pygame.Rect(0, 0, width, height)
        self.set_new_label()
        self.fill(self.button_color)
        self.blit(self.text, self.text_rect)
