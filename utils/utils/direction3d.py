import enum

from .direction2d import Direction2D


class Direction3D(Direction2D):
    FORWARD = enum.auto()
    BACKWARD = enum.auto()
