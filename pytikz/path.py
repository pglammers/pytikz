import numpy as np

from .constants import LINE_WIDTHS, LINE_JOINS, DEFAULT_FILL_COLOR
import numpy as np

def path_from_vertices(vertices: np.array) -> str:
    vertices_string_list = ['({x},{y})--'.format(x=v[0], y=v[1]) for v in vertices]
    path_string = ''.join(vertices_string_list)
    return path_string[:-2]


class DrawablePath:
    def __init__(self, vertices: np.array, cycle: bool = False):
        self.vertices = vertices
        self.cycle = cycle

        self.line = True
        self.line_color = None
        self.line_width = None
        self.line_join = None

        self.fill = False
        self.fill_color = DEFAULT_FILL_COLOR

    def build_tikz_string(self) -> str:
        path = path_from_vertices(self.vertices)
        if self.cycle:
            path += '--cycle'

        options = []

        if self.line:
            if self.line_color is None:
                options.append('draw')
            else:
                options.append('draw={color}'.format(color=self.line_color))
            if self.line_width is not None:
                if self.line_width in LINE_WIDTHS:
                    options.append(self.line_width)
                else:
                    options.append('line width={width}'.format(width=self.line_width))
            if self.line_join is not None:
                options.append('line join={option}'.format(option=self.line_join))

        if self.fill:
            options.append('fill={color}'.format(color=self.fill_color))

        if len(options) > 0:
            return '\\path[{options}]{path};'.format(options=','.join(options), path=path)
        return ''
