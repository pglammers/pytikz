import os
import numpy as np

from pytikz.latex_figure import LatexFigure
from pytikz.path import DrawablePath


if __name__ == "__main__":
    fig = LatexFigure('figure', os.path.dirname(__file__))

    vertices = 10 * np.random.rand(10, 2)

    path = DrawablePath(vertices)
    path.line_join = 'round'
    fig.draw(path)

    fig.update(hard=True)
