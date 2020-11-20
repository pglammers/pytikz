import pytest

from pytikz import Vector, Path
import numpy as np


def test_path():
	a = Vector(1, 2)
	b = Vector(3, 5)
	c = Vector(9, 4)

	p1 = Path([a,b,c])
	assert p1.anchor == None
	assert p1[0] == a and p1[1] == b
	with pytest.raises(IndexError):
		p1[3]
	assert [x for x in p1] == [a,b,c]
	assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"
	assert p1 == Path([a,b,c])

	p2 = Path([a,b,c], a)
	assert p2[0] == 2*a and p2[1] == b+a and p2[2] == c+a and p2.anchor == a
	assert [v for v in p2] == [a+a, b+a, c+a]
	assert str(p2) == "(2, 4) -- (4, 7) -- (10, 6)"

	p1 = Path([a,b,c], cycle=True)
	assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4) -- cycle"

	assert p1 != p2

	assert p1._copy() == p1
	p1_mod = p1._copy()
	p1_mod._cycle = False
	assert p1_mod != p1

	p1 = Path([a,b,c])
	p2 = Path([a+a,b+a,c+a])
	assert p1 + a == p2

	p1 = Path([a,b,c],a)
	p2 = Path([a,b,c],a+a)
	assert p1+a==p2
	assert 2 * p1 == p2
	assert (-p1) + 2*a == p1
	assert p2 - a == p1

	ar = np.array([
		[10, 10],
		[10, 10]
	])

	p3 = Path([a,b,c], a @ ar)
	assert Path([a,b,c],a) @ ar == p3
	assert Path([a,b,c])@ ar == Path([a@ar, b@ar, c@ar])

	rect = Path.rectangle(0,1,2,3)
	assert rect == Path([
		Vector(0,2),
		Vector(0,3),
		Vector(1,3),
		Vector(1,2)
	], cycle=True)
