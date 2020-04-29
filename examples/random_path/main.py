import os
import numpy as np

from pytikz.latex_figure import LatexFigure
from pytikz.path import DrawablePath


if __name__ == "__main__":
    fig = LatexFigure('figure', os.path.dirname(__file__))

    fig.append_string('\clip (0,0) rectangle (15,15);')

    vertices = 15 * np.random.rand(20, 2)
    path = DrawablePath(vertices)
    path.line_join = 'round'
    fig.draw(path)

    fig.update()
