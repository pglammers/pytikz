class Drawable:
	line = True
	line_color = None
	line_width = None
	line_join = None

	fill = False
	fill_color = None

	def __init__(self, shape):
		self.shape = shape

	def __str__(self):
		if self.fill: assert self.shape.cycle

		if not self.line:
			if self.fill: return f"\\fill[{self.fill_color}] {self.shape};"
			if not self.fill: return ""

		if self.line:

			options = []
			if self.line_color: options.append(self.line_color)
			if self.line_width: options.append(self.line_width.value)
			if self.line_join: options.append(f"line join={self.line_join.value}")
			if self.fill: options.append(f"fill={self.fill_color}")
			options = f"[{', '.join(options)}]" if options else ""

			return f"\\draw{options} {self.shape};"

	def apply(self, callable):
		self.shape.apply(callable)
		return self
