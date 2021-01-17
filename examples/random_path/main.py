import os
import numpy as np

from pytikz import *


if __name__ == "__main__":

    np.random.seed(1)

    fig = Figure("figure", os.path.dirname(__file__))

    data = 5 * np.random.rand(20, 2)
    vectors = [Vector(*a) for a in data]
    path = Path(vectors)

    line = ShapeStyle()
    line.line_join = LineJoin.ROUND

    d = line(path)

    fig.draw(d)
    fig.write_all(True)
    fig.process()
