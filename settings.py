class Settings():
    """A class to store all settings for Alien Invasion game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # Ship's speed factor
        self.ships_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed_factor = 6


        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Score points
        self.alien_points = 50

        # How quickly the alien_points increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize the game's static settings."""
        self.ship_speed_factor = 7
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 0.2

        # fleet direction of 1 represents right, -1 represents the left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings and alien points"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
