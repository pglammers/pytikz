from abc import ABC, abstractmethod
import numpy as np
from .vector import Vector


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


class Path(Shape):
    """Class for describing straight lines connecting a sequence of vectors."""

    def __init__(self, vector_list, cycle=False, anchor=None):
        self.vector_list = vector_list
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

    def __getitem__(self, arg):
        """Returns the anchor-shifted version of the n-th vector."""
        if self.anchor is None:
            return self.vector_list[arg]
        else:
            return self.anchor + self.vector_list[arg]

    def __iter__(self):
        """Iterates k over .__getitem__[k]."""
        for k in range(len(self.vector_list)):
            yield self[k]

    def __str__(self):
        """Generates the path string, using the custom np.ndarray.__str__ method."""
        cycle = " -- cycle" if self.cycle else ""
        return f"{str(np.array([v for v in self]))}{cycle}"

    def copy(self):
        return Path(self.vector_list, self.cycle, self.anchor)

    def apply_internally(self, transformation):
        """Applies the transformation to the vectors in .vector_list."""
        self.vector_list = [transformation(v) for v in self.vector_list]
