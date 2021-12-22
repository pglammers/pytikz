from abc import ABC, abstractmethod
from typing import Union
from numbers import Number
from plum import dispatch
import numpy as np


# Revised 2021-12-22


# Vectors are represented by `np.ndarray`.
VectorType = np.ndarray


class Element(ABC):
    """Abstract class for elements of some set.

    An `Element` should carry only information necessary for describing the
    location of some vector. If an `Element` is not `VectorLike`, then it must
    be `Transformable` into a `VectorLike`.

    """


ElementLike = Union[VectorType, Element]


class EnhancedVector(Element):
    """Abstract class for elements that can be cast directly to `VectorType`."""

    @abstractmethod
    def vector(self) -> VectorType:
        """Returns the `VectorType` representation of the instance."""
        pass


VectorLike = Union[VectorType, EnhancedVector]


@dispatch
def Vector(vector: VectorType) -> VectorType:
    return vector


@dispatch
def Vector(enhanced_vector: EnhancedVector) -> VectorType:
    return enhanced_vector.vector()


@dispatch
def Vector(*args: Number) -> VectorType:
    return np.array(list(args))


@dispatch
def coordinate_string(v: VectorLike) -> str:
    v = Vector(v)
    if v.shape != (2,):
        raise TypeError(
            f"The `VectorLike` input has shape `{v.shape}` rather than `(2,)`."
        )
    return f"({v[0]}, {v[1]})"


class TransformationFuture(ABC):
    pass


class Transformable(ABC):
    """Abstract class for instances that may be subjected to `Transformable`."""

    @abstractmethod
    def copy(self) -> "Transformable":
        pass

    @abstractmethod
    def apply(self, transformation: TransformationFuture) -> None:
        pass


class Transformation:
    """Wrapper class for functions that act on `Transformable` instances."""

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

    @dispatch
    def anchor_resolve(self, vector: VectorLike) -> VectorType:
        """Returns the absolute position of a vector, given the anchor."""
        return Vector(self.anchor) + Vector(vector)


class AnchoredVector(EnhancedVector, AnchoredObject):
    """For instances which consist of an absolute and a relative `Vector`."""

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
