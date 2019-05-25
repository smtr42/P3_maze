"""This module will contain everything about the position :
calculations and checks, either for the player or the items."""


class Position:
    """This class will calculate every position
    according to the direction provided."""

    def __init__(self, x, y):
        """ Args:
                x (int): refers to the line number.
                y (int): refers to the column number.
            Attributes:
                position (tuple): couple of coordinate from x and y."""
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __eq__(self, pos):
        """This will enable the comparison between the attribute
        position of the class Position and other coordinates."""
        return self.position == pos

    # def __hash__(self):
    #     return hash(self.position)

    def __iter__(self):
        """So the object returned can be transformed in a tuple or
        list, it must be an iterable. See player.move(direction) method.
        """
        for i in self.position:
            yield i

    def up(self):
        """Takes the position and calculate a new one according to the
        direction.
        Returns:
            the object Position itself with new coordinates
                """
        x, y = self.position
        return self.__class__(x - 1, y)

    def down(self):
        """Takes the position and calculate a new one according to the
        direction.
        Returns:
            the object Position itself with new coordinates
                """
        x, y = self.position
        return self.__class__(x + 1, y)

    def right(self):
        """Takes the position and calculate a new one according to the
        direction.
        Returns:
            the object Position itself with new coordinates
                """
        x, y = self.position
        return self.__class__(x, y + 1)

    def left(self):
        """Takes the position and calculate a new one according to the
        direction.
        Returns:
            the object Position itself with new coordinates
                """
        x, y = self.position
        return self.__class__(x, y - 1)
