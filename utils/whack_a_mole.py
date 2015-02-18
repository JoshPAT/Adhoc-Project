import sys
import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *
import socket
#import Sensing
import re
import sys

port = 7000
hits = 0
class Mole(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole.gif")
        self.rect = self.image.get_rect()

    #move to a new random position
    def flee(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX, randY)

#main
pygame.init()

mole = Mole()
mole2 = Mole()
sprites = Group(mole)
sprites2 = Group(mole2)


s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(('', port))
# header for the window
display.set_caption("Whack-a-mole")
screen = display.set_mode((640, 480))

screen.fill((255, 255, 255))
f = font.Font(None, 25)
t = f.render("Hits = " + str(hits), False, (0,0,0))
screen.blit(t, (320, 0)) # draw text to screen
sprites.update()
sprites.draw(screen)

sprites2.update()
sprites2.draw(screen)
display.update()


while True:
    data = s.recvfrom(1024)
    # mole moves positions when clicked on
    if (len(data) > 0):	
	mole.flee()
	mole2.flee()
	hits += 1
    screen.fill((255, 255, 255))
    t = f.render("Hits = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0)) # draw text to screen
    sprites.update()
    sprites.draw(screen)

    
    sprites2.update()
    sprites2.draw(screen)
    display.update()
