import pygame as pg
from pygame.locals import *
import sys

import ui.basic_ui

pg.init()
pg.font.init()

#Display vars
size = screen_width, screen_height = 1920, 1080 #temporary
caption = 'Terrible World Simulator'
display = pg.display
screen = display.set_mode(size, RESIZABLE) #you can also use SCREEN_SIZE
display.set_caption(caption)

#FPS Counter
clock = pg.time.Clock()
font = pg.font.SysFont("Arial",16)

running = True

#image dimesions are 750 x 450
#Home_ui is the basic surface we're blitting all the components to
home_ui = ui.basic_ui.Home_Window( \
    screen_width,              \
    700,                       \
    screen_width,              \
    screen_height              \
) # imgwidth, imgheight, screenwidth, screenheight

while running:
    screen.fill((255,255,255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    #Update the pygame Surfaces
    home_ui.update()

    # blit everything to the screen
    screen.blit(home_ui, (0,0))

    #Updates the Window
    display.update()
