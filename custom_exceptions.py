"""Custom exceptions"""


class WinCondition(Exception):
    """Base class for others exceptions"""
    pass


class GameWinException(WinCondition):
    """Raised when the layer reach the finish position
    and have ALL the items"""
    pass


class GameOverException(WinCondition):
    """ Raised when the player reach the finish position
    but doesn't have all the items"""
    pass

