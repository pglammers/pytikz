import pytikz as pt
import pytest


def test_view():
    a, b = pt.Vector(1, 1), pt.Vector(2, 2)
    p1 = pt.Path([a, b])
    p2 = pt.Path([a, b])
    d = pt.ShapeStyle()
    o1 = d(p1)
    o2 = d(p2)
    v = pt.View(pt.vector.Transformation(lambda x: x + a))
    v.append(o1)
    v.append(o2)
    assert str(v[0]) == "\\draw (2, 2) -- (3, 3);"
    v.apply(pt.vector.Transformation(lambda x: 2 * x))
    assert str(v[0]) == "\\draw (4, 4) -- (6, 6);"
