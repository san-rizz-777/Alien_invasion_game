import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to represent the scoring information."""
    def __init__(self,ai_settings,screen,stats):
        """Initialize the score-keeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_settings

        # Font settings for storing the information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # Prepare the inital stat images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """To display the current level."""
        # Get the image
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Position the image
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right  = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_high_score(self):
        """To display the high score."""
        rounded_high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(rounded_high_score)

        # To render the image
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_score(self):
        """Turn the score into rendered image."""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw the ships
        self.ships.draw(self.screen)
