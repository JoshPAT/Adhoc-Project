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
import time

port = 7000
hits = 0

flag = 1
class Mole(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole1.png")
	
        self.rect = self.image.get_rect()
	self.rect.center = (100, 150)

    #move to a new random position
    def knock(self):
        self.image = image.load("mole1k.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 150)
    def normal(self):
        self.image = image.load("mole1.png")
        self.rect = self.image.get_rect()
	self.rect.center = (100, 150)
class Mole2(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole2.png")
	
        self.rect = self.image.get_rect()
	self.rect.center = (400, 150)

    #move to a new random position
    def knock(self):
        self.image = image.load("mole2k.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 150)
    def normal(self):
        self.image = image.load("mole2.png")
        self.rect = self.image.get_rect()
	self.rect.center = (400, 150)

class Mole3(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole3.png")
	
        self.rect = self.image.get_rect()
	self.rect.center = (100, 400)

    #move to a new random position
    def knock(self):
        self.image = image.load("mole3k.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)
    def normal(self):
        self.image = image.load("mole3.png")
        self.rect = self.image.get_rect()
	self.rect.center = (100, 400)

class Mole4(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole4.png")
	
        self.rect = self.image.get_rect()
	self.rect.center = (400, 400)

    #move to a new random position
    def knock(self):
        self.image = image.load("mole4k.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
    def normal(self):
        self.image = image.load("mole4.png")
        self.rect = self.image.get_rect()
	self.rect.center = (400, 400)

class Welcome(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("play.png")	
        self.rect = self.image.get_rect()
	self.rect.center = (320, 240)
   
    def left(self):
        self.image = image.load("left1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
    def right(self):
        self.image = image.load("right1.png")

        self.rect = self.image.get_rect()
	self.rect.center = (320, 240)


#main
pygame.init()

welconme = Welcome()
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(('', port))
# header for the window
display.set_caption("Whack-a-mole")
screen = display.set_mode((640, 480))
sprites5 = Group(welconme)

sprites5.update()
sprites5.draw(screen)
display.update()

ev = event.wait()
mixer.Sound("play.wav").play()
while flag == 1:
	ev = event.wait()
	if ev.type == MOUSEBUTTONDOWN:
		flag = 0
		mole = Mole()
		mole2 = Mole2()
		mole3 = Mole3()
		mole4 = Mole4()
		sprites = Group(mole)
		sprites2 = Group(mole2)
		sprites3 = Group(mole3)
		sprites4 = Group(mole4)


		screen.fill((55, 192, 67))


		sprites.update()
		sprites.draw(screen)

		sprites2.update()
		sprites2.draw(screen)

		sprites3.update()
		sprites3.draw(screen)

		sprites4.update()
		sprites4.draw(screen)

		f = font.Font(None, 45)
		t = f.render("Hits = " + str(hits), False, (0,0,0))
		screen.blit(t, (180, 0)) # draw text to screen
		display.update()

def scrprt():
    screen.fill((55, 192, 67))
    t = f.render("Hits = " + str(hits), False, (0,0,0))
    screen.blit(t, (180, 0)) # draw text to screen
    sprites.update()
    sprites.draw(screen)
	    
    sprites2.update()
    sprites2.draw(screen)

    sprites3.update()
    sprites3.draw(screen)

    sprites4.update()
    sprites4.draw(screen)
    display.update()
    time.sleep(0.5)

while True:
    p = 30.00
    a = time.time()
    n = 0

    while True:
        n = time.time()
        if n  > a + p:
            if flag == 0:
		flag +=1
	    	mixer.Sound("gameover.wav").play()
	    screen.fill((255, 255, 255))
            f = font.Font(None, 80)
	    c = font.Font(None, 5)
            t = f.render("GameOver", False, (0,0,0))
	    c = f.render("Score: " + str(hits), False, (0,0,0))
            screen.blit(t, (180, 0)) # draw text to screen
            screen.blit(c, (180, 50))
	    welconme.left()
	    sprites5.update()
	    sprites5.draw(screen)
	    display.update()
            time.sleep(0.5) 
	    welconme.right()
	    sprites5.update()
            sprites5.draw(screen)
	    display.update()
            time.sleep(0.5)
           
	else:
            mole.normal()  
            mole2.normal()   
            mole3.normal() 
            mole4.normal()     
            screen.fill((55, 192, 67))
            t = f.render("Hits = " + str(hits), False, (0,0,0))
            screen.blit(t, (180, 0)) # draw text to screen
            sprites.update()
            sprites.draw(screen)
            sprites2.update()
            sprites2.draw(screen)

            sprites3.update()
            sprites3.draw(screen)

            sprites4.update()
            sprites4.draw(screen)
            display.update()
            	
            data, addr = s.recvfrom(1024)

            # mole moves positions when clicked on
            if (len(data) > 0):	
        	mixer.Sound("hit.wav").play()
        	hits += 1
                addrstr = str(addr)
        	if int(addrstr[8]) == 2:
        	    mole.knock()    	
        	    mole2.normal()
        	    mole3.normal()
        	    mole4.normal()
        	    scrprt()
        	elif int(addrstr[8]) == 3:
        	    mole.normal()    	
        	    mole2.knock()
        	    mole3.normal()
        	    mole4.normal()
        	    scrprt()
        	elif int(addrstr[8]) == 4:
        	    mole.normal()    	
        	    mole2.normal()
        	    mole3.knock()
        	    mole4.normal()
                    scrprt()
        	elif int(addrstr[8]) == 8:   
        	    mole.normal()    	
        	    mole2.normal()
        	    mole3.normal()
        	    mole4.knock()
        	    scrprt()
        

