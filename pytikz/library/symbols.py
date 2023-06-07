from plum import dispatch
from numbers import Number
import numpy as np
from ..vector import AnchoredVector
from ..shape import ClosedPath
from .transformations import rotate


# EVERYTHING UNTESTED


_mask_minus_diameter = np.array([[1, 0], [-1, 0], [-1, 0], [1, 0]])


_mask_minus_thickness = np.array([[0, 1], [0, 1], [0, -1], [0, -1]])


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


_theta = np.pi / 4
_rotation = np.array(
    [[np.cos(_theta), -np.sin(_theta)], [np.sin(_theta), np.cos(_theta)]]
)
_mask_x_diameter = _mask_plus_diameter @ _rotation
_mask_x_thickness = _mask_plus_thickness @ _rotation


def _def_anchor_zip(m1, m2):
    return [AnchoredVector(v1, v2) for (v1, v2) in zip(m1, m2)]


def _path_from_data(mask1, mask2, n1, n2, offset_n1, offset_n2):
    return ClosedPath(
        _def_anchor_zip(n1 * mask1 + n2 * mask2, offset_n1 * mask1 + offset_n2 * mask2)
    )


@dispatch
def path_minus(
    diameter: Number,
    thickness: Number,
    *,
    offset_diameter: Number = 0,
    offset_thickness: Number = 0,
) -> ClosedPath:
    return _path_from_data(
        _mask_minus_diameter,
        _mask_minus_thickness,
        diameter,
        thickness,
        offset_diameter,
        offset_thickness,
    )


@dispatch
def path_plus(
    diameter: Number,
    thickness: Number,
    *,
    offset_diameter: Number = 0,
    offset_thickness: Number = 0,
) -> ClosedPath:
    return _path_from_data(
        _mask_plus_diameter,
        _mask_plus_thickness,
        diameter,
        thickness,
        offset_diameter,
        offset_thickness,
    )


@dispatch
def path_x(
    diameter: Number,
    thickness: Number,
    *,
    offset_diameter: Number = 0,
    offset_thickness: Number = 0,
) -> ClosedPath:
    return _path_from_data(
        _mask_x_diameter,
        _mask_x_thickness,
        diameter,
        thickness,
        offset_diameter,
        offset_thickness,
    )
