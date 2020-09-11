import pygame
from hazman import Hazman
from environment import (
    Mask,
    Tree,
    Sanitizer,
    Playground,
    School
)

class Game:

    def __init__(self, background, icon, numInfected, numCitizen):

        # Initialise the pygame module 
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode((1366, 768))

        # Background
        self.background = pygame.image.load(os.path.join(dir_path,background))

        # Title & Icon
        pygame.display.set_caption("Hazzy Man")
        icon = pygame.image.load(os.path.join(dir_path,"hazmat.png"))
        pygame.display.set_icon(icon)

        # Player
        self.player = Hazman()

        # Buildings
        playground = Playground()
        school = School()

        self.numInfected = numInfected
        self.numCitizen = numCitizen