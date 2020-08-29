import random
import pygame
import os

current_path = os.path.dirname(__file__) + "/"
class Citizen:

    def __init__(self):

        self.icon = pygame.image.load(current_path+"walk.png")
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.xChange = 0.4
        self.yChange = 10

    def draw_citizen(self, screen):

        screen.blit(self.icon, (self.x, self.y))
