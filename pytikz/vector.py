from abc import ABC, abstractmethod
from typing import Union
from numbers import Number
from plum import dispatch
import numpy as np


class Point(ABC):
    """Abstract class for instances that represent a point in some space."""


class EnhancedVector(Point):
    """Abstract class for points that can be cast directly to VectorType."""

    @abstractmethod
    def vector(self) -> np.ndarray:
        """Returns the VectorType representation of the instance."""
        pass


# The following composed types are defined in increasing order of generality.
VectorType = np.ndarray
VectorLike = Union[VectorType, EnhancedVector]
PointLike = Union[VectorType, Point]


@dispatch
def Vector(vector: np.ndarray) -> np.ndarray:
    return vector


@dispatch
def Vector(enhanced_vector: EnhancedVector) -> np.ndarray:
    return enhanced_vector.vector()


@dispatch
def Vector(*args: Number) -> np.ndarray:
    return np.array(list(args))


@dispatch
def coordinate_string(v: VectorLike) -> str:
    v = Vector(v)
    if v.shape != (2,):
        raise Exception
    return f"({v[0]}, {v[1]})"


class TransformableFuture(ABC):
    pass


class TransformationFuture(ABC):
    pass


class Transformable(TransformableFuture):
    """Abstract class for instances that may be subjected to Transformables."""

    @abstractmethod
    def copy(self):
        """Returns a copy of the instance."""

    @abstractmethod
    def apply(self, transformation: TransformationFuture) -> None:
        """Applies the transformation internally to the instance."""


class Transformation:
    """Wrapper class for functions that act on Transformable instances."""

    def __init__(self, transformation):
        self._transformation = transformation

    @dispatch
    def __call__(self, subject: VectorType):
        return self._transformation(subject)

    @dispatch
    def __call__(self, subject: Transformable, *, inplace=False):
        if inplace:
            subject.apply(self)
        else:
            subject = subject.copy()
            subject.apply(self)
            return subject

    @dispatch
    def __mul__(self, other: "Transformation"):
        return Transformation(lambda x: self._transformation(other._transformation(x)))


class AnchoredObject(Transformable):
    """Abstract class for anchored instances.

    Transformations are applied to the anchor only.
    """

    anchor = None

    @dispatch
    def apply(self, transformation: Transformation):
        self.anchor = transformation(self.anchor)

    def anchor_resolve(self, vector: VectorLike) -> VectorType:
        """Returns the absolute position of a vector, given the anchor."""
        return Vector(self.anchor) + Vector(vector)


class AnchoredVector(EnhancedVector, AnchoredObject):
    """EnhancedVector instance which consists of an absolute and a relative vector."""

    @dispatch
    def __init__(self, anchor: VectorType, offset: VectorType):
        self.anchor = anchor
        self.offset = offset

    @dispatch
    def vector(self) -> VectorType:
        return self.anchor_resolve(self.offset)

    @dispatch
    def copy(self) -> "AnchoredVector":
        return AnchoredVector(self.anchor, self.offset)
