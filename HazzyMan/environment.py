import random
import pygame
import os

class Mask:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load("face-mask.png")

    def drawMask(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Tree:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
        self.icon = pygame.image.load("tree.png")

    def drawTree(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Sanitizer:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load("hand-sanitizer.png")

    def drawSanitizer(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Playground:

    def __init__(self):
        self.x = 10
        self.y = 10
        self.iconCont = pygame.image.load("playground_c.png")
        self.iconNonCont = pygame.image.load("playground_nc.png")
        self.infected = False

    def drawPlayground(self, screen):
        if self.infected is False:
            screen.blit(self.iconNonCont, (self.x, self.y))
        else:
            screen.blit(self.iconCont, (self.x,self.y))


class School:

    def __init__(self):
        self.x = 50
        self.y = 40
        self.iconCont = pygame.image.load("school_C.png")
        self.iconNonCont = pygame.image.load("school_NC.png")
        self.infected = False

    def drawSchool(self, screen):
        if self.infected == False:
            screen.blit(self.iconNonCont, (self.x, self.y))
        else:
            screen.blit(self.iconCont, (self.x,self.y))
