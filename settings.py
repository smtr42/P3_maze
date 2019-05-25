"""
The settings used for configuration of the game
"""

CHAR_WALL = "#"
CHAR_PATH = "0"
CHAR_PLAYER = "S"
CHAR_FINISH = "F"


class Settings:
    """This is the settings class with no method"""
    def __init__(self):
        """initialize the game's settings
        Attributes:
            item_created (int): the number of item created
            sprites_number (int): the number of sprites
            size_sprite (in): the size in pixel of each sprites of the
                            game
            level_size (int): gives the size of a side of the screen.
            """
        self.item_created = 3
        self.sprites_number = 15
        self.size_sprite = 32
        self.level_size = self.sprites_number * self.size_sprite
