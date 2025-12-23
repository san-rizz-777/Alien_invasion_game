class Settings():
    """A class to store all settings for Alien Invasion game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # Ship's speed factor
        self.ship_speed_factor = 7

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed_factor = 3
        # fleet direction of 1 represents right, -1 represents the left.
        self.fleet_direction = 1