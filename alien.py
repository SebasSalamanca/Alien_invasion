import pygame
from pygame.sprite import Sprite
import sys 
import os

def get_reurce_path(relative_path):
    """Get aboslute path to resource, works for dev and for PyInstaller"""
    try:
        #Pyinstaller creates a temp folder and stores path in MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)



class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()

        self.screen = ai_game.screen #Review this line of dependency injection later
        self.settings = ai_game.settings

        #Load the alien image and set its attribute
        self.image = pygame.image.load(get_reurce_path('images/alien_paul_42.bmp'))
        self.rect = self.image.get_rect()

        #Same color of the background.
        #back_gr = self.image.get_at((0,0))
        #self.image.set_colorkey(back_gr)    

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's horizontal position 
        self.x = float(self.rect.x)


    def update(self):
        #Move the alien to the right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


    def check_edges(self):
        """Return true if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right > screen_rect.right) or (self.rect.left <= 0)
