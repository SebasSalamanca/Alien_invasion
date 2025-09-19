import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        #Initialize scorekeeping attributes 

        self.ai_game = ai_game ##Assinging the game instance to an attribute, because we'll need it to create some ships.

        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring information 
        self.text_color = (180, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #Turn the score into a redered image

        rounded_score = round(self.stats.score, -1) #Sets the value of nearest number multiple of 10
        score_str = f"{rounded_score:,}" #thousands separators
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        back_gr = self.score_image.get_at((0, 0))
        self.score_image.set_colorkey(back_gr)

        #Display score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.settings.screen_width - 20 #Review the book !
        self.score_rect.top = 20

    
    def show_score(self):
        #Draw score to the screen 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #We call draw on the gruop and pygame draws each ship
        self.ships.draw(self.screen) 


    def prep_high_score(self):
        #Turn the high score into a rendered image
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        back_gr = self.high_score_image.get_at((0, 0))
        self.high_score_image.set_colorkey(back_gr)

        #Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        #Check to see if there'se a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        #turn the level into a rendered image.
        level_str = str(self.stats.level)

        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        back_gr = self.level_image.get_at((0, 0))
        self.level_image.set_colorkey(back_gr)
        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        #Show how many ships are left 
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (40, 50))
            ship.rect = ship.image.get_rect(center = ship.rect.center)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y  = 10
            self.ships.add(ship)
        