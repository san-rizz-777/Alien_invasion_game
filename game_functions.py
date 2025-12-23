import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    """Handle keydown  events"""
    if event.key == pygame.K_RIGHT:
        ship.isMovingRight = True
    elif event.key == pygame.K_LEFT:
        ship.isMovingLeft = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

# Fire a bullet if limit not reached
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
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


def update_screen(ai_settings,screen,ship,bullets,aliens):
    """Update the images on screen and flip to new screen"""
    screen.fill(ai_settings.bg_color)
    # Redraw all the bullets behind the ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently draw screen visible
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,bullets):
    """Update the position of bullets and remove the old bullets from the bullets list"""
    bullets.update()

    # Get rid of old bullets(the ones that disappeared)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings,alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = (ai_settings.screen.get_width() - 2 * alien_width)
    number_of_aliens_x = int(available_space_x / 2 * alien_width)
    return number_of_aliens_x

def create_alien(ai_settings,screen,aliens,alien_width,alien_number):
    # Create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    """Create the fleet of aliens"""
    # Create a full fleet of aliens
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
       create_alien(ai_settings,screen,aliens,alien.rect.width,alien_number)
