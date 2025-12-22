import sys
import pygame


from settings import Settings
from ship import Ship


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.isMovingRight = True
            elif event.key == pygame.K_LEFT:
                ship.isMovingLeft = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.isMovingRight = False
            elif event.key == pygame.K_LEFT:
                ship.isMovingLeft = False


def update_screen(ai_settings,screen,ship):
    """Update the images on screen and flip to new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()
