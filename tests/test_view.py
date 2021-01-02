import pytikz as pt
import pytest


def test_view():
    a, b = pt.Vector(1), pt.Vector(2)
    p1 = pt.Path([a, b])
    p2 = pt.Path([a, b], anchor=a)
    d = pt.ShapeStyle()
    o1 = pt.DrawableShape(p1, d)
    o2 = pt.DrawableShape(p2, d)
    v = pt.View()
    v.append(o1)
    v.append(o2)
    assert str(v[0]) == str(o1) == "\\draw (1) -- (2);"
    assert str(v[1]) == str(o2) == "\\draw (2) -- (3);"
