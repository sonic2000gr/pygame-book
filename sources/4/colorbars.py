#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()
screen = pygame.display.set_mode((640, 480), DOUBLEBUF)

while True:
  ypos=0
  for ypos in range(0,479,30):
    for xpos in range(0,639,30):
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
      the_pos=(xpos,ypos,29,29)
      random_color = (randint(0,255), randint(0,255), randint(0,255))
      pygame.draw.rect(screen, random_color, the_pos)
  pygame.display.update()
