from pprint import pprint


class Vector:
	def __init__(self, *args):
		self._coordinates = list(args)
		self._dim = len(self._coordinates)

	@property
	def x(self):
		return self._coordinates[0]

	@property
	def y(self):
		return self._coordinates[1]

	@property
	def z(self):
		return self._coordinates[2]

	def __str__(self):
		return f"({', '.join(str(c) for c in self._coordinates)})"


class Path:
	cycle = False

	def __init__(self, vector_list):
		self._vector_list = vector_list

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

	def __str__(self):
		path_string = " -- ".join([str(v) for v in self._vector_list])
		if self.cycle:
			path_string += " -- cycle"
		return path_string

	def build_tikz_string(self):
		return f"\\draw{self};"
