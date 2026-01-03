import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))      #Creates a screen obj with dimensions 1200 by 800 pixels
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen,ai_settings)

    #Make a group of bullets
    bullets = Group()

    # Make an alien
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Create a instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # Make the button
    play_button = Button(ai_settings,screen,"Play")

    # Start the main game loop
    while True:
       # Listening to events and updating the screen
       gf.check_events(ship,ai_settings,screen,bullets, play_button, stats, sb, aliens)

       # Check if the game is over or not
       if stats.game_active:
           ship.update()
           gf.update_bullets(ai_settings,screen,ship,stats,sb,aliens,bullets)
           gf.update_aliens(ai_settings,stats,screen, ship,sb,aliens,bullets)
       gf.update_screen(ai_settings,screen,stats,ship,sb,aliens,bullets,play_button)


run_game()
