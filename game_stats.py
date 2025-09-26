class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        #Initialize statistics 
        self.settings = ai_game.settings
        self.high_score_stored = ai_game.new_score.get_stored_score()
        self.reset_stats()

        #High score should never be reset
        self.high_score = self.high_score_stored
         

    def reset_stats(self):
        # Initialize statistics that can change during the game.
        self.ships_left = self.settings.ship_limit
        self.score = 0 
        self.level = 1