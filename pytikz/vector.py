from abc import ABC, abstractmethod
import numpy as np


# Implementation of Vector and of the string representation of Vector


def _tikz_representation(array):
    """Alternative .__str__ method for np.ndarray."""
    if array.ndim == 1:
        return f"({', '.join(str(c) for c in array)})"
    elif array.ndim == 2:
        return " -- ".join(str(v) for v in array)
    else:
        raise ValueError(
            f"Arrays of dimension {array.ndim} have no TikZ representation."
        )


np.set_string_function(
    _tikz_representation, False
)  # Presents this .__str__ method to np.


VectorType = type(np.array([]))


class VectorLike(ABC):
    @property
    @abstractmethod
    def vector(self):
        pass

    def __str__(self):
        return str(self.vector)


def Vector(*args):
    """Generates a vector; used to control its generation."""
    args = list(args)
    if len(args) == 1 and isinstance(args[0], VectorType):
        return args[0]
    elif len(args) == 1 and isinstance(args[0], VectorLike):
        return args[0].vector
    else:
        return np.array(args)


# Implementation of transformations


class Shiftable(ABC):
    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def apply(self, transformation):
        pass


class Scalable(Shiftable):
    pass


class Transformable(Scalable):
    pass


class Transformation:

    _subject_type = Transformable

    def __init__(self, transformation):
        self._transformation = transformation

    def __call__(self, subject, inplace=False):
        if isinstance(subject, VectorType):
            return self._transformation(subject)
        elif not isinstance(subject, self._subject_type):
            raise ValueError(subject, self._subject_type)
        else:
            if not inplace:
                subject = subject.copy()
            subject.apply(self)
            return subject


class Scaling(Transformation):

    _subject_type = Scalable

    def __init__(self, x, y, origin=Vector(0, 0)):
        self.x = x
        self.y = y
        self.origin = origin

    def _transformation(self, vector):
        return Vector(
            self.x * (vector[0] - self.origin[0]), self.y * (vector[1] - self.origin[1])
        )


class Shift(Scaling):

    _subject_type = Shiftable

    def __init__(self, origin):
        self.x = 1
        self.y = 1
        self.origin = origin


def compose(a, b):
    return lambda v: a(b(v))


# Definition of AnchoredObject and implementation of AnchoredVector


class AnchoredObject(ABC):
    """Implements the .anchor property."""

    anchor = None

    def apply(self, transformation):
        """Distributes the application of the transformation."""
        if self.anchor is None:
            self.apply_internally(transformation)
        else:
            self.anchor = transformation(self.anchor)
        return self

    def anchor_resolve(self, vector):
        if self.anchor is None:
            return Vector(vector)
        else:
            return Vector(vector) + Vector(self.anchor)


class AnchoredVector(VectorLike, AnchoredObject, Transformable):
    def __init__(self, anchor, offset):
        self.anchor = anchor
        self.offset = offset

    @property
    def vector(self):
        return self.anchor_resolve(self.offset)

    def copy(self):
        return AnchoredVector(self.anchor, self.offset)
