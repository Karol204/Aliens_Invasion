import sys
import pygame
from settings import Settings

def run_game():
    # Game initialization, settings and screen set
    pygame.init()
    ai_settings = Settings()
    screen = pygame. display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens Invasion")

    # Change color of background
    bg_color = (200, 200, 200)

    # Start loop of main part of the game
    while True:

        # Waiting for push any button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Refreshing screen
        screen.fill(ai_settings.bg_color)

        # Show last modified screen
        pygame.display.flip()

run_game()
