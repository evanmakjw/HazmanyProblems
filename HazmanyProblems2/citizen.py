import random
import pygame
import os

class Citizen():
    def __init__(self, ID, status):
        self.personID  = ID
        self.attribute = random.choice(["Compliant","Stubborn"])
        self.masked = False
        self.sanitized = False
        self.hiddenStatus = status
        self.tested = False
        self.icon = pygame.image.load("walk.png")
        self.xChange = 0.4
        self.yChange = 10

    def remove_mask(self): 
        self.masked = False

    def take_supplies(self):
        self.sanitized = True
        self.masked = True

    def draw_citizen(self, screen):
        screen.blit(self.icon, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def infect(self,target):
        target.get_infection()

    def infect_object(self,obj):
        pass

    def cure_infection(self):
        self.infected = False
        screen.blit(self.iconCont, (self.x,self.y))

    def get_infection(self):
        self.infected = True
        screen.blit(self.iconCont, (self.x, self.y))



        


numInfected = 1

infectedIDArr = []
notInfectedIDArr = []
citizenArr = []

# while infected ppl is less than num specified
while len(infectedIDArr) < numInfected:

    # choose a random index
    random_num = random.choice(range(0,10))
    print(random_num)

    # if array is empty
    if not infectedIDArr:
        infectedIDArr.append(random_num)

    # if the index has already been chosen
    elif random_num in infectedIDArr:
        continue

    # otherwise 
    else:
        infectedIDArr.append(random_num)

# for index in infectedIDArr:
for i in range(0,10):
    if i in infectedIDArr:
        citizenArr.append(ECitizen(i,"Infected"))
    else:
        notInfectedIDArr.append(i)
        citizenArr.append(ECitizen(i,"notInfected"))

print(infectedIDArr)
print(notInfectedIDArr)
print()




