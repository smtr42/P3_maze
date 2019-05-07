"""This class will take care of the player functions"""
import settings
import exceptions
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
        self.gk_position = self.level.get_finish_position
        self.item_position = []

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
            self.level.set_player_position(self.position)
            print("New player position is :", self.position)

    def pickup_item(self):
        self.item_position = self.level.get_item_position
        if self.position in self.item_position:
            self.item_position.remove(self.position)
            self.level.set_items_position(self.item_position)

    @property
    def item_count(self):
        return settings.ITEMS_CREATED - len(self.item_position)

    def check_victory_condition(self):
        try:
            if self.position == self.gk_position and self.item_count == settings.ITEMS_CREATED:
                raise exceptions.GameWinException
            elif self.position == self.gk_position and self.item_count != settings.ITEMS_CREATED:
                raise exceptions.GameOverException
        except GameWinException:
            pass
        except GameOverException:
            pass
