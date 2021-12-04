import pytest
from pytikz.vector import AnchoredVector, Transformation
from pytikz import Vector, Path, ClosedPath
from pytikz.shape import Circle, path_string


a = Vector(1, 2)
b = Vector(3, 5)
c = AnchoredVector(Vector(1, 1), Vector(2, 3))


vector_list = [a, b, c]


def test_path():
    p = Path(vector_list)

    assert path_string(Path([a, b, c])) == "(1, 2) -- (3, 5) -- (3, 4)"

    p2 = p.copy()
    p2.apply(Transformation(lambda v: 2 * v))

    assert path_string(p) == "(1, 2) -- (3, 5) -- (3, 4)"
    assert path_string(p2) == "(2, 4) -- (6, 10) -- (4, 5)"


def test_closed_path():
    p = ClosedPath(vector_list)
    assert path_string(p) == "(1, 2) -- (3, 5) -- (3, 4) -- cycle"
    assert (
        p.clip("blablabla")
        == """\\begin{scope}
\\clip (1, 2) -- (3, 5) -- (3, 4) -- cycle;
blablabla
\\end{scope}"""
    )


def test_circle():
    c = Circle(Vector(2, 0), 1)
    c.apply(Transformation(lambda v: 2 * v))
    assert path_string(c) == "(4, 0) circle (1)"
