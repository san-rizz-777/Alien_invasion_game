class Settings():
    """A class to store all settings for Alien Invasion game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # Ship's speed factor
        self.ship_speed_factor = 1.5