class GameStats():
    """Track statistics about the game"""

    def __init__(self,ai_settings):
        """Initialize the statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # start the alien invasion in inactive state
        self.game_active = False
        self.score = 0

    def reset_stats(self):
        """Initialize the statistics that can change during the game."""
        self.ships_left = self.ai_settings.ships_limit
