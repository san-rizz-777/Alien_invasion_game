import sys
import pygame
from time import sleep


from bullet import Bullet
from alien import Alien



def check_keydown_events(event,ship,ai_settings,screen,stats,bullets):
    """Handle keydown  events"""
    if event.key == pygame.K_RIGHT:
        ship.isMovingRight = True
    elif event.key == pygame.K_LEFT:
        ship.isMovingLeft = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stats.game_active = True



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

def check_events(ship,ai_settings,screen,bullets, play_button, stats, sb, aliens):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,stats,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, stats, sb, mouse_x, mouse_y, ship, screen, aliens, bullets,ai_settings)


def check_play_button(play_button, stats, sb, mouse_x, mouse_y, ship, screen, aliens, bullets,ai_settings):
    """Start a new game when player clicks the play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Reseting the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse
        pygame.mouse.set_visible(False)

        # Reset the game stats
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create the fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,ship,sb,aliens,bullets,play_button):
    """Update the images on screen and flip to new screen"""
    screen.fill(ai_settings.bg_color)
    # Redraw all the bullets behind the ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the score info
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()


    # Make the most recently draw screen visible
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,stats,sb,aliens,bullets):
    """Update the position of bullets and remove the old bullets from the bullets list"""
    bullets.update()

    # Get rid of old bullets(the ones that disappeared)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,ship,stats,sb,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,stats,sb,aliens,bullets):
    # Check for any bullets that have hit the aliens
    # If so delete both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += (ai_settings.alien_points*len(aliens))     # Scoring as per no. of aliens hit by each bullet
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens)==0:
        # Empty the existing bullets and create a new fleet and speed up the game.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase the level
        stats.level+=1
        sb.prep_level()

        create_fleet(ai_settings,screen,ship,aliens)

def get_number_rows(ai_settings,ship_height,alien_height):
    """Determine the number of available rows in the screen"""
    available_space_y = (ai_settings.screen_height - ship_height - (3*alien_height))
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows


def get_number_aliens_x(ai_settings,alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = (ai_settings.screen_width - 2* alien_width)
    number_of_aliens_x = int(available_space_x / 2* alien_width)
    return number_of_aliens_x

def create_alien(ai_settings,screen,aliens,alien_width,alien_number,y):
    # Create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien.x = 2*alien_width + 2* alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = y
    if alien.rect.x <= (ai_settings.screen_width - 2*alien_width):
        aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """Create the fleet of aliens"""
    # Create a full fleet of aliens
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # Create the fleet of aliens
    for rows in range(int(number_rows/2)):
        y = alien.rect.height + 2*alien.rect.height * rows + 30
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien.rect.width, alien_number,y)

def check_fleet_edges(ai_settings,aliens):
    """Respond appropriately if the alien is on the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed_factor
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets):
    """Respond to ship being hit by aliens"""
    if stats.ships_left > 1:

        # Decrement ships left.
        stats.ships_left -=1


        # Update the scoreboard for ships.
        sb.prep_ships()

        # Remove the existing fleet and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and recenter the ship.
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        # Pause the game.
        sleep(0.5)

    else:
        # Else if the amount of ships becomes zero stop the game and show the mouse and reset the score.
        stats.score = 0
        sb.prep_score()
        stats.ships_left -=1
        sb.prep_ships()
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,screen,ship,sb,aliens,bullets):
    """Check if any alien has reached to the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat it same as ship hit
            ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,sb,aliens,bullets):
    """Check if the fleet is at the edge and then update the position of all the aliens in the fleet"""
    check_fleet_edges(ai_settings,aliens)
    check_aliens_bottom(ai_settings,stats,screen,ship,sb,aliens,bullets)
    aliens.update()

    # Look for any alien-ship collosions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets)

def check_high_score(stats,sb):
    """To check the high score each time and update it."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

