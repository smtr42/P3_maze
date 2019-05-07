import random


class Item:

    def __init__(self, level):
        self.level = level
        self.path_possibles = self.level.path_possibles
        self.items_coordinate = []
        print("Item_slot", self.path_possibles)
        self.place_item()

    def place_item(self):
        self.items_coordinate = random.sample(self.path_possibles, 3)
        self.level.set_items_position(self.items_coordinate)