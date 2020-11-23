import numpy


def _tikz_representation(array):
	if array.ndim == 1:
		return f"({', '.join([str(c) for c in array])})"
	elif array.ndim == 2:
		return " -- ".join(str(v) for v in array)
	else:
		raise ValueError(f"Arrays of dimension {array.ndim} have no TikZ representation.") 


numpy.set_string_function(_tikz_representation, False)


def Vector(*args):
	return numpy.array(list(args))
