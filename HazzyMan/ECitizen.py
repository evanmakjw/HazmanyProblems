import random
import pygame
import os

class ECitizen():
    def __init__(self, ID, status):
        self.personID  = ID
        self.__attribute = random.choice(["Compliant","Stubborn"])
        self.__masked = False
        self.__sanitized = False
        self.__hiddenStatus = status
        self.__tested = False
        self.icon = pygame.image.load("walk.png")
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
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

    # def change_direction(self):
    #     while True:
    #         direction  = random.choice(range(0,3))
    #         if direction ~= current_direction:





class Infected(ECitizen):
    def infect(self,target):
        pass

    def infect_object(self,obj):
        pass

class NonInfected(ECitizen):
    def infectionChance(self):
        pass

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




