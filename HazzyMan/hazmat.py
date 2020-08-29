import pygame
import random
import os

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
from settings import dir_path

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
# citizen = Citizen()

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

numInfected = 1
numCitizens = 30

# Get list of infected and non infected citizen objects
while len(people) < numCitizens:
    if len(people) < numInfected:
        people.append(Citizen(True))
    else:
        people.append(Citizen(False))

print(people[0].infected)
print(people[1].infected)

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


    # Update the player's collision field
    player.rect.x += player.xChange
    player.rect.y += player.yChange

    # Check if no collision occurs
    if player.rect.collidelist(treeColideArr) == -1:
        player.x += player.xChange
        player.y += player.yChange

    # If a collision occurs, move the player back
    else:
        player.rect.x -= player.xChange
        player.rect.y -= player.yChange

    # Establish boundaries
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

    path = ["up", "down", "right", "left"]

    # For each citizen
    i = 0
    while i < len(people):

        # Change direction randomly after 100 pixels
        if people[i].distanceTravelled > 100:
            chance = random.choice(path)
            people[i].direction = chance
            people[i].distanceTravelled = 0

        # Change direction status appropriately
        if people[i].direction == "right":
            people[i].xChange = 1
            people[i].yChange = 0
        elif people[i].direction == "left":
            people[i].xChange = -1
            people[i].yChange = 0
        elif people[i].direction == "up":
            people[i].yChange = -1
            people[i].xChange = 0
        elif people[i].direction == "down":
            people[i].yChange = 1
            people[i].xChange = 0

        # Update citizens' collision field
        people[i].rect.x += people[i].xChange
        people[i].rect.y += people[i].yChange

        # Account for normal movement of citizens
        if people[i].rect.collidelist(treeColideArr) == -1:
            people[i].distanceTravelled += abs(people[i].xChange)
            people[i].distanceTravelled += abs(people[i].yChange)
            people[i].x += people[i].xChange
            people[i].y += people[i].yChange

        # Citizens collide with tree
        else:
            people[i].rect.x -= people[i].xChange
            people[i].rect.y -= people[i].yChange
            bad_direction = people[i].direction
            while people[i].direction == bad_direction:
                # print(bad_direction)
                # print([direc for direc in path if direc != bad_direction])
                chance = random.choice([direc for direc in path if direc != bad_direction])
                people[i].direction = chance

        # print([ppl.rect for ppl in people if ppl is not people[i]])
        if people[i].rect.collidelist([ppl.rect for ppl in people if ppl is not people[i]]) != -1:
            contactIndex = people[i].rect.collidelist([ppl.rect for ppl in people if ppl is not people[i]])
            if people[i].infected == True:
                 if people[i].masked == False and people[contactIndex].masked == False:
                    people[contactIndex].infected = True

            elif people[i].infected == False: 
                if people[i].masked == False and people[contactIndex].infected == True and people[contactIndex].masked == False:
                    people[i].infected = True

        people[i].draw_citizen(screen)

        #If people collide with the playground or school
        if people[i].rect.colliderect(playground.rect) and people[i].infected is True:
            playground.infected = True
        if people[i].rect.colliderect(school.rect) and people[i].infected is True:
            school.infected = True

        i += 1

    # Keep drawing the player
    player.draw_player(screen)

    # If player collides with locations
    if player.rect.colliderect(playground.rect):
        playground.infected = False

    if player.rect.colliderect(school.rect):
        school.infected = False


    i = 0
    while i < len(masks):
        
        #If player goes over the mask, collect it
        if masks[i].rect.colliderect(player.rect):
            masks[i].collected = True
            player.pick_up_masks()
        
        #Only show mask if it has been collected
        if masks[i].collected == False:
            masks[i].drawMask(screen)

        i += 1

    i = 0
    while i < len(trees):
        trees[i].drawTree(screen)
        i += 1

    i = 0
    while i < len(sanitizers):
        #If player goes over the saniriser, collect it
        if sanitizers[i].rect.colliderect(player.rect):
            sanitizers[i].collected = True
            player.pick_up_sanitizer()
        
        #Only show santiser if it has been collected
        if sanitizers[i].collected == False:
            sanitizers[i].drawSanitizer(screen)

        i += 1

    i = 0
    while i < len(people):
        if people[i].rect.colliderect(player.rect) and people[i].masked == False:
            if player.maskCount > 0:
                player.maskCount -= 1
                people[i].masked = True

            if player.sanitizerCount > 0 and people[i].infected == True:
                player.sanitizerCount -= 1
                people[i].infected = False

            people[i].draw_citizen(screen)

        i += 1

    # Display other locations
    playground.drawPlayground(screen)
    school.drawSchool(screen)


    # Always update your screen
    pygame.display.update()
