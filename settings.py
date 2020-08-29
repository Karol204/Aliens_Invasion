

class Settings():
    """Class is made for keeping all settings in game"""

    def __init__(self):
        """Settings initialization"""

        # Screen settings
        self.screen_width = 1720
        self.screen_height = 1024
        self.bg_color = (200, 200, 200)

        # Ship settings
        self.ship_speed_factor = 2.5

        # Bullet's settings
        self.bullet_speed_factor = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Aien's settings
        self.alien_factor_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction set 1 is move right and -1 is left
        self.fleet_direction = 1