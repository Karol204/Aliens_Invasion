import pygame

class Ship():

    def __init__(self, screen):
        """Ship and start position initialization"""
        self.screen = screen

        # Load of ship image
        self.image = pygame.image.load('images/Spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # All of new ship appeared on bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship move option
        self.moving_right = False

    def update(self):
        """Update ship's location based on move option"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Show actual position of ship"""
        self.screen.blit(self.image, self.rect)