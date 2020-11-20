from pprint import pprint
from .constants import *
from .vector import Vector


class Path:
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

	def __str__(self):
		path_string = " -- ".join([str(v) for v in self._vector_list])
		if self.cycle:
			path_string += " -- cycle"
		return path_string


class Drawable:
	line = True
	line_color = None
	line_width = None
	line_join = None

	fill = False
	fill_color = None

	def __init__(self, path):
		self.path = path

	def __str__(self):
		if self.fill: assert self.path.cycle

		if not self.line:
			if self.fill: return f"\\fill[{self.fill_color}] {self.path};"
			if not self.fill: return ""

		if self.line:

			options = []
			if self.line_color: options.append(self.line_color)
			if self.line_width: options.append(self.line_width.value)
			if self.line_join: options.append(f"line join={self.line_join.value}")
			if self.fill: options.append(f"fill={self.fill_color}")
			options = f"[{', '.join(options)}]" if options else ""

			return f"\\draw{options} {self.path};"
