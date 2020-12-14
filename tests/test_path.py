import pytest

from pytikz import Vector, Path
import numpy as np


def test_path():
    a = Vector(1, 2)
    b = Vector(3, 5)
    c = Vector(9, 4)

    # Test string representation
    p1 = Path([a, b, c])
    assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"

    # Test immutability under operators
    assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"

    # Test addition
    p2 = p1.copy().apply(lambda v: v + a)
    assert str(p2) == "(2, 4) -- (4, 7) -- (10, 6)"

    # Test multiplication
    p2 = p1.copy().apply(lambda v: 2 * v)
    assert str(p2) == "(2, 4) -- (6, 10) -- (18, 8)"

    # Test anchor presence
    p1.anchor = Vector(1, 1)
    p2 = p1.copy().apply(lambda v: v + a)
    assert str(p2) == "(3, 5) -- (5, 8) -- (11, 7)"
    p2 = p1.copy().apply(lambda v: 2 * v)
    assert str(p2) == "(3, 4) -- (5, 7) -- (11, 6)"
