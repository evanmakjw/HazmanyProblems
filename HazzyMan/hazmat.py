import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("ground.png")

# Title & Icon
pygame.display.set_caption("Hazzy Man")
icon = pygame.image.load("hazmat.png")
pygame.display.set_icon(icon)

# Player
playerIcon = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Citizen
citizenIcon = pygame.image.load("walk.png")
citizenX = random.randint(0, 800)
citizenY = random.randint(50, 150)
citizenX_change = 0.4
citizenY_change = 10


class Mask:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load("face-mask.png")
    
    def drawMask(self):
        screen.blit(self.icon, (self.x, self.y))

masks = []

for i in range(10):
    temp = Mask()
    masks.append(temp)

class Tree:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load("tree.png")

    def drawTree(self):
        screen.blit(self.icon, (self.x, self.y))

trees = []

for i in range(70):
    temp = Tree()
    trees.append(temp)

class Sanitizer:

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.icon = pygame.image.load("hand-sanitizer.png")

    def drawSanitizer(self):
        screen.blit(self.icon, (self.x, self.y))

sanitizers = []

for i in range(10):
    temp = Sanitizer()
    sanitizers.append(temp)

        


def player(x, y):

    # Draw image of player
    screen.blit(playerIcon, (x, y))

def citizen(x, y):

    # Draw image of player
    screen.blit(citizenIcon, (x, y))

#def mask(x, y):

#    screen.blit(maskIcon, (x, y))

# Main loop
running = True
while running:

    # RBG Values
    screen.fill((192, 192, 192))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # Condition to quit the game
        if event.type == pygame.QUIT:
            running = False

        # Check for user input
        if event.type == pygame.KEYDOWN:

            # Move left
            if event.key == pygame.K_LEFT:
                playerX_change = -1

            # Move right
            elif event.key == pygame.K_RIGHT:
                playerX_change = 1

            # Move left
            elif event.key == pygame.K_UP:
                playerY_change = -1

            # Move left
            elif event.key == pygame.K_DOWN:
                playerY_change = 1
        
        # Stop moving the player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    
    # Update player positon
    playerX += playerX_change
    playerY += playerY_change

    # Establish boundaries
    if playerX <= 0:
        playerX = 0

    elif playerX >= 768:
        playerX = 768

    # Do the same for the citizen
    citizenX += citizenX_change

    if citizenX <= 0:
        citizenX_change = 0.4
        citizenY += citizenY_change

    elif citizenX >= 768:
        citizenX_change = -0.4
        citizenY += citizenY_change

    player(playerX, playerY)
    citizen(citizenX, citizenY)

    i = 0
    while i < len(masks):
        masks[i].drawMask()
        i += 1

    i = 0
    while i < len(trees):
        trees[i].drawTree()
        i += 1

    i = 0
    while i < len(sanitizers):
        sanitizers[i].drawSanitizer()
        i += 1


    # Always update your screen
    pygame.display.update()