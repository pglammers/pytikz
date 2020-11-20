import pytest

from pytikz import Vector
import numpy as np


def test_vector():
	a = Vector(1, 2, 3)
	b = Vector(4, 5, 6)
	c = Vector(5, 7, 9)
	d = Vector(1, 2)
	f = Vector(-1, -2, -3)
	g = Vector(2, 4, 6)
	ar = np.array([
		[1, 0],
		[3, 1],
		[4, 0]
	])

	assert c[2] == 9
	with pytest.raises(IndexError):
		print(d[3])

	e = [v for v in a]
	assert e == [1, 2, 3]

	assert a.x == 1 and a.y == 2 and a.z == 3
	with pytest.raises(IndexError):
		print(d.z)

	assert a.dim == 3 and d.dim == 2

	assert str(a) == "(1, 2, 3)"

	assert a == Vector(1, 2, 3)
	assert a != b

	assert a + b == c

	assert -a == f

	assert c - b == a

	assert 2 * a == g

	assert a @ ar == Vector(19, 2)

	assert a != None and a != 1
