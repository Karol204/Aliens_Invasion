

class Settings():
    """Class is made for keeping all settings in game"""

    def __init__(self):
        """Settings initialization"""

        # Screen settings
        self.screen_width = 1720
        self.screen_height = 1024
        self.bg_color = (200, 200, 200)

        # Ship settings
        self.ship_limit = 1

        # Bullet's settings
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5000

        # Alien's settings
        self.fleet_drop_speed = 10



        # Easy speed change
        self.speedup_scale = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings, which change in game"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_factor_speed = 1

        # fleet_direction set 1 is move right and -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Change speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_factor_speed *= self.speedup_scale