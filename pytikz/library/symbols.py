from plum import dispatch
from numbers import Number
import numpy as np
from ..shape import ClosedPath
from .transformations import rotate


# EVERYTHING UNTESTED


_mask_plus_diameter = np.array(
    [
        [1, 0],
        [0, 0],
        [0, 1],
        [0, 1],
        [0, 0],
        [-1, 0],
        [-1, 0],
        [0, 0],
        [0, -1],
        [0, -1],
        [0, 0],
        [1, 0],
    ]
)


_mask_plus_thickness = np.array(
    [
        [0, 1],
        [1, 1],
        [1, 0],
        [-1, 0],
        [-1, 1],
        [-0, 1],
        [-0, -1],
        [-1, -1],
        [-1, -0],
        [1, -0],
        [1, -1],
        [0, -1],
    ]
)


_mask_minus_diameter = np.array([[1, 0], [-1, 0], [-1, 0], [1, 0]])


_mask_minus_thickness = np.array([[0, 1], [0, 1], [0, -1], [0, -1]])


@dispatch
def path_plus(diameter: Number, thickness: Number) -> ClosedPath:
    return ClosedPath(diameter * _mask_plus_diameter + thickness * _mask_plus_thickness)


@dispatch
def path_minus(diameter: Number, thickness: Number) -> ClosedPath:
    return ClosedPath(
        diameter * _mask_minus_diameter + thickness * _mask_minus_thickness
    )


@dispatch
def path_x(diameter: Number, thickness: Number) -> ClosedPath:
    return rotate(np.pi / 4)(path_plus(diameter, thickness))
