import pytest

from pytikz import Vector, Path
import numpy as np


def test_path():
	a = Vector(1, 2)
	b = Vector(3, 5)
	c = Vector(9, 4)

	p1 = Path([a,b,c])

	assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"

	p2 = p1 + a

	assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"
	assert str(p2) == "(1, 4) -- (4, 7) -- (10, 6)"

	
