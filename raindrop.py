import pygame
from random import randint
from pygame.sprite import Sprite


class Monster(Sprite):
    """A class to represent a moster it will drop from top of the screen."""

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
        self.x = float(self.rect.x)

    def set_random_position(self):
        
        self.rect.x = randint(self.rect.width, (self.settings.screen_width-self.rect.width))



    def update(self):
        self.x = self.settings.monster_speed
        self.rect.x = self.x


    def blitme(self):
        #Draw the monster at its current location
        self.screen.blit(self.image, self.rect)