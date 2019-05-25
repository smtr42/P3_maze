"""A character at the end of the maze.
The game is over if the player reach him
without all the items"""


class GateKeeper:
    """
    The Gatekeeper class
    """
    def __init__(self, level):
        """
        Args:
            level (obj): the level instance so we can reach its values
        Attributes:
            level (obj): store the instance to access it
            position (list): get the finish position from level object
        """
        self.level = level
        self.position = self.level.get_finish_position