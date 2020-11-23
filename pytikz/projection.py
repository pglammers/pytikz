from abc import ABC, abstractmethod
import numpy as np

from .vector import Vector


class Projection(ABC):

    @abstractmethod
    def transformation(self, vector):
        pass


class ScaleProjection(Projection):

    def __init__(self, units=Vector(1, 1), origin_position=Vector(0, 0)):
        self.units = units
        self.origin_position = origin_position

    def transformation(self, vector):
        return (vector - self.origin_position) @ np.diag(1. / self.units) 
