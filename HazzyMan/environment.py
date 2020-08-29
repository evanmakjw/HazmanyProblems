import random
import pygame
import os
from settings import dir_path
class Mask:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load(os.path.join(dir_path,"face-mask.png"))
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def drawMask(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Tree:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
        self.icon = pygame.image.load(os.path.join(dir_path,"tree.png"))
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def drawTree(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Sanitizer:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load(os.path.join(dir_path,"hand-sanitizer.png"))
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def drawSanitizer(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Playground:

    def __init__(self):
        self.x = 10
        self.y = 10
        self.iconCont = pygame.image.load(os.path.join(dir_path,"playground_c.png"))
        self.iconNonCont = pygame.image.load(os.path.join(dir_path,"playground_nc.png"))
        self.infected = False
        self.rect = pygame.Rect(self.x, self.y, 100, 90)

    def drawPlayground(self, screen):
        if self.infected is False:
            screen.blit(self.iconNonCont, (self.x, self.y))
        else:
            screen.blit(self.iconCont, (self.x,self.y))


class School:

    def __init__(self):
        self.x = 640
        self.y = 460
        self.iconCont = pygame.image.load(os.path.join(dir_path,"school_C.png"))
        self.iconNonCont = pygame.image.load(os.path.join(dir_path,"school_NC.png"))
        self.infected = False
        self.rect = pygame.Rect(self.x, self.y, 130, 120)

    def drawSchool(self, screen):
        if self.infected == False:
            screen.blit(self.iconNonCont, (self.x, self.y))
        else:
            screen.blit(self.iconCont, (self.x,self.y))
