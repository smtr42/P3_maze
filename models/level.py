"""This module level will contain the Level class
in order to create and manage the maze
"""
import settings


class Level:
    """This class will manage everything about the maze itself"""

    def __init__(self, filename):
        """ Args:

        """
        self.filename = filename
        self.paths = []
        self.player = []
        self.finish = []

    def load_txt(self):
        """Load the data from the textfile and append
        each paths, player and finish position's coordinate into a list.
        Each line ha coordinate "x"
        Each column has coordinate "y"

        Args :
            filename (str): giving textfile path
        """
        with open(self.filename, "r") as textfile:
            for x, line in enumerate(textfile):
                for y, col in enumerate(line):
                    if col == settings.CHAR_PATH:
                        self.paths.append((x, y))
                    if col == settings.CHAR_FINISH:
                        self.paths.append((x, y))
                        self.finish.append((x, y))
                    if col == settings.CHAR_PLAYER:
                        self.player.append((x, y))
                        self.paths.append((x, y))


level = Level("map.txt")

level.load_txt()
