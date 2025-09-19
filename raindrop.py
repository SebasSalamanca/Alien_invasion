import pygame
import random
from pygame.sprite import Sprite


class Monster(Sprite):
    """A class to represent a moster it will drop from top of the screen."""
    
    
    def __init__(self, ai_game):
        """Initialize a monster an it starting position"""
        super().__init__()

        self.screen = ai_game.screen 
        self.settings = ai_game.settings 

        #Load the alien and set its attribute
        self.image = pygame.image.load('images/monster_42.bmp')
        self.rect = self.image.get_rect()

        #Same color of the background
        back_gr = self.image.get_at((0, 0))
        self.image.set_colorkey(back_gr)

        
        #Store the alien's horizontal position 
        self.y = float(self.rect.y)

        
        
        #List of position of the vector:
        self.inventory_position = list(range(0,self.settings.screen_width, 50))

        

    def set_random_position(self, monster_index):

        #if monster_index == Monster.monster_id:
        if self.settings.number_monsters == 6:
            start_position = monster_index * 4
            end_position = start_position + 4
        elif self.settings.number_monsters == 8:
            start_position = monster_index * 3
            end_position = start_position + 3
        elif self.settings.number_monsters > 8 and self.settings.number_monsters <= 12:
            start_position = monster_index * 2
            end_position = start_position + 2
            
            

        number_2 = random.sample(self.inventory_position[start_position:end_position], 1)
        self.rect.x = number_2[0]
  
            
        
        
    def update(self):
        self.y += self.settings.monster_speed
        self.rect.y = self.y
