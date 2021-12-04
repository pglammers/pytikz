import pytest
from pytikz import (
    Vector,
    Path,
    ClosedPath,
    ShapeStyle,
    LineWidth,
    LineJoin,
    object_string,
)


def test_shape_style():
    p = Path([Vector(0, 3), Vector(1, 2)])
    l = ShapeStyle()
    d = l(p)
    assert object_string(d) == "\\draw (0, 3) -- (1, 2);"

    l.fill = True
    l.fill_color = "blue"
    with pytest.raises(AssertionError):
        object_string(d)

    p = ClosedPath([Vector(0, 0), Vector(1, 5)])
    d = l(p)
    assert object_string(d) == "\\draw[fill=blue] (0, 0) -- (1, 5) -- cycle;"

    l.line = False
    assert object_string(d) == "\\fill[blue] (0, 0) -- (1, 5) -- cycle;"

    l.line = True
    l.line_color = "blue"
    assert object_string(d) == "\\draw[blue, fill=blue] (0, 0) -- (1, 5) -- cycle;"

    l.line_width = LineWidth.ULTRA_THIN
    assert (
        object_string(d)
        == "\\draw[blue, ultra thin, fill=blue] (0, 0) -- (1, 5) -- cycle;"
    )

    l.line_join = LineJoin.MITER
    assert (
        object_string(d)
        == "\\draw[blue, ultra thin, line join=miter, fill=blue] (0, 0) -- (1, 5) -- cycle;"
    )
