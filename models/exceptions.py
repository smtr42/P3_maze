"""Custom exceptions"""


class Wincondition(Exception):
    """Base class for others exceptions"""
    pass


class GameWinException(Wincondition):
    """Raised when the layer reach the finish position
    and have ALL the items"""
    pass


class GameOverException(Wincondition):
    """ Raised when the player reach the finish position
    but doesn't have all the items"""
    pass
