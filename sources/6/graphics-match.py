#
# Graphics Match
# Adapted from the TI-99/4A original
# Download this source file and game support files
# from http://pygamegr.wordpress.com

import pygame
from pygame.locals import *
from random import randint
from sys import exit

class Spinner:
  def __init__(self,images):
    self.slot=[]
    for image in images:
      self.slot.append(pygame.image.load(image))

  def Spin(self, surface, x, y, framerate, clock):
    for draws in range(0,50):
      self.luck = (randint(0,5),randint(0,5), randint(0,5))
      x1=x
      for i in self.luck:
        surface.blit(self.slot[i], (x1, y))
        x1 = x1 + self.slot[i].get_width() + 3
      pygame.display.update()
      time = clock.tick(framerate)

  def GetScore(self):
    if self.luck[0] == self.luck[1] == self.luck[2]:
      points = 75
    elif self.luck[0] == self.luck[1]:
      if self.luck[0] in [0,1,2]:
        points = 40
      else:
        points = 10
    elif self.luck[0] == self.luck[2]:
      points = 10
    else:
      points = -10
    return points

#
# Initialize the pygame library
#

pygame.init()

#
# Leftmost image position
#

x = 126.0
y = 100.0

#
# Define a modest window size
#

screenwidth = 640
screenheight = 480

#
# Load slot images from files and init
# slotmachine, an object of the Spinner class
#

slot_images = ('lemon.jpg','bar.jpg','cherry.jpg','bell.jpg','raspberry.jpg','seven.jpg')
slotmachine = Spinner(slot_images)

#
# Initialize screen and caption
#

screen = pygame.display.set_mode((screenwidth, screenheight), 0, 32)
pygame.display.set_caption("Graphics Match 2012")

#
# Screen color is basically blue
#

surfacecolor = (50,80,250)
screen.fill(surfacecolor)

#
# Setup some fonts and text messages
#

font = pygame.font.SysFont("impact",32)
header_text = font.render("Graphics Match - 2012", True, (255,0,0),(255,255,0))
keys_text = font.render("Press [SPACE] to Play, Q to quit", True, (255,255,255))

#
# Create a Clock object and set framerate variable for  ticks
#

clock = pygame.time.Clock()
framerate = 25

#
# Show info message
#

screen.blit(header_text,(175,20))
screen.blit(keys_text,(125,350))

#
# Initialize score value and position
# Zero is actually a good score for this game,
# just play for a while and you'll see...
#

score = 0
scorex = 120
scorey = 300

#
# Enter main game loop
#

endgame = False
spacepressed = True
while not endgame:
  for event in pygame.event.get():
    if event.type == QUIT:
      endgame = True
    if event.type == KEYDOWN:
      keyboardinput = event.key
      if keyboardinput == K_q:
        endgame = True
      if keyboardinput == K_SPACE:
        spacepressed = True

  if spacepressed:
    slotmachine.Spin(screen,x,y,framerate,clock)
    score += slotmachine.GetScore()

  scoretext = font.render("Score:  "+str(score),True,(255,255,255))
  pygame.draw.rect(screen,(255,0,0),(scorex,scorey,400,40))
  screen.blit(scoretext,(scorex,scorey))
  pygame.display.update()
  spacepressed = False

pygame.quit()
exit()
