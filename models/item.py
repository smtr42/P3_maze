import random
import copy


class Item:

    def __init__(self, level):
        self.level = level
        self.path_possibles = self.level.path_possibles
        self.finish_position = self.level.get_finish_position
        self.items_coordinate = []
        self.item_obj_position = {"aiguille": None, "ether": None, "seringue": None}
        self.place_item()

    def place_item(self):
        path_possibles_for_item = copy.deepcopy(self.path_possibles)
        path_possibles_for_item.remove(self.finish_position)
        self.items_coordinate = random.sample(path_possibles_for_item, 3)
        b = copy.deepcopy(self.items_coordinate)
        for key in self.item_obj_position.keys():
            self.item_obj_position[key] = b.pop(0)

        self.level.set_items_position(self.items_coordinate)
        self.level.set_item_obj_position(self.item_obj_position)
