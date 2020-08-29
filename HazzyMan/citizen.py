import random
import pygame
import os
from settings import dir_path
class Citizen:

    def __init__(self):

        self.icon = pygame.image.load(os.path.join(dir_path,"walk.png"))
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.xChange = 0.4
        self.yChange = 10

    def draw_citizen(self, screen):

        screen.blit(self.icon, (self.x, self.y))
