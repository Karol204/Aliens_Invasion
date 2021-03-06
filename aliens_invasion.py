import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Game initialization, settings and screen set
    pygame.init()
    ai_settings = Settings()
    screen = pygame. display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens Invasion")

    # Create button Game
    play_button = Button(ai_settings, screen, "Play")

    # Create a new copy for keep data about game
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)

    # Creating alien
    # alien = Alien(ai_settings, screen)

    # Create ship group for hold bullet inside and another for aliens
    bullets = Group()
    aliens = Group()

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start loop of main part of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)



run_game()
