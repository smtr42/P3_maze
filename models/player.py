"""This class will take care of the player functions"""
import settings as st
import custom_exceptions as cexcept
from .position import Position


class Player:
    """Contains all the actions the player can make.
    Args:
            level (obj): an instance of the Level class.
        Attributes:
            level (obj): an instance of the Level class.
            position (tuple): the coordinate of the player."""

    def __init__(self, level, settings):
        self.settings = settings
        self.level = level
        self.position = self.level.player_position
        self.gatekeeper_position = self.level.get_finish_position
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
        return self.settings.item_created - len(self.item_position)

    def check_victory_condition(self):
        try:
            if self.position == self.gatekeeper_position and self.item_count == self.settings.item_created:
                raise cexcept.GameWinException
            elif self.position == self.gatekeeper_position and self.item_count != self.settings.item_created:
                print("conditions de defaite remplie")
                raise cexcept.GameOverException
        except cexcept.GameWinException:
            print("You win, the guard fell asleep. And you could escape.")
            return False
        except cexcept.GameOverException:
            print("you failed to stun the guard. You lack some items to do so.")
            return False
