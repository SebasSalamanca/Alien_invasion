

class Settings:
    """A class to store all settings for alien invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (125,125,125)

        #Ship settings
        self.ship_speed = 5

        #Bullet Settings
        self.bullet_speed = 7.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 165, 0)
        self.bullets_allowed = 7

        #Alien settings
        self.alien_speed = 2.5
        self.fleet_drop_speed = 10
        #Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        