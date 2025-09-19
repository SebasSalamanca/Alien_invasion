import pygame.font



class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        #Initialize scorekeeping attributes 

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
