import pygame as pg
from pygame.locals import *
from game_settings import Settings
import sys

import ui.basic_ui


class Terrible_World_Simulator:
    ''' The main loop for the sim '''

    def __init__(self):
        pg.init()
        pg.font.init()

        # init our settings
        self.settings = Settings(self)

        # FPS Counter
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 16)

        self.display = pg.display
        # you can also use SCREEN_SIZE
        self.screen = self.display.set_mode(self.settings.size, RESIZABLE)
        self.display.set_caption(self.settings.caption)

        self.running = True

        # image dimesions are 750 x 450
        # Home_ui is the basic surface we're blitting all the components to
        self.home_ui = ui.basic_ui.Home_Window(
            self.settings.screen_width,
            700,
            self.settings.screen_width,
            self.settings.screen_height
        )  # imgwidth, imgheight, screenwidth, screenheight

    def _check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def run_sim(self):
        ''' run the game '''

        while self.running:
            # set the pace of the game
            self.clock.tick(self.settings.game_pace)
            self.screen.fill(self.settings.background_color)
            self._check_for_events()

            # Update the pygame Surfaces
            self.home_ui.update()

            # blit everything to the screen
            self.screen.blit(self.home_ui, (0, 0))

            # Updates the Window
            self.display.update()


# if this file is the one that the program is executed from.
if __name__ == "__main__":
    terrible_world_sim = Terrible_World_Simulator()
    terrible_world_sim.run_sim()
