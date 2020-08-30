import pygame as pg
import sys

from src.colors import White, Black

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

        self.img = Component_Img(int(w * .75), int(h * .75))
        self.img.set_img(self.worldmap)
        # Centers the image
        self.img.set_coors((screen_width - self.img.img_width) / 2 + 50, 0)

        self.text = Component_Text(screen_width, int(screen_height * .33))
        self.text.set_text("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        self.text.set_coors(0, self.img.img_height)
        self.text.set_fontsize(25)
        self.text.set_screen_dimensions(screen_width, screen_height)

    def _load_buttons(self):
        self.play_button = Component_Button("Play", 150, 50, self)
        self.play_button.set_coors(10, 450)
        self.stop_button = Component_Button("Stop", 150, 50, self)
        self.stop_button.set_coors(210, 450)
        self.pause_button = Component_Button("Pause", 150, 50, self)
        self.pause_button.set_coors(410, 450)

    def _load_assets(self):
        self.arial = pg.font.SysFont("Arial", 25)
        try:
            self.worldmap = pg.image.load('./src/img/worldmap.png')
        except:
            print("World map loading error.")

    # def resize(self, new_width: int, new_height: int):
    #     oldw = self.w
    #     oldh = self.h
    #     self.__init__(self.w * new_width / 1920, self.h * new_height / 1080, self.w, self.h)
    #     self.img.scale_img(self.w // oldw, self.h // oldh)

    def check_buttons(self):
        mouse_position = pg.mouse.get_pos()

        if (button_clicked := self.play_button.rect.collidepoint(mouse_position)):
            print("Play button pressed!")
        elif (button_clicked := self.stop_button.rect.collidepoint(mouse_position)):
            print("Stop button pressed!")
        elif (button_clicked := self.pause_button.rect.collidepoint(mouse_position)):
            print("Pause button pressed!")

    def update(self):
        # Draw background
        self.fill(White)

        # Drawing the Image
        self.img.update()
        self.blit(self.img, (self.img.coors))

        # Draw play button
        self.play_button.draw_button()
        self.stop_button.draw_button()
        self.pause_button.draw_button()

        # Draw the Info tab
        # later we'll need to function to retrieve and parse the trackable stats
        self.text.update()
        self.blit(self.text, self.text.bounding_rect)
