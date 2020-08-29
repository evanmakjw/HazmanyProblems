import random
import pygame
import os

current_path = os.path.dirname(__file__) + "/"

class Mask:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load(current_path+"face-mask.png")
    
    def drawMask(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Tree:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load(current_path+"tree.png")

    def drawTree(self, screen):
        screen.blit(self.icon, (self.x, self.y))

class Sanitizer:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load(current_path+"hand-sanitizer.png")

    def drawSanitizer(self, screen):
        screen.blit(self.icon, (self.x, self.y))