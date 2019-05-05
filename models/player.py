from .position import Position


class Player:

    def __init__(self, level):
        self.level = level
        self.position = self.level.player_position

    def move(self, direction):
        x, y = self.position
        new_position = getattr(Position(x, y), direction)()
        if new_position in self.level:
            self.position = tuple(new_position)

    # def pick_up_item(self):
    #     # if item position == player position
    #     # then add item to item_count
    #     # delete
    #     pass

# plm.move("up")
