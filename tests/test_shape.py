import pytest
from pytikz.vector import Transformation
from pytikz import Vector, Path, ClosedPath
from pytikz.shape import Circle, path_string
import numpy as np


def test_path():
    a = Vector(1, 2)
    b = Vector(3, 5)
    c = Vector(9, 4)

    # Verify direct string representations
    assert path_string(Path([a, b, c])) == "(1, 2) -- (3, 5) -- (9, 4)"

    # Verify copying and transformation
    p1 = Path([a, b, c])
    p2 = p1.copy()
    p2.apply(Transformation(lambda v: v + a))
    assert path_string(p1) == "(1, 2) -- (3, 5) -- (9, 4)"
    assert path_string(p2) == "(2, 4) -- (4, 7) -- (10, 6)"

    # Verify ClosedPath
    p3 = ClosedPath([a, b, c])
    assert path_string(p3) == "(1, 2) -- (3, 5) -- (9, 4) -- cycle"

    # Verify Circle
    assert path_string(Circle(Vector(0, 0), 1)) == "(0, 0) circle (1)"
    assert (
        Circle(Vector(0, 0), 1).clip("blabla")
        == """\\begin{scope}
\\clip (0, 0) circle (1);
blabla
\\end{scope}"""
    )
