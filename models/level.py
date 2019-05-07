"""This module level will contain the Level class
in order to create and manage the maze.
"""
import settings


class Level:
    """This class will manage everything about the maze itself."""

    def __init__(self, filename):
        """ Args:
                filename (str): the path needed to load the file.
            Attributes:
                filename (str):the path needed to load the file.
                _paths (list): list of set for each place possible the
                        player can move on freely.
                _player (list): initial coordinate of the player.
                _finish (list): the coordinate where the player win the game
        """
        self.filename = filename
        self._paths = []
        self._player = []
        self._finish = []
        self._items = []
        self.load_txt()

    def __contains__(self, position):
        return position in self._paths

    def load_txt(self):
        """Load the data from the textfile and append
        each paths, player and finish position's coordinate into a list.
        Each line has coordinate "x"
        Each column has coordinate "y"
        """
        with open(self.filename, "r") as textfile:
            for x, line in enumerate(textfile):
                for y, col in enumerate(line):
                    if col == settings.CHAR_PATH:
                        self._paths.append((x, y))
                    if col == settings.CHAR_FINISH:
                        self._paths.append((x, y))
                        self._finish.append((x, y))
                    if col == settings.CHAR_PLAYER:
                        self._player.append((x, y))
                        self._paths.append((x, y))

    def __repr__(self):
        return f"Paths : {self._paths}\nPlayer : {self._player}\nFinish : {self._finish}"

    @property
    def player_position(self):
        return self._player[0]

    @property
    def path_possibles(self):
        return list(self._paths)

    @property
    def get_finish_position(self):
        return self._finish[0]

    @property
    def get_item_position(self):
        return list(self._items)

    def set_player_position(self, x):
        self._player[0] = x

    def set_items_position(self, x):
        self._items = x

