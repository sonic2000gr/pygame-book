#
# Bouncing ball
# Download this source file
# and support files from http://pygamegr.wordpress.com
#

import pygame
from pygame.locals import *
from sys import exit


def getQuit():
  for event in pygame.event.get():
    if event.type == QUIT:
      return True
  return False

def main():
  pygame.init()
  ballimage = 'soccer-ball.png'
  x,y = 100.0,100.0
  xspeed,yspeed = 50,50
  windowsize = (640,480)
  surfacecolor = (50,80,250)
  screen = pygame.display.set_mode(windowsize, DOUBLEBUF)
  ball = pygame.image.load(ballimage)
  ballwidth = ball.get_width()
  ballheight = ball.get_height()
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
    screen.blit(ball, (x, y))
    time = clock.tick()
    thetext = textfont.render(str(1000/time), True, (255,0,0),(255,255,0))
    screen.blit(thetext,(0,0))
    time = time / 1000.0
    distance_x = time * xspeed
    distance_y = time * yspeed
    x = x + distance_x
    y = y + distance_y

    if (x > (640.0-ballwidth) or x<=0.0):
      xspeed = -xspeed
    if (y > (480.0-ballheight) or y<=0.0):
      yspeed = -yspeed
    pygame.display.update()
    endprogram = getQuit()

  pygame.quit()
  exit()

if __name__ == "__main__":
  main()
