"""A character at the end of the maze.
The game is over if the player reach him
without all the items"""


class GateKeeper:

    def __init__(self, level):
        self.level = level
        self.position = self.level.get_finish_position
