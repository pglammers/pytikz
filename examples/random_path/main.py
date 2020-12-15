import os
import numpy as np

from pytikz import LatexFigure, Vector, Path, Drawer, Drawable, LineJoin


if __name__ == "__main__":
    fig = LatexFigure("figure", os.path.dirname(__file__))

    data = 5 * np.random.rand(20, 2)
    vectors = [Vector(*a) for a in data]
    path = Path(vectors)

    line = Drawer()
    line.line_join = LineJoin.ROUND

    d = Drawable(line, path)

    fig.draw(d)
    fig.build()
