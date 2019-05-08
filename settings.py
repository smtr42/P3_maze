CHAR_WALL = "#"
CHAR_PATH = "0"
CHAR_PLAYER = "S"
CHAR_FINISH = "F"


class Settings:
    def __init__(self):
        """initialize the game's settings"""
        self.item_created = 3
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
