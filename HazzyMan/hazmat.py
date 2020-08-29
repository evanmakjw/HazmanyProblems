import pygame
import random
from environment import (
    Mask,
    Tree,
    Sanitizer
)
from hazman import Hazman
from citizen import Citizen

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

# Create player and citizen
player = Hazman()
citizen = Citizen()

# Create other interactable objects
masks = []

for i in range(10):
    temp = Mask()
    masks.append(temp)

trees = []

for i in range(70):
    temp = Tree()
    trees.append(temp)

sanitizers = []

for i in range(10):
    temp = Sanitizer()
    sanitizers.append(temp)

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
                player.xChange = -1

            # Move right
            elif event.key == pygame.K_RIGHT:
                player.xChange = 1

            # Move up
            elif event.key == pygame.K_UP:
                player.yChange = -1

            # Move down
            elif event.key == pygame.K_DOWN:
                player.yChange = 1
        
        # Stop moving the player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.yChange = 0
    
    # Update player positon
    player.x += player.xChange
    player.y += player.yChange

    # Establish boundaries
    if player.x <= 0:
        player.x = 0

    elif player.x >= 768:
        player.x = 768

    # Do the same for the citizen
    citizen.x += citizen.xChange

    if citizen.x <= 0:
        citizen.xChange = 0.4
        citizen.y += citizen.yChange

    elif citizen.x >= 768:
        citizen.xChange = -0.4
        citizen.y += citizen.yChange

    # Keep drawing the characters
    player.draw_player(screen)
    citizen.draw_citizen(screen)

    i = 0
    while i < len(masks):
        masks[i].drawMask(screen)
        i += 1

    i = 0
    while i < len(trees):
        trees[i].drawTree(screen)
        i += 1

    i = 0
    while i < len(sanitizers):
        sanitizers[i].drawSanitizer(screen)
        i += 1


    # Always update your screen
    pygame.display.update()