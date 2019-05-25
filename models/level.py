"""This module level will contain the Level class
in order to create and manage the maze.
"""
import settings


class Level:
    """This class will manage everything about the maze itself."""

    def __init__(self, filename):
        """
        Args:
            filename (str): the path needed to load the file.
        Attributes:
            filename (str):the path needed to load the file.
            _paths (list): list of set for each place possible the
            player can move on freely.
            _player (list): initial coordinate of the player.
            _finish (list): the coordinate where the player win the
            game.
            _items (list): the coordinates where the items are placed.
            _wall (list): the coordinates where the walls are
            placed.
            _item_obj_position (dict): each item name has a
            corresponding position.
        """
        self.filename = filename
        self._paths = []
        self._player = []
        self._finish = []
        self._items = []
        self._wall = []
        self._item_obj_position = {}
        self.load_txt()

    def __contains__(self, position):
        """
        Args:
            position (obj): needed so we can use 'in' comparison over
            the level object.
        Return:
            return what asked for from the _paths attribute for
            comparison.
        """
        return position in self._paths

    def load_txt(self):
        """
        Load the data from the textfile and append each paths, player
        and finish position's coordinate into a list.
        Each line has coordinate "x".
        Each column has coordinate "y".
        Modifications will be made for pygame use in display.py.
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
                    if col == settings.CHAR_WALL:
                        self._wall.append((x, y))

    def __repr__(self):
        return f"Paths : {self._paths}\nPlayer : {self._player}\nFinish : {self._finish}"

    @property
    def player_position(self):
        """
        Getter that return the player position as a tuple.
        """
        return self._player[0]

    @property
    def path_possibles(self):
        """
        Getter that return all the walkable paths as a list.
        """
        return list(self._paths)

    @property
    def get_finish_position(self):
        """
        Getter that return the finish/gatekeeper position as a tuple.
        """
        return self._finish[0]

    @property
    def get_item_position(self):
        """
        Getter that return the items position as a list.
        """
        return list(self._items)

    def set_player_position(self, x):
        self._player[0] = x

    def set_items_position(self, x):
        self._items = x

    @property
    def get_wall_positions(self):
        """
        Getter that return the walls position as a list.
        """
        return list(self._wall)

    @property
    def get_item_obj_position(self):
        """
        Getter that return the item position linked to each item as dict.
        """
        return self._item_obj_position

    def set_item_obj_position(self, x):
        self._item_obj_position = x
