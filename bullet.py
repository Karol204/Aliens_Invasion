import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class created for menage shooted bullets from ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet's object in current ship position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create square of bullet in position(0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Position