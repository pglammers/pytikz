from abc import ABC, abstractmethod
import numpy as np
from .vector import Vector


class Shape(ABC):

    cycle = False
    anchor = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def apply_internally(self, calback):
        pass

    def apply(self, callback):
        if self.anchor is None:
            self.apply_internally(callback)
        else:
            self.anchor = callback(self.anchor)
        return self


class Path(Shape):
    def __init__(self, vector_list, cycle=False, anchor=None):
        self.vector_list = vector_list
        self.cycle = cycle
        self.anchor = anchor

    @classmethod
    def rectangle(self, left, right, lower, upper, anchor=None):
        vector_list = [
            Vector(left, lower),
            Vector(left, upper),
            Vector(right, upper),
            Vector(right, lower),
        ]
        return self(vector_list, True, anchor)

    def __getitem__(self, arg):
        if self.anchor is None:
            return self.vector_list[arg]
        else:
            return self.anchor + self.vector_list[arg]

    def __iter__(self):
        for k in range(len(self.vector_list)):
            yield self[k]

    def __str__(self):
        cycle = " -- cycle" if self.cycle else ""
        return f"{str(np.array([v for v in self]))}{cycle}"

    def copy(self):
        return Path(self.vector_list, self.cycle, self.anchor)

    def apply_internally(self, callback):
        self.vector_list = [callback(v) for v in self.vector_list]
