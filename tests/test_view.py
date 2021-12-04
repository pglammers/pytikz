import pytikz as pt
import pytest
from pytikz.shape_style import ShapeStyle


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
    assert pt.object_string(v) == "\\draw (2, 2) -- (3, 3);\n\\draw (2, 2) -- (3, 3);"
    v.apply(pt.vector.Transformation(lambda x: 2 * x))
    assert pt.object_string(v) == "\\draw (4, 4) -- (6, 6);\n\\draw (4, 4) -- (6, 6);"

    v.clip = pt.ClosedPath([a, b])

    assert (
        pt.object_string(v)
        == """\\begin{scope}
\\clip (1, 1) -- (2, 2) -- cycle;
\\draw (4, 4) -- (6, 6);
\\draw (4, 4) -- (6, 6);
\\end{scope}"""
    )

    v.boundary = ShapeStyle()

    assert (
        pt.object_string(v)
        == """\\begin{scope}
\\clip (1, 1) -- (2, 2) -- cycle;
\\draw (4, 4) -- (6, 6);
\\draw (4, 4) -- (6, 6);
\\end{scope}
\\draw (1, 1) -- (2, 2) -- cycle;"""
    )

    s = ShapeStyle()
    s.line=False
    s.fill=True
    s.fill_color="blue"

    v.background = s

    assert pt.object_string(v) =="""\\fill[blue] (1, 1) -- (2, 2) -- cycle;
\\begin{scope}
\\clip (1, 1) -- (2, 2) -- cycle;
\\draw (4, 4) -- (6, 6);
\\draw (4, 4) -- (6, 6);
\\end{scope}
\\draw (1, 1) -- (2, 2) -- cycle;"""
