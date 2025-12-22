import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    """Handle keydown  events"""
    if event.key == pygame.K_RIGHT:
        ship.isMovingRight = True
    elif event.key == pygame.K_LEFT:
        ship.isMovingLeft = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the group
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.isMovingRight = False
    elif event.key == pygame.K_LEFT:
        ship.isMovingLeft = False

def check_events(ship,ai_settings,screen,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
    """Update the images on screen and flip to new screen"""
    screen.fill(ai_settings.bg_color)
    # Redraw all the bullets behind the ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()
