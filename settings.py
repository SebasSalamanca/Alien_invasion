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
        self.ship_speed = 8
        self.bullet_speed = 7.0
        self.alien_speed = 2.5
        self.monster_speed = 6
        #Number of monsters 
        self.number_monsters = 6

        #Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Level game
        self.game_level = 1

        #Scoring settings
        self.alien_points = 50
        

    def increase_speed(self):
        """Increase speed settings"""
        
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        if self.game_level == 1:
            self.number_monsters += 2**self.game_level
            self.monster_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
            self.ship_speed *= self.speedup_scale
            self.game_level += 1
        else:
            self.monster_speed = 6.5
            self.number_monsters = 12
        

            