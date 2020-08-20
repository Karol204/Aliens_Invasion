import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Game initialization, settings and screen set
    pygame.init()
    ai_settings = Settings()
    screen = pygame. display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens Invasion")
    ship = Ship(screen)

    # Change color of background
    bg_color = (200, 200, 200)

    # Start loop of main part of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
