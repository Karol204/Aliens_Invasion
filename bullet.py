import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class created for menage shot bullets from ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet's object in current ship position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create square of bullet in position(0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Position of the bullet with use float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Bullet's move"""
        # Update bullet position
        self.y -= self.speed_factor

        # Update of bullet's rect position

        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
