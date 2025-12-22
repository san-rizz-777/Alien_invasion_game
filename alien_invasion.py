import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))      #Creates a screen obj with dimensions 1200 by 800 pixels
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen,ai_settings)

    # Start the main game loop
    while True:
       # Listening to events and updating the screen
       gf.check_events(ship)
       ship.update()
       gf.update_screen(ai_settings,screen,ship)

run_game()
