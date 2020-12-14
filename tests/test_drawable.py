import pytest

from pytikz import Vector, Path, Drawable, LineWidth, LineJoin


def test_drawable():
    p = Path([Vector(0), Vector(1)])
    d = Drawable(p)
    assert str(d) == "\\draw (0) -- (1);"
    d.fill = True
    d.fill_color = "blue"
    with pytest.raises(AssertionError):
        str(d)

    p = Path([Vector(0)], cycle=True)
    d = Drawable(p)

    assert str(d) == "\\draw (0) -- cycle;"

    d.fill = True
    d.fill_color = "blue"
    assert str(d) == "\\draw[fill=blue] (0) -- cycle;"

    d.line = False
    assert str(d) == "\\fill[blue] (0) -- cycle;"

    d.line = True
    d.line_color = "blue"
    assert str(d) == "\\draw[blue, fill=blue] (0) -- cycle;"

    d.line_width = LineWidth.ULTRA_THIN
    assert str(d) == "\\draw[blue, ultra thin, fill=blue] (0) -- cycle;"

    d.line_join = LineJoin.MITER
    assert (
        str(d) == "\\draw[blue, ultra thin, line join=miter, fill=blue] (0) -- cycle;"
    )
