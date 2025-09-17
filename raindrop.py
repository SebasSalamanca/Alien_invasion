import pygame
from random import randint
from pygame.sprite import Sprite


class Monster(Sprite):
    """A class to represent a moster it will drop from top of the screen."""
    vector_location = []
    
    def __init__(self, ai_game):
        """Initialize a monster an it starting position"""
        super().__init__()

        self.screen = ai_game.screen 
        self.settings = ai_game.settings 

        #Load the alien and set its attribute
        self.image = pygame.image.load('images/monster.bmp')
        self.rect = self.image.get_rect()

        #Same color of the background
        back_gr = self.image.get_at((0, 0))
        self.image.set_colorkey(back_gr)

        
        #Store the alien's horizontal position 
        self.y = float(self.rect.y)
        


    def set_random_position(self):
        
        if len(Monster.vector_location) < 1:
            number_2 = randint(self.rect.width, (self.settings.screen_width-self.rect.width))
            Monster.vector_location.append(number_2)
            self.rect.x = number_2
        else:
            tam = len(Monster.vector_location)
            while (len(Monster.vector_location) == tam):
                number_3 = randint(self.rect.width, (self.settings.screen_width-self.rect.width))
                vector_3 = []
                for i in range((len(Monster.vector_location))):
                    if(number_3 < Monster.vector_location[i] - 80 or number_3 > Monster.vector_location[i] + 80):
                        vector_3.append(1)
                    else:
                        vector_3.append(0)
                if 0 not in vector_3:
                    self.rect.x = number_3
                    Monster.vector_location.append(number_3)


    def update(self):
        self.y += self.settings.monster_speed
        self.rect.y = self.y
