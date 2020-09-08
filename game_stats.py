

class GameStats():
    """Monitoring data in game"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # Launch game
        self.game_active = False

        # Best score
        self.high_score = 0

    def reset_stats(self):
        """Init data that can change in game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
