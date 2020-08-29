import pygame
import random
<<<<<<< Updated upstream
import time
=======
import os
>>>>>>> Stashed changes
from environment import (
    Mask,
    Tree,
    Sanitizer,
    Playground,
    School
)
from hazman import Hazman
from citizen import Citizen
from trees import (
    treexcor,
    treeycor
)
<<<<<<< Updated upstream
=======
from settings import dir_path
>>>>>>> Stashed changes

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load(os.path.join(dir_path,"ground.png"))

# Title & Icon
pygame.display.set_caption("Hazzy Man")
icon = pygame.image.load(os.path.join(dir_path,"hazmat.png"))
pygame.display.set_icon(icon)

# Create player and citizen
player = Hazman()
citizen = Citizen()

# Other locations
playground = Playground()
school = School()

# Create other interactable objects
masks = []

for i in range(10):
    temp = Mask()
    masks.append(temp)

trees = []
treeColideArr = []

for i in range(len(treexcor)):
    temp = Tree(treexcor[i], treeycor[i])
    trees.append(temp)
    treeColideArr.append(temp.rect)

sanitizers = []

for i in range(10):
    temp = Sanitizer()
    sanitizers.append(temp)

people = []

for i in range(10):
    temp = Citizen()
    people.append(temp)

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
<<<<<<< Updated upstream
    player.x += player.xChange
    player.y += player.yChange
    player.rect.x += player.xChange
    player.rect.y += player.yChange

    # Establish boundaries for the player
=======
    for event in pygame.event.get():
        if player.rect.collidelist(treeColideArr) is -1:
            player.x += player.xChange
            player.y += player.yChange
            player.rect.x += player.xChange
            player.rect.y += player.yChange
        else:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.yChange = 0


    # Establish boundaries
>>>>>>> Stashed changes
    if player.x <= 0:
        player.x = 0
        player.rect.x = 0

    elif player.x >= 768:
        player.x = 768
        player.rect.x = 768

    if player.y <= 0:
        player.y = 0
        player.rect.y = 0

    elif player.y >= 568:
        player.y = 568
        player.rect.y = 568

    # Do the same for citizen
    i = 0
    while i < 10:
        people[i].x += people[i].xChange
        if people[i].x <= 0:
            people[i].xChange = 0.4
            people[i].y += people[i].yChange

        elif people[i].x >= 768:
            people[i].xChange = -0.4
            people[i].y += people[i].yChange

        people[i].draw_citizen(screen)

        i += 1

    # Keep drawing the player
    player.draw_player(screen)

    # Uncomment if
    if player.rect.colliderect(playground.rect):
    # if player.x in range(playground.x - 10, playground.x + 10):
        playground.infected = True

    if player.rect.colliderect(school.rect):
    # if player.x in range(playground.x - 10, playground.x + 10):
        school.infected = True

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

    # Display other locations
    playground.drawPlayground(screen)
    school.drawSchool(screen)


    # Always update your screen
    pygame.display.update()
