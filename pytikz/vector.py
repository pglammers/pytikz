import numpy as np


class Vector:
	def __init__(self, *args):
		self._coordinates = list(args)
		self._dim = len(self._coordinates)

	def __getitem__(self, arg):
		return self._coordinates[arg]

	def __iter__(self):
		for c in self._coordinates:
			yield c

	@property
	def x(self):
		return self._coordinates[0]

	@property
	def y(self):
		return self._coordinates[1]

	@property
	def z(self):
		return self._coordinates[2]

	@property
	def dim(self):
		return self._dim

	def __str__(self):
		return f"({', '.join(str(c) for c in self._coordinates)})"

	def __eq__(self, other):
		return self.dim == other.dim and self._coordinates == other._coordinates

	def __add__(self, other):
		assert self.dim == other.dim
		return Vector(*[a + b for a, b in zip(self, other)])

	def __neg__(self):
		return Vector(*[-a for a in self])

	def __sub__(self, other):
		return self + (-other)

	def __rmul__(self, other):
		return Vector(*[other * a for a in self])

	def __matmul__(self, other):
		return Vector(*(np.array([a for a in self]) @ other))
