# Background music
import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load("spaceinvaders.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
        clock.tick()
