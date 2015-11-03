#
# Pygame Invaders
# Loosely Adapted from more
# than one TI-99/4A original games
# Final Stage - Invasion has began!
# Download this source file and game support files
# from http://pygamegr.wordpress.com

import pygame
import os
from pygame.locals import *
from random import randint
from sys import exit

# Center Message on surface, used for blitting info text

def CenterMessage(screen, surface):
  return (screen.get_width() - surface.get_width())/2

# A function for the background music

def PlayMusic(soundfile):
  pygame.mixer.music.load(soundfile)
  pygame.mixer.music.play(-1)

# A function for the sound effects

def PrepareSound(filename):
    sound = pygame.mixer.Sound(filename)
    return sound

# The superclass for both our ship and the aliens

class Craft(object):
  def __init__ (self, imagefiles, coord):
    self.shape = [pygame.image.load(imagefile) for imagefile in imagefiles]
    self.ship_width = self.shape[0].get_width()
    self.ship_height = self.shape[0].get_height()
    self.rect = pygame.Rect(coord,(self.ship_width, self.ship_height))
    self.ship_midwidth = self.ship_width / 2
    self.firecolor=(255,0,0)
    self.firespeed = -800
    self.shotlength = 20

  def Show(self, surface,imageindex):
    surface.blit(self.shape[imageindex],(self.rect[0],self.rect[1]))

  def Move(self,speed_x,speed_y, time):
    distance_x = speed_x * time
    distance_y = speed_y * time
    self.rect.move_ip(distance_x,distance_y)

  def Fire(self):
    shot = Laser((self.rect[0]+self.ship_midwidth, self.rect[1]),
                  self.firecolor,self.shotlength,self.firespeed,self.rect[1],15)
    return shot

#
# Alien is used to create AlienShips (really?)
#

class Alien(Craft):
  def __init__(self, imagefile, coord, speed_x, speed_y):
    imagefiles = (imagefile,)
    super(Alien, self).__init__(imagefiles, coord)
    self.speed_x = speed_x
    self.speed_y = speed_y
    self.shot_height = 10
    self.firebaseline = self.ship_height
    self.firecolor=(255,255,0)
    self.firespeed = 200

  def Move(self, time):
    super(Alien,self).Move(self.speed_x, self.speed_y,time)
    if self.rect[0] >= 440 or self.rect[0] <= 10:
      self.speed_x = -self.speed_x
    if self.rect[1] <= 10 or self.rect[1] >= 440:
      self.speed_y = -self.speed_y

  def Fire(self):
    theshot = Laser((self.rect[0]+self.ship_midwidth,
                     self.rect[1]+self.firebaseline),self.firecolor,
                     self.shot_height,
                     self.firespeed,self.rect[1]+self.firebaseline, 0)
    return theshot

  def Show(self, surface):
    imageindex = 0
    super(Alien,self).Show(surface,imageindex)

# The class for our ship

class SpaceCraft(Craft):
  def __init__ (self, imagefile, coord, min_coord, max_coord,lasersound):
    super(SpaceCraft,self).__init__(imagefile,coord)
    self.min_coord = min_coord
    self.max_coord = (max_coord[0]-self.ship_width, max_coord[1]-self.ship_height)
    self.lasersound = lasersound

  def Move(self, speed_x, speed_y, time):
    super(SpaceCraft,self).Move(speed_x, speed_y, time)
    for i in (0,1):
      if self.rect[i] < self.min_coord[i]:
        self.rect[i] = self.min_coord[i]
      if self.rect[i] > self.max_coord[i]:
        self.rect[i] = self.max_coord[i]

  def Fire(self):
    self.lasersound.play()
    return super(SpaceCraft,self).Fire()

# This is the class for the scrolling background

class SpaceBackground:
  def __init__(self, screenheight, imagefile):
    self.shape = pygame.image.load(imagefile)
    self.coord = [0,0]
    self.coord2 = [0, -screenheight]
    self.y_original = self.coord[1]
    self.y2_original = self.coord2[1]

  def Show(self, surface):
    surface.blit(self.shape, self.coord)
    surface.blit(self.shape, self.coord2)

  def Scroll(self, speed_y, time):
    distance_y = speed_y * time
    self.coord[1] += distance_y
    self.coord2[1] += distance_y
    if self.coord2[1] >= 0:
      self.coord[1] = self.y_original
      self.coord2[1] = self.y2_original

