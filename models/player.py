"""This class will take care of the player functions"""
from .position import Position


class Player:
    """
    Contains all the actions the player can make.
    """

    def __init__(self, level, settings):
        """
        Args:
            level (obj): instance of the Level class.
            settings (obj): instance of the settings class.
        Attributes:
            settings (obj): instance of the settings class.
            level (obj): instance of the Level class.
            item_obj_position (dict): each item name has a
                                    corresponding position.
            position (tuple): the coordinate of the player.
            gatekeeper_position (tuple): the finnish position.
            item_position (list): the item coordinates.
            victory_condition (bool): used to know if win or fail.
            item_counter (int): count every item picked up by the player.
        """
        self.settings = settings
        self.level = level
        self.item_obj_position = self.level.get_item_obj_position
        self.position = self.level.player_position
        self.gatekeeper_position = self.level.get_finish_position
        self.item_position = []
        self.victory_condition = None
        self.item_counter = 0

    def move(self, direction):
        """
        Action to modify the coordinate of the player according
        to a specified direction.
        Args:
            direction(str): the direction among 4 str possibles
                            "up", "down", "right", "left".
        """
        x, y = self.position
        new_position = getattr(Position(x, y), direction)()
        if new_position in self.level:
            # That's where the __contains__ method is useful in level.py
            self.position = tuple(new_position)
            self.level.set_player_position(self.position)

    def pickup_item(self):
        """
        The method adding item to the counter and delete the ones
        picked up from the dict
        """
        for item in self.item_obj_position.keys():
            # Comparing the player position to the items positions
            if self.item_obj_position.get(item) == self.position:
                del self.item_obj_position[item]
                self.item_counter += 1
                break

    # @property
    # def item_count(self):
    #     """
    #     Getter that returns
    #     """
    #     return self.settings.item_created - len(self.item_position)

    def check_victory_condition(self):
        """
        Check the victory conditions and change the boolean
        victory_condition accordingly
        """
        if self.position == self.gatekeeper_position and self.item_counter == self.settings.item_created:
            self.victory_condition = True
        elif self.position == self.gatekeeper_position and self.item_counter != self.settings.item_created:
            self.victory_condition = False
