import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Ship and start position initialization"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load of ship image
        self.image = pygame.image.load('images/Spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # All of new ship appeared on bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Center point of the ship write as float
        self.center = float(self.rect.centerx)

        # Ship move option
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's location based on move option"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object
        self.rect.centerx = self.center

    def blitme(self):
        """Show actual position of ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put ship in the middle of the bottom edge of screen"""
        self.center = self.screen_rect.centerx