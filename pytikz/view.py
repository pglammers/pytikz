from abc import ABC, abstractmethod
import numpy as np

from .vector import Vector


class Projection(ABC):

    @abstractmethod
    def transformation(self, vector):
        pass


class View:

	def __init__(self, projection):
		assert issubclass(type(projection), Projection)
		self.projection = projection
		self.drawables = []

	def transformation(self, vector):
		return self.projection.transformation(vector)

	def append(self, drawable):
		self.drawables.append(drawable)

	def __iter__(self):
		for drawable in self.drawables:
			yield drawable.apply(self.transformation)


class IdentityProjection(Projection):

	def transformation(self, vector):
		return vector


class ScaleProjection(Projection):

    def __init__(self, units=Vector(1, 1), origin_position=Vector(0, 0)):
        self.units = units
        self.origin_position = origin_position

    def transformation(self, vector):
        return (vector - self.origin_position) @ np.diag(1. / self.units)
