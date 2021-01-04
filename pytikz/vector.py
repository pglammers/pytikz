import numpy as np
from abc import ABC, abstractmethod


def _tikz_representation(array):
    """Alternative .__str__ method for np.ndarray."""
    if array.ndim == 1:
        return f"({', '.join([str(c) for c in array])})"
    elif array.ndim == 2:
        return " -- ".join(str(v) for v in array)
    else:
        raise ValueError(
            f"Arrays of dimension {array.ndim} have no TikZ representation."
        )


np.set_string_function(
    _tikz_representation, False
)  # Presents this .__str__ method to np.


def Vector(*args):
    """Generates a vector; used to control its generation."""
    return np.array(list(args))


VectorType = type(Vector())


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
            raise ValueError
        else:
            if not inplace:
                subject = subject.copy()
            subject.apply(self._transformation)
            return subject


class Scaling(Transformation):

    _subject_type = Scalable

    def __init__(self, x, y, origin=Vector(0, 0)):
        self.x = x
        self.y = y
        self.origin = origin

    def _transformation(self, vector):
        return Vector(self.x * vector[0], self.y * vector[1]) + self.origin


class Shift(Scaling):

    _subject_type = Shiftable

    def __init__(self, origin):
        self.x = 1
        self.y = 1
        self.origin = origin


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
            return vector
        else:
            return vector + self.anchor


class AnchoredVector(AnchoredObject, Transformable):
    def __init__(self, anchor, offset):
        self.anchor = anchor
        self.offset = offset

    def __str__(self):
        return str(self.anchor_resolve(self.offset))

    def copy(self):
        return AnchoredVector(self.anchor, self.offset)
