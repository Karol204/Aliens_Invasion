import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class show single alien"""

    def __init__(self, ai_settings, screen):
        """Init alien and define his position"""
        super(Alien).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien's image and define his rect
        self.image = pygame.image.load('images/Alien.bmp')
        self.rect = self.image.get_rect()

        # Put new alien in left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Shown alien and his actual position"""
        self.screen.blit(self.image, self.rect)