#
# Laser class
#

class Laser:
  def __init__(self, coord, color, size, speed, refline, voffset):
    self.x1 = coord[0]
    self.y1 = coord[1] + voffset
    self.size = size
    self.color = color
    self.speed = speed
    self.refline = refline

  def Show(self, surface):
    pygame.draw.line(surface, self.color, (self.x1, self.y1),(self.x1,self.y1-self.size),3)

  def Move(self, time):
    distance = self.speed * time
    self.y1 += distance

  def DistanceTravelled(self):
    return abs(self.refline - self.y1)

  def GoneAbove(self,y):
    if self.y1<=y:
      return True
    else:
      return False

  def GoneBelow(self,y):
    if self.y1>=y:
      return True
    else:
      return False

  def GetXY(self):
    return (self.x1, self.y1)

#
# ScoreBoard - Score keeping and display
#

class ScoreBoard:
  def __init__(self,x,y,font,fontsize):
    self.x = x
    self.y = y
    self.font = pygame.font.SysFont(font,fontsize)
    self.score = 0

  def Change(self, amount):
    self.score += amount

  def Show(self,surface):
    scoretext = self.font.render("Score: "+str(self.score), True, (0,0,255))
    surface.blit(scoretext,(self.x, self.y))

  def GetValue(self):
    return self.score

  def SetValue(self, score):
    self.score = score

#
# ShieldMeter - Keep and display vintage style bar shield meter
#

class ShieldMeter:
  def __init__(self, x, y, maxvalue, warnvalue):
    self.x = x
    self.y = y
    self.maxvalue = maxvalue
    self.currentvalue = maxvalue
    self.warnvalue = warnvalue

  def Show(self, surface):
    if self.currentvalue < self.warnvalue:
      self.shieldcolor = (255,0,0)
    else:
      self.shieldcolor = (0,255,0)
    pygame.draw.rect(surface,self.shieldcolor,(self.x, self.y, self.currentvalue,25))

  def Increase(self, amount):
    self.currentvalue += amount
    if self.currentvalue > self.maxvalue:
      selfcurrentvalue = self.maxvalue

  def Decrease(self, amount):
    self.currentvalue -= amount
    if self.currentvalue < 0:
      self.currentvalue = 0

  def GetValue(self):
    return self.currentvalue

  def SetValue(self,value):
    self.currentvalue = value
    if self.currentvalue > self.maxvalue:
      self.currenvalue = self.maxvalue
    if self.currentvalue < 0:
      self.currentvalue = 0

#
# Simple function to display message for Game Over
#

def GameOverShow(screen):
  font = pygame.font.SysFont("impact", 32)
  gameovertext = font.render("Game Over!",True,(255,255,255))
  text_x = CenterMessage(screen, gameovertext)
  screen.blit (gameovertext,(text_x,280))
  gameovertext = font.render("Press R to Restart", True, (255,255,255))
  text_x = CenterMessage(screen, gameovertext)
  screen.blit(gameovertext,(text_x,320))
  return

#
# Main function, program entry point
#

