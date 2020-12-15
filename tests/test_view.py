import pytikz as pt
import pytest


def test_view():
    a, b = pt.Vector(1), pt.Vector(2)
    p1 = pt.Path([a, b])
    p2 = pt.Path([a, b], anchor=a)
    d = pt.Drawer()
    o1 = pt.Drawable(d, p1)
    o2 = pt.Drawable(d, p2)
    v = pt.View()
    v.append(o1)
    v.append(o2)
    assert str(v[0]) == str(o1) == "\\draw (1) -- (2);"
    assert str(v[1]) == str(o2) == "\\draw (2) -- (3);"

    v.compose(lambda x: -x)
    assert str(v[0]) == "\\draw (-1) -- (-2);"
    assert str(v[1]) == "\\draw (0) -- (1);"

    v.compose(lambda x: x + 1)
    assert str(v[0]) == "\\draw (0) -- (-1);"
    assert str(v[1]) == "\\draw (1) -- (2);"
