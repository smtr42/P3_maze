"""This module will contain everything about
the position : calculations and checks, either
for the player or the items"""


# from .level import Level

class Position:
    """This class will calculate every position
    according to the direction provided"""

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __eq__(self, pos):
        return self.position == pos

    def __hash__(self):
        return hash(self.position)

    def __iter__(self):
        for i in self.position:
            yield i

    def up(self):
        x, y = self.position
        return self.__class__(x - 1, y)

    def down(self):
        x, y = self.position
        return self.__class__(x + 1, y)

    def right(self):
        x, y = self.position
        return self.__class__(x, y + 1)

    def left(self):
        x, y = self.position
        return self.__class__(x, y - 1)
