import sys
import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *
import socket
import Sensing
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
        self.image = image.load("1.png")
	
        self.rect = self.image.get_rect()
	self.rect.center = (500, 360)

    #move to a new random position
    def knock1(self):
        self.image = image.load("1knock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 360)
    def knock2(self):
        self.image = image.load("2knock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 360)
    def knock3(self):
        self.image = image.load("3knock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 360)
    def knock4(self):
        self.image = image.load("4knock.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 360)


    def normal(self):
        self.image = image.load("1.png")
        self.rect = self.image.get_rect()
	self.rect.center = (500, 360)
    
    def start(self):
        self.image = image.load("1.png")
        self.rect = self.image.get_rect()
	self.rect.center = (800, 360)


class Welcome(Sprite):
    # constructor
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("play.png")	
        self.rect = self.image.get_rect()
	self.rect.center = (500, 360)
   
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
screen = display.set_mode((1000, 720))


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
	
	    sprites = Group(mole)
	    screen.fill((55, 192, 67))


	    sprites.update()
	    sprites.draw(screen)

	    f = font.Font(None, 45)
	    t = f.render("Hits = " + str(hits), False, (0,0,0))
	    screen.blit(t, (450, 65)) # draw text to screen
	    display.update()

def scrprt():
    
     # draw text to screen
    sprites.update()
    t = f.render("Hits = " + str(hits), False, (0,0,0))
    screen.blit(t, (450, 65))    
    sprites.draw(screen)
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
	    c = font.Font(None, 30)
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
           
             # draw text to screen
            sprites.update()
            sprites.draw(screen)
	    t = f.render("Hits = " + str(hits), False, (0,0,0))
            screen.blit(t, (450, 65))
            display.update()
            	
            data, addr = s.recvfrom(1024)

            # mole moves positions when clicked on
            if (len(data) > 0):	
        	mixer.Sound("hit.wav").play()
        	hits += 1
                addrstr = str(addr)
        	if int(addrstr[8]) == 2:
        	    mole.knock1()    	
        	    scrprt()
        	elif int(addrstr[8]) == 3:
        	    mole.knock2()
        	    scrprt()
        	elif int(addrstr[8]) == 4:
        	    mole.knock3()
                    scrprt()
        	elif int(addrstr[8]) == 8:   
        	    mole.knock4()    	
        	    scrprt()
        

