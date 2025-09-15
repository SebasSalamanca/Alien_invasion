

class Settings:
    """A class to store all settings for alien invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,0)

        #Ship settings
        self.ship_speed = 3.5

        #Bullet Settings
        self.bullet_speed = 5.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 165, 0)
        self.bullets_allowed = 7
        