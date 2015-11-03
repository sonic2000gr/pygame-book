#
# Pygame Invaders
# Loosely Adapted from more
# than one TI-99/4A original games
# Stage 1 - Basic craft motion
#

import pygame
import os
from pygame.locals import *
from random import randint
from sys import exit

# A function for the background music

def PlayMusic(soundfile):
  pygame.mixer.music.load(soundfile)
  pygame.mixer.music.play(-1)

# The superclass for both our ship and the aliens

class Craft(object):
  def __init__ (self, imagefile, coord):
    self.shape = pygame.image.load(imagefile)
    self.ship_width = self.shape.get_width()
    self.ship_height = self.shape.get_height()
    self.rect = pygame.Rect(coord,(self.ship_width, self.ship_height))

  def Show(self, surface):
    surface.blit(self.shape,(self.rect[0],self.rect[1]))

  def Move(self,speed_x,speed_y, time):
    distance_x = speed_x * time
    distance_y = speed_y * time
    self.rect.move_ip(distance_x,distance_y)

  def Fire(self):
    pass


# The class for our ship

class SpaceCraft(Craft):
  pass

# This is the class for the scrolling background

class SpaceBackground:
  def __init__(self, coord, imagefile):
    self.shape = pygame.image.load(imagefile)
    self.coord = coord

  def Show(self, surface):
    surface.blit(self.shape,self.coord)

  def Scroll(self, speed_y, time):
    pass


# Initialize pygame library

pygame.init()

# Screen size and initial spaceship position

screenwidth,screenheight = (480,640)
spaceship_pos = (240, 540)

# Initialize screen and set caption

screen = pygame.display.set_mode((screenwidth,screenheight), DOUBLEBUF, 32)
pygame.display.set_caption("Pygame Invaders")

# Set keyboard repeat to super fast / delay to minimum

pygame.key.set_repeat(1,1)

# Initialize the background and spaceship objects

StarField = SpaceBackground((0,0), "stars.jpg")
SpaceShip = SpaceCraft("spaceship2.png",spaceship_pos)

# Start the background music

PlayMusic("spaceinvaders.ogg")

# Initialize the clock object and set framerate

clock = pygame.time.Clock()
framerate = 60

while True:
  time = clock.tick(framerate)/1000.0

  # shipspeed is zeroed at every cycle of the loop

  shipspeed_x = 0
  shipspeed_y = 0
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      # This returns a list of True/False where the index is the
      # code of the key pressed. Fortunately pygame.locals provides
      # symbolics for these codes
      key = pygame.key.get_pressed()
      if key[K_q]:
        pygame.quit()
        exit()
      if key[K_LEFT]:
        shipspeed_x = -300
      if key[K_RIGHT]:
        shipspeed_x = 300

  # Move the SpaceShip by the specified amount

  SpaceShip.Move(shipspeed_x, shipspeed_y, time)

  # Show all the objects, background first (or it will erase everything else!)

  StarField.Show(screen)
  SpaceShip.Show(screen)
  pygame.display.update()
