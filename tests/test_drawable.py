import pytest

from pytikz import Vector, Path, ClosedPath, ShapeStyle, LineWidth, LineJoin


def test_drawable():
    p = Path([Vector(0, 3), Vector(1, 2)])
    l = ShapeStyle()
    d = l(p)
    assert str(d) == "\\draw (0, 3) -- (1, 2);"

    l.fill = True
    l.fill_color = "blue"
    with pytest.raises(AssertionError):
        str(d)

    p = ClosedPath([Vector(0, 0), Vector(1, 5)])
    d = l(p)
    assert str(d) == "\\draw[fill=blue] (0, 0) -- (1, 5) -- cycle;"

    l.line = False
    assert str(d) == "\\fill[blue] (0, 0) -- (1, 5) -- cycle;"

    l.line = True
    l.line_color = "blue"
    assert str(d) == "\\draw[blue, fill=blue] (0, 0) -- (1, 5) -- cycle;"

    l.line_width = LineWidth.ULTRA_THIN
    assert str(d) == "\\draw[blue, ultra thin, fill=blue] (0, 0) -- (1, 5) -- cycle;"

    l.line_join = LineJoin.MITER
    assert (
        str(d)
        == "\\draw[blue, ultra thin, line join=miter, fill=blue] (0, 0) -- (1, 5) -- cycle;"
    )
