# example base

import pygame as pg
import sys

pg.init()

#Display vars
size = width,height = 1000,1000 #temporary
caption = 'Terrible World Simulator'
screen = pg.display.set_mode(size)
pg.display.set_caption(caption)

running = True

while running:
    screen.fill((255,255,255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    pg.display.update()
