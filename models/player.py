"""This class will take care of the player functions"""
from .position import Position


class Player:
    """Contains all the actions the player can make.
    Args:
            level (obj): an instance of the Level class.
        Attributes:
            level (obj): an instance of the Level class.
            position (tuple): the coordinate of the player."""
    def __init__(self, level):
        self.level = level
        self.position = self.level.player_position

    def move(self, direction):
        """Action to modify the coordinate of the player according
        to a specified direction.
        Args:
                direction(str): the direction among 4 str possibles
                                "up", "down", "right", "left". """
        x, y = self.position
        new_position = getattr(Position(x, y), direction)()
        if new_position in self.level:
            self.position = tuple(new_position)
            print("New player position is :", self.position)

    # def pick_up_item(self):
    #     # if item position == player position
    #     # then add item to item_count
    #     # delete
    #     pass

# plm.move("up")
