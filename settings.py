import pygame
from random import randint

class Settings:
    """A class to store all settings for alien invasion"""
    
    def __init__(self):
        """Initialize game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 10, 30)
        

        #Ship settings
        
        self.ship_limit = 3

        #Bullet Settings
        
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 165, 0)
        self.bullets_allowed = 7

        #Alien settings
        
        self.fleet_drop_speed = 7

        #How quickly the game speeds up 
        self.speedup_scale = 1.2

        #How quikly the alien point values increase
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        """Initialize settings that change throughout the game. """
        self.ship_speed = 4
        self.bullet_speed = 6
        self.alien_speed = 2.5
        self.monster_speed = 4
        #Number of monsters 
        self.number_monsters = 6

        #Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Scoring settings
        self.alien_points = 100
        

    def increase_speed(self, level):
        """Increase speed settings"""
        
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(level)
        if level == 2:

            self.alien_speed *= self.speedup_scale
            self.ship_speed *= self.speedup_scale
            self.monster_speed *= self.speedup_scale

        elif level == 3:
            self.number_monsters += 2
            self.monster_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
            self.ship_speed *= self.speedup_scale

        elif level == 4:
            self.monster_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
            self.ship_speed *= self.speedup_scale


        elif level == 5:
            
            self.number_monsters += 4
            self.monster_speed = 6.5 

        elif level >= 6:

            self.ship_speed = 11
            self.monster_speed = 6.5 
            self.bullet_speed = 10


        
        
        
        
        
        

            