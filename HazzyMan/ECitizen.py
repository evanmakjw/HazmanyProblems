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

while len(infectedIDArr) < numInfected:
    random_num = random.choice(range(0,10))
    print(random_num)
    if not infectedIDArr:
        infectedIDArr.append(random_num)
    elif random_num in infectedIDArr:
        continue
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




