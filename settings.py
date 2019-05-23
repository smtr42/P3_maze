CHAR_WALL = "#"
CHAR_PATH = "0"
CHAR_PLAYER = "S"
CHAR_FINISH = "F"


# NBR_SPRITES = 15
# SIZE_SPRITE = 32
# LEVEL_SIZE = NBR_SPRITES * SIZE_SPRITE

class Settings:
    def __init__(self):
        """initialize the game's settings"""
        self.item_created = 3
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.sprites_number = 15
        self.size_sprite = 32
        self.level_size = self.sprites_number * self.size_sprite
