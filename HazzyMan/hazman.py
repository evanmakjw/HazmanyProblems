import pygame
import os

from settings import dir_path

class Hazman():

    def __init__(self):

        # Position on the screen
        self.icon = pygame.image.load(os.path.join(dir_path,"player.png"))
        self.x = 400
        self.y = 480
        self.xChange = 0
        self.yChange = 0
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

        # Other attributes
        self.maskCount = 0
        self.sanitizerCount = 0

    def draw_player(self, screen):
        screen.blit(self.icon, (self.x, self.y))
        # Comment this line to show hazman image
        pygame.draw.rect(screen, (255, 200, 0), self.rect)

    def give_mask(self):
        self.maskCount -= 1; 
        print("{0} masks left".format(self.maskCount) )

    def give_sanitizer(self):
        self.sanitizerCount -= 1 
        
    def give_supplies(self, target):
        if self.maskCount > 0:
            self.give_mask(target)
            masked = True

        if self.sanitizerCount > 0:
            self.give_sanitizer(target)
            sanitized = True; 

        target.take_supplies(masked, sanitized)


    def pick_up_masks(self):
        self.maskCount += 5 

    def pick_up_sanitizer(self):
        self.sanitizerCount+= 5

    def clean_object(self, obj):
        obj.decontaminate()

    def test_citizen(self):
        pass
    # def send_to_isolate(self):

#hazzy = Hazman()
#hazzy.give_mask()
#print("hello")
    # body of the constructor