def main():
  # Initialize pygame library and OS environment
  #The following will center the game window on the screen

  os.environ['SDL_VIDEO_CENTERED']='1'
  pygame.init()

  # Screen size and initial spaceship position

  screenwidth,screenheight = (480,640)
  spaceship_pos = (240, 540)

  # Initialize screen and set caption

  screen = pygame.display.set_mode((screenwidth,screenheight), DOUBLEBUF, 32)
  pygame.display.set_caption("Pygame Invaders")

  # Set keyboard repeat to super fast / delay to minimum

  pygame.key.set_repeat(1,1)

  # Prepare Sound Effects

  laser = PrepareSound("shoot.wav")
  explosion = PrepareSound("invaderkilled.wav")
  destroyed = PrepareSound("explosion.wav")

  # Initialize the background and spaceship objects

  spaceship_low = (0,0)
  spaceship_high = (screenwidth, screenheight)
  StarField = SpaceBackground(screenheight, "stars.jpg")
  shipimages = ('spaceship2.png', 'spaceship3.png')
  SpaceShip = SpaceCraft(shipimages,spaceship_pos, spaceship_low, spaceship_high,laser)

  # Initialize fire lists (ours and aliens)

  firelist=[]
  alienfirelist = []

  # Set the background scrolling speed

  backspeed = 100

  # Initialize some objects and game variables

  score = ScoreBoard(0,0,"impact",32)
  shield = ShieldMeter(200,10,250,75)
  laserdownlimit = screenheight - 40
  GameOver = False

  # Start the background music

  PlayMusic("spaceinvaders.ogg")

  # Images used for the aliens

  alienimage=('alien1.png','alien2.png','alien3.png','alien4.png','alien5.png')

  # Number of aliens per 'wave'

  numofaliens = 8
  AlienShips = []

  # Initialize the clock object and set framerate

  clock = pygame.time.Clock()
  framerate = 60

  # imageindex & flashcount used for alternating between normal
  # and 'hit' images

  imageindex = 0
  flashcount = 0

  while True:
    time = clock.tick(framerate)/1000.0

    if not AlienShips:
      # AlienShips empty means we need to create new 'wave'
      AlienShips = [ Alien(alienimage[randint(0,len(alienimage)-1)],
                          [randint(20,screenwidth-80),
                           randint(20,screenheight-140)],randint(100,150),
                          randint(100,150)) for i in range(0,numofaliens) ]

    # shipspeed is zeroed at every cycle of the loop
    shipspeed_x = 0
    shipspeed_y = 0
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()

      if event.type == USEREVENT + 1:
        if flashcount < 10:
          flashcount += 1
          if imageindex == 1:
            imageindex = 0
          else:
            imageindex = 1
        else:
          imageindex = 0
          flashcount = 0
          pygame.time.set_timer(USEREVENT+1,0)

      if event.type == KEYDOWN:
        # This returns a list of True/False where the index is the
        # code of the key pressed. Fortunately pygame.locals provides
        # symbolics for these codes
        key = pygame.key.get_pressed()
        if key[K_q]:
          pygame.quit()
          exit()
        if key[K_r] and GameOver:
          GameOver = False
          shield.SetValue(250)
          score.SetValue(0)
        if key[K_LEFT]:
          shipspeed_x = -300
        if key[K_RIGHT]:
          shipspeed_x = 300
        if key[K_UP]:
          shipspeed_y = -300
        if key[K_DOWN]:
          shipspeed_y = 300
        if key[K_SPACE] and not GameOver:
          if firelist:
            # Only fire if last shot has travelled
            # a minimum distance
            if firelist[-1].DistanceTravelled() >=  150:
              firelist.append(SpaceShip.Fire())
          else:
            # or if there is no shot
            firelist.append(SpaceShip.Fire())


    # Move the SpaceShip by the specified amount

    SpaceShip.Move(shipspeed_x, shipspeed_y, time)

    # Show all the objects, background first (or it will erase everything else!)
    StarField.Scroll(backspeed, time)
    StarField.Show(screen)
    SpaceShip.Show(screen,imageindex)

    # Show and move the aliens

    for AlienShip in AlienShips:
      AlienShip.Show(screen)
      AlienShip.Move(time)
      if randint(0,10)==9:
        if alienfirelist:
          if alienfirelist[-1].DistanceTravelled()>=100:
            alienfirelist.append(AlienShip.Fire())
        else:
          alienfirelist.append(AlienShip.Fire())

    for theshot in firelist:
      theshot.Move(time)
      theshot.Show(screen)
      if theshot.GoneAbove(0):
          firelist.remove(theshot)
      else:
        for AlienShip in AlienShips:
          if AlienShip.rect.collidepoint(theshot.GetXY()):
            score.Change(10)
            explosion.play()
            if score.GetValue() % 100 == 0:
              shield.Increase(25)
            if theshot in firelist:
              firelist.remove(theshot)
            AlienShips.remove(AlienShip)

    for theshot in alienfirelist:
      theshot.Move(time)
      theshot.Show(screen)
      if theshot.GoneBelow(laserdownlimit):
        alienfirelist.remove(theshot)
      else:
        if SpaceShip.rect.collidepoint(theshot.GetXY()) and not GameOver:
          destroyed.play()
          pygame.time.set_timer(USEREVENT+1,25)
          shield.Decrease(25)
          if theshot in alienfirelist:
            alienfirelist.remove(theshot)

    score.Show(screen)
    shield.Show(screen)
    if shield.GetValue() == 0:
      GameOverShow(screen)
      GameOver = True

    pygame.display.update()

# End main loop

# Start program
if __name__ == "__main__":
    main()
