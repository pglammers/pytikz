import pytest

from pytikz import Vector, Path, ClosedPath
from pytikz.shape import Circle
import numpy as np


def test_path():
    a = Vector(1, 2)
    b = Vector(3, 5)
    c = Vector(9, 4)

    # Verify direct string representations
    assert str(Path([a, b, c])) == "(1, 2) -- (3, 5) -- (9, 4)"

    # Verify copying and transformation
    p1 = Path([a, b, c])
    p2 = p1.copy()
    p2.apply(lambda v: v + a)
    assert str(p1) == "(1, 2) -- (3, 5) -- (9, 4)"
    assert str(p2) == "(2, 4) -- (4, 7) -- (10, 6)"

    # Verify rectangle
    # assert str(Rectangle(0, 1, 2, 3)) == "(0, 2) -- (0, 3) -- (1, 3) -- (1, 2) -- cycle"

    assert str(Circle(Vector(0, 0), 1)) == "(0, 0) circle (1)"
    assert (
        Circle(Vector(0, 0), 1).clip("blabla")
        == """\\begin{scope}
\\clip (0, 0) circle (1);
blabla
\\end{scope}"""
    )
