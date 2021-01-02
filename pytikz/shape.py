from abc import ABC, abstractmethod
import numpy as np
from .vector import Vector, VectorType
from .abstract import AbstractList


class Shape(ABC):
    """Abstract Shape class.

    Instances of subclasses must describe the abstract information of a shape.
    They must also be able to handle a transformation which maps the shape to another vector space.
    If the instance has an anchor, then the transformation is applied only to this anchor,
    not the full shape.
    """

    cycle = False
    anchor = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def apply_internally(self, transformation):
        pass

    def apply(self, transformation):
        """Distributes the application of the transformation."""
        if self.anchor is None:
            self.apply_internally(transformation)
        else:
            self.anchor = transformation(self.anchor)
        return self

    def _view(self, item):
        if self.anchor is None:
            return item
        else:
            return self.anchor + item


class Path(Shape, AbstractList):
    """Class for describing straight lines connecting a sequence of vectors."""

    _type = VectorType

    def __init__(self, vector_list, cycle=False, anchor=None):
        self._list = []
        for vector in vector_list:
            self.append(vector)
        self.cycle = cycle
        self.anchor = anchor

    @classmethod
    def rectangle(self, left, right, lower, upper, anchor=None):
        """Alternative constructor for generating a rectangle in the obvious way."""
        vector_list = [
            Vector(left, lower),
            Vector(left, upper),
            Vector(right, upper),
            Vector(right, lower),
        ]
        return self(vector_list, True, anchor)

    def __str__(self):
        """Generates the path string, using the custom np.ndarray.__str__ method."""
        cycle = " -- cycle" if self.cycle else ""
        return f"{str(np.array([v for v in self]))}{cycle}"

    def copy(self):
        return Path(self._list, self.cycle, self.anchor)

    def apply_internally(self, transformation):
        """Applies the transformation to the vectors in .vector_list."""
        self._list = [transformation(v) for v in self._list]


class Circle(Shape):

    cycle = True

    def __init__(self, center, radius, anchor=None):
        self._center = center
        self.radius = radius
        self.anchor = anchor

    @property
    def center(self):
        return self._view(self._center)

    def __str__(self):
        return f"{str(self.center)} circle ({self.radius})"

    def copy(self):
        return Circle(self._center, self.radius, self.anchor)

    def apply_internally(self, transformation):
        self._center = transformation(self._center)
