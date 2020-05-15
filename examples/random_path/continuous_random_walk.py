import os
import numpy as np

from pytikz.latex_figure import LatexFigure
from pytikz.path import DrawablePath


if __name__ == "__main__":
    fig = LatexFigure('figure', os.path.dirname(__file__))

    figure_width = 40

    n_steps = 3000
    vertices = np.vstack(
        (np.zeros(n_steps), np.arange(n_steps) / n_steps * figure_width)
    ).T
    a = 0
    for i in range(n_steps):
        a += np.random.randn() / np.sqrt(n_steps)
        vertices[i, 0] = a
    print(vertices)
    # vertices /= np.sqrt(n_steps)
    # vertices = 10 * np.random.rand(10, 2)

    # fig.append_string('\clip (0,0) rectangle (15,15);\n')

    path = DrawablePath(vertices)
    path.line_join = 'round'
    fig.draw(path)

    fig.update(hard=True)
