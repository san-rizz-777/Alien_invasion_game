import pygame.font

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

        # Prepare the inital score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
