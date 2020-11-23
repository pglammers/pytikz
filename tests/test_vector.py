import pytest

from pytikz import Vector
import numpy as np


def test_vector():
	a = Vector(1, 2, 3)
	ar = np.array([
		[1, 0],
		[3, 1],
		[4, 0]
	])
	assert str(Vector(1, 2, 3)) == "(1, 2, 3)"
	assert np.all(a @ ar == Vector(19, 2))
