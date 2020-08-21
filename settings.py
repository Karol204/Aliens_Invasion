

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
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
