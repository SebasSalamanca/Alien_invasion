import pygame

class Settings:
    """A class to store all settings for alien invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 10, 30)
        
        

        #Ship settings
        self.ship_speed = 8
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed = 7.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 165, 0)
        self.bullets_allowed = 7

        #Alien settings
        self.alien_speed = 2.5
        self.fleet_drop_speed = 7
        #Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Number of monsters 
        self.monster_speed = 6
        self.number_monsters = 7