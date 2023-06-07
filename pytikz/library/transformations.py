from plum import dispatch
from numbers import Number
import numpy as np
from ..vector import Transformation, VectorType


# EVERYTHING UNTESTED
# * May fail if VectorLike elements are feeded into the shift
# * This may actually be the intended behaviour


@dispatch
def rotate(theta: Number) -> Transformation:
    return Transformation(
        lambda v: np.array(
            [
                [np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)],
            ]
        )
        @ v
    )


@dispatch
def shift(vector: VectorType) -> Transformation:
    return Transformation(lambda v: v + vector)


@dispatch
def scale(factor: Number) -> Transformation:
    return Transformation(lambda v: factor * v)
