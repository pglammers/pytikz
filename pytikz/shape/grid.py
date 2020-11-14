

class Grid:
    xlabels = None
    ylabels = None

    def __init__(self, limits_start, limits_stop):
        self.x0, self.y0 = limits_start[0], limits_start[1]
        self.x1, self.y1 = limits_stop[0], limits_stop[1]

    def build_tikz_string(self):
        x0, x1, y0, y1 = self.x0, self.x1, self.y0, self.y1
        output = f"\draw[step = 1.0, black, thin] ({x0}, {y0}) grid ({x1}, {y1});\n"
        if self.xlabels:
            for key, value in self.xlabels.items():
                output += f"\\node[below] at ({key},{y0}) {{{value}}};\n"
        if self.ylabels:
            for key, value in self.ylabels.items():
                output += f"\\node[left] at ({x0},{key}) {{{value}}};\n"
        return output
