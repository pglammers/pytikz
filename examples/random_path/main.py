import os
import numpy as np

from pytikz import LatexFigure
from pytikz import DrawablePath


if __name__ == "__main__":
    fig = LatexFigure('figure', os.path.dirname(__file__))

    fig.append_string('\clip (0,0) rectangle (15,15);\n')

    vertices = 15 * np.random.rand(20, 2)
    path = DrawablePath(vertices)
    path.line_join = 'round'
    fig.draw(path)

    fig.build()
