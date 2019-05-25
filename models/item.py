import random
import copy


class Item:

    def __init__(self, level):
        self.level = level
        self.path_possibles = self.level.path_possibles
        self.items_coordinate = []
        self.item_obj_position = {"aiguille": None, "ether": None, "seringue": None}
        self.place_item()

    def place_item(self):
        self.items_coordinate = random.sample(self.path_possibles, 3)
        b = copy.deepcopy(self.items_coordinate)
        for key in self.item_obj_position.keys():
            self.item_obj_position[key] = b.pop(0)

        self.level.set_items_position(self.items_coordinate)
        self.level.set_item_obj_position(self.item_obj_position)
