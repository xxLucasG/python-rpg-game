import enum

from .direction2d import Direction2D


class CardinalDirection(Direction2D):
    NORTH = Direction2D.UP
    EAST = Direction2D.RIGHT
    SOUTH = Direction2D.DOWN
    WEST = Direction2D.LEFT
