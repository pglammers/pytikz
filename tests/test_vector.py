import pytest

from pytikz import Vector

import numpy


def test_vector():

	# Test if Vectors are cast to the correct shape under all circumstances
	assert Vector(    ).shape == (0, )
	assert Vector(0   ).shape == (1, )
	assert Vector(0, 0).shape == (2, )

	# Test the string representation of a vector
	assert str(Vector(1, 2, 3)) == "(1, 2, 3)"

	# Test the behaviour of Vectors under linear transformations
	transformation = numpy.array([
		[1, 0],
		[3, 1],
		[4, 0]
	])
	assert numpy.all(Vector(1, 2, 3) @ transformation == Vector(19, 2))

	# Test the string representation of a matrix
	assert str(numpy.ones((2, 2), dtype=numpy.int8)) == "(1, 1) -- (1, 1)"
