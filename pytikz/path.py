from abc import ABC, abstractmethod
from .vector import Vector


class Shape(ABC):

	@abstractmethod
	def __str__(self):
		pass

	@abstractmethod
	def copy(self):
		pass

	@abstractmethod
	def apply(self, callback):
		pass

	def __add__(self, other):
		return self.apply(lambda v: v + other)

	def __neg__(self):
		return self.apply(lambda v: -v)

	def __sub__(self, other):
		return self + (-other)

	def __rmul__(self, other):
		return self.apply(lambda v: other * v)

	def __matmul__(self, other):
		return self.apply(lambda v: v @ other)


class Path(Shape):

	cycle = False

	def __init__(self, vector_list, anchor=None):
		self._vector_list = vector_list
		self._anchor = anchor

	@classmethod
	def rectangle(self, left, right, lower, upper):
		vector_list = [
			Vector(left, lower),
			Vector(left, upper),
			Vector(right, upper),
			Vector(right, lower)
		]
		path = self(vector_list)
		path.cycle = True
		return path

	def __getitem__(self, arg):
		if self.anchor is None:
			return self._vector_list[arg]
		else:
			return self.anchor + self._vector_list[arg]

	def __iter__(self):
		for k in range(len(self._vector_list)):
			yield self[k]

	@property
	def anchor(self):
		return self._anchor

	def __str__(self):
		path_string = " -- ".join([str(v) for v in self])
		if self.cycle:
			path_string += " -- cycle"
		return path_string

	def __eq__(self, other):
		if type(other) != Path: return False
		return self._vector_list == other._vector_list \
			and self.anchor == other.anchor \
			and self.cycle == other.cycle

	def copy(self):
		path = Path(self._vector_list, self.anchor)
		path.cycle = self.cycle
		return path

	def apply(self, callback):
		path = self.copy()
		if path.anchor is None:
			path._vector_list = [callback(v) for v in self]
		else:
			path._anchor = callback(path.anchor)
		return path
