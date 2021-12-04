import os
import numpy as np

from pytikz import *
from pytikz.shape import Shape


if __name__ == "__main__":

    np.random.seed(1)

    fig = Figure("figure", os.path.dirname(__file__))

    data = 5 * np.random.rand(20, 2)
    vectors = [Vector(*a) for a in data]
    path = Path(vectors)

    line = ShapeStyle()
    line.line_join = LineJoin.ROUND

    d = line(path)

    blue = ShapeStyle()
    blue.line = False
    blue.fill = True
    blue.fill_color = "blue!50"

    boundary = ShapeStyle()

    v = View(
        clip=Circle(Vector(5 / 2, 5 / 2), 5 / 2),
        background=blue,
        boundary=boundary,
    )
    v.append(d)

    fig.draw(v)
    fig.write_all(True)
    fig.process()
