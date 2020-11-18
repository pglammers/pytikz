from pprint import pprint
from .constants import *


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


class DrawablePath(Path):
	line = True
	line_color = None
	line_width = None
	line_join = None

	fill = False
	fill_color = None

	def __str__(self):
		if self.fill: assert self.cycle

		path = super().__str__()

		if not self.line:
			if self.fill: return f"\\fill[{self.fill_color}] {path};"
			if not self.fill: return ""

		if self.line:

			options = []
			if self.line_color: options.append(self.line_color)
			if self.line_width: options.append(self.line_width.value)
			if self.line_join: options.append(f"line join={self.line_join.value}")
			if self.fill: options.append(f"fill={self.fill_color}")
			options = f"[{', '.join(options)}]" if options else ""

			return f"\\draw{options} {path};"
