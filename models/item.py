"""This is the Item class it does everything related to it.
"""
import random
import copy


class Item:
    """
    The Item object.
    """

    def __init__(self, level):
        """
        Args:
            level (object): to retrieve coordinates.

        Attributes:
            level (obj): store the level instance.
            _paths_possibles (list): list of the path possible to
                                    walk onto.
            finish_position (list): list of one tuple with finish
                                    coordinate.
            items_coordinate (list): list of the coordinate of
                                    each item.
            item_obj_position (dict): the name of the object is
                                     linked to a position.
        """
        self.level = level
        self.path_possibles = self.level.path_possibles
        self.finish_position = self.level.get_finish_position
        self.items_coordinate = []
        self.item_obj_position = {"aiguille": None, "ether": None,
                                  "seringue": None,
                                  }
        self.place_item()

    def place_item(self):
        """
        Place randomly the items on walkable path and modify every
        attributes related with the new positions.

        """
        path_possibles_for_item = copy.deepcopy(self.path_possibles)
        # We need to remove the gatekeeper position or an item can appear
        # at the same place
        path_possibles_for_item.remove(self.finish_position)
        self.items_coordinate = random.sample(path_possibles_for_item, 3)
        b = copy.deepcopy(self.items_coordinate)
        # Link the item name with its position in a dictionary
        for key in self.item_obj_position.keys():
            self.item_obj_position[key] = b.pop(0)
        # Updating the values into level object
        self.level.set_items_position(self.items_coordinate)
        self.level.set_item_obj_position(self.item_obj_position)
