from .constants import LINE_WIDTHS, DEFAULT_FILL_COLOR


def path_from_vertex_list(vertex_list):
    if type(vertex_list) == list:
        vertex_string_list = ['({x},{y})--'.format(x=v[0], y=v[1]) for v in vertex_list]
    else:
        raise ValueError('vertex_list is not a list')
    path_string = ''.join(vertex_string_list)
    return path_string[:-2]


class DrawablePath:
    def __init__(self, vertex_list, cycle=False):
        self.vertex_list = vertex_list
        self.cycle = cycle

        self.path_draw = True
        self.path_color = 'black'
        self.path_width = 'thin'

        self.fill = False
        self.fill_color = DEFAULT_FILL_COLOR

    def draw(self):
        path = path_from_vertex_list(self.vertex_list)
        if self.cycle:
            path += '--cycle'

        options = []
        if self.path_draw:
            options.append('draw={path_color}'.format(path_color=self.path_color))
            if self.path_width != 'thin':
                if self.path_width in LINE_WIDTHS:
                    options.append(self.path_width)
                else:
                    options.append('line width={width}'.format(width=self.path_width))
        if self.fill:
            options.append('fill={color}'.format(color=self.fill_color))

        if len(options) > 0:
            return '\\path[{options}]{path};'.format(options=','.join(options), path=path)
        return ''
