from abc import ABC, abstractmethod
from .vector import Vector


class Shape(ABC):

	cycle = False

	@abstractmethod
	def __str__(self):
		pass

	@abstractmethod
	def _copy(self):
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

	def __init__(self, vector_list, anchor=None, cycle=False):
		self._vector_list = vector_list
		self._anchor = anchor
		self._cycle = cycle

	@classmethod
	def rectangle(self, left, right, lower, upper, anchor=None):
		vector_list = [
			Vector(left, lower),
			Vector(left, upper),
			Vector(right, upper),
			Vector(right, lower)
		]
		return self(vector_list, anchor, True)

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

	@property
	def cycle(self):
		return self._cycle

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

	def _copy(self):
		return Path(self._vector_list, self.anchor, self.cycle)

	def apply(self, callback):
		path = self._copy()
		if path.anchor is None:
			path._vector_list = [callback(v) for v in self]
		else:
			path._anchor = callback(path.anchor)
		return path
