import pytest

from pytikz import Vector, Path
import numpy as np


def test_path():
    a = Vector(1, 2)
    b = Vector(3, 5)
    c = Vector(9, 4)

    # Verify direct string representations
    assert str(Path([a, b, c])) == "(1, 2) -- (3, 5) -- (9, 4)"
    assert str(Path([a, b, c], cycle=True)) == "(1, 2) -- (3, 5) -- (9, 4) -- cycle"
    assert str(Path([a, b, c], anchor=a)) == "(2, 4) -- (4, 7) -- (10, 6)"

    # Verify copying and transformation
    p1 = Path([a, b, c])
    p2 = p1.copy().apply(lambda v: v + a)
    assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"
    assert str(p2) == "(2, 4) -- (4, 7) -- (10, 6)"

    # Verify non-copying and transformation with an anchor
    p1 = Path([a, b, c], anchor=Vector(0, 0))
    p2 = p1.apply(lambda v: 2 * (v + Vector(1, 1)))
    assert str(p1) == "(3, 4) -- (5, 7) -- (11, 6)"
    assert str(p2) == "(3, 4) -- (5, 7) -- (11, 6)"

    # Verify rectange
    assert (
        str(Path.rectangle(0, 1, 2, 3))
        == "(0, 2) -- (0, 3) -- (1, 3) -- (1, 2) -- cycle"
    )
