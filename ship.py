import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self,screen,ai_settings):
        super().__init__()
        # Initalize the ship and set it's starting position
        self.screen = screen
        self.ai_settings = ai_settings

        # Flag for movement
        self.isMovingRight = False
        self.isMovingLeft = False

        # Load the ship image and load it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for ship's center
        self.center = float(self.rect.centerx)


    def blitme(self):
        # Draw the ship at it's current location
        self.screen.blit(self.image,self.rect)

    # To update the position of ship
    def update(self):
        if self.isMovingRight and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.isMovingLeft and self.rect.left > 0:
            self.center-=self.ai_settings.ship_speed_factor

        # Update the rect object from self.center
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx