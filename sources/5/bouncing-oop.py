#
# Bouncing ball - OOP :)
#

import pygame
from pygame.locals import *
import random
from sys import exit

class Ball:
  def __init__(self,theImage,x,y,xspeed,yspeed):
    self.ballimage = theImage
    self.x = x
    self.y = y
    self.xspeed = xspeed
    self.yspeed = yspeed
    self.shape = pygame.image.load(theImage)
        
  def Show(self,surface):
    surface.blit(self.shape, (self.x, self.y))
        
  def GetWidth(self):
    return self.shape.get_width()
    
  def GetHeight(self):
    return self.shape.get_height()

  def Move(self, time):
    distance_x = time * self.xspeed
    distance_y = time * self.yspeed
    self.x = self.x + distance_x
    self.y = self.y + distance_y
        
  def IsOutofX(self,xmin,xmax):
    if (self.x >= (xmax - self.GetWidth()) or self.x <= xmin):
      return True
    else:
      return False
        
  def IsOutofY(self,ymin,ymax):
    if (self.y >= (ymax - self.GetHeight()) or self.y <= ymin):
      return True
    else:
      return False
        
def getQuit():
  for event in pygame.event.get():
    if event.type == QUIT:
      return True
  return False

def main():
  pygame.init()
  ballimage = 'soccer-ball.png'
  balls=[]
  for i in range(0,8):
    x = random.randint(80,500)
    y = random.randint(80,400)
    xspeed = 0
    while (xspeed >= -5 and xspeed <= 5):
      xspeed = random.randint(-50,50)
    yspeed = 0
    while (yspeed >= -5 and yspeed <=5):
      yspeed = random.randint(-50,50)
    balls.append(Ball(ballimage,x,y,xspeed,yspeed))
  windowsize = (640,480)
  surfacecolor = (50,80,250)
  screen = pygame.display.set_mode(windowsize, DOUBLEBUF)
  clock = pygame.time.Clock()

  # Uncomment the framerate line and change
  # time = clock.tick() in main loop to
  # time = clock.tick(framerate)
  # to limit the animation to a specific framerate

  #framerate = 30

  textfont = pygame.font.SysFont("Arial",24)

  #
  # Main loop
  #

  endprogram = False
  while not endprogram:
    screen.fill(surfacecolor)
    for theball in balls:
      theball.Show(screen)
    time = clock.tick()
    thetext = textfont.render(str(1000/time), True, (255,0,0),(255,255,0))
    screen.blit(thetext,(0,0))
    time = time / 1000.0
    for theball in balls:
      theball.Move(time)
      if theball.IsOutofX(0,640):
        theball.xspeed = -theball.xspeed
      if theball.IsOutofY(0,480):
        theball.yspeed = -theball.yspeed
    pygame.display.update()
    endprogram = getQuit()

  pygame.quit()
  exit()

if __name__ == "__main__":
  main()
