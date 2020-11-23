import numpy as np


class Vector:
	def __init__(self, *args):
		self._coordinates = np.array(list(args))

	@classmethod
	def _np(self, np_array):
		vector = self()
		vector._coordinates = np_array
		return vector

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
		return self._coordinates.shape[0]

	def __str__(self):
		return f"({', '.join(str(c) for c in self._coordinates)})"

	def __eq__(self, other):
		if type(other) != Vector: return False
		if self.dim != other.dim: return False
		return np.all(self._coordinates == other._coordinates)

	def __add__(self, other):
		if type(other) != Vector: raise ValueError("Cannot add a Vector to a non-Vector.")
		if self.dim != other.dim: raise ValueError("The dimensions of the two vectors must be the same.")
		return Vector._np(self._coordinates + other._coordinates)

	def __neg__(self):
		return Vector._np(-self._coordinates)

	def __sub__(self, other):
		return self + (-other)

	def __rmul__(self, other):
		return Vector._np(other * self._coordinates)

	def __matmul__(self, other):
		return Vector._np(self._coordinates @ other)
