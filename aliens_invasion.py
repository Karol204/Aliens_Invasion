import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Game initialization, settings and screen set
    pygame.init()
    ai_settings = Settings()
    screen = pygame. display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens Invasion")
    ship = Ship(ai_settings, screen)

    # Create group for hold bullet inside
    bullets = Group()

    # Change color of background
    bg_color = (200, 200, 200)

    # Start loop of main part of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # gf.check_events(ship)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets ))
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
