import pygame as pg
import sys

from src.colors import White, Black, Light_black

from ui.component_img import Component_Img
from ui.component_text import Component_Text
from ui.component_button import Component_Button


class Home_Window(pg.Surface):
    """docstring for Home_Window."""

    def __init__(self, w: int, h: int, screen_width: int, screen_height: int):
        w, h = int(w), int(h)
        super(Home_Window, self).__init__((w, h))
        self.w = w
        self.h = h
        self.screen_width = screen_width
        self.screen_height = screen_height

        # load our image and font
        self._load_assets()
        # load buttons
        self._load_buttons()

        self.img = Component_Img(int(w * 0.75), int(h * 0.75))
        self.img.set_img(self.worldmap)
        # Centers the image
        self.img.set_coors((screen_width - self.img.img_width) / 2 + 50, 0)

        self.text = Component_Text(screen_width, int(screen_height * 0.33))
        self.text.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        )
        self.text.set_coors(0, self.img.img_height - 200)
        self.text.set_fontsize(25)
        self.text.set_screen_dimensions(screen_width, screen_height)

    def _load_buttons(self):
        """
        Load and set positions of the ui buttons
        play, stop, pause
        """
        self.play_button = Component_Button("Play", 150, 50)
        self.play_button.set_position(
            610, self.screen_height - 130
        )  #  WIN >>was 610, self.screen_height-80

        self.stop_button = Component_Button(
            "Stop", 150, 50
        )  # On Macbook, buttons were cut off so
        self.stop_button.set_position(
            910, self.screen_height - 130
        )  # the coords were changed from -80 to

        self.pause_button = Component_Button("Pause", 150, 50)  # -130
        self.pause_button.set_position(1210, self.screen_height - 130)

    def _load_assets(self):
        self.arial = pg.font.SysFont("Arial", 25)
        try:
            self.worldmap = pg.image.load("./src/img/worldmap.png")
        except:
            print("World map loading error.")

    # def resize(self, new_width: int, new_height: int):
    #     oldw = self.w
    #     oldh = self.h
    #     self.__init__(self.w * new_width / 1920, self.h * new_height / 1080, self.w, self.h)
    #     self.img.scale_img(self.w // oldw, self.h // oldh)

    def check_buttons(self, mouse_pos):

        if self.play_button.rect.collidepoint(mouse_pos):
            print("Play button pressed!")
        elif self.stop_button.rect.collidepoint(mouse_pos):
            print("Stop button pressed!")
        elif self.pause_button.rect.collidepoint(mouse_pos):
            print("Pause button pressed!")

    def _blit_buttons(self):
        self.blit(self.play_button, self.play_button.rect)
        self.blit(self.stop_button, self.stop_button.rect)
        self.blit(self.pause_button, self.pause_button.rect)

    def _blit_ui_text(self):
        """
        Draw the Info tab
        later we'll need to function to retrieve and parse the trackable stats
        """
        self.text.update()
        self.blit(self.text, self.text.bounding_rect)

    def _blit_ui_img(self):
        """
        Draw ui map image
        """
        self.img.update()
        self.blit(self.img, (self.img.coors))

    def _blit_ui_components(self):
        """
        blit the ui components in the order called
        """
        self._blit_ui_img()
        self._blit_ui_text()
        self._blit_buttons()

    def update(self):
        # Draw background
        self.fill(Light_black)
        self._blit_ui_components()
