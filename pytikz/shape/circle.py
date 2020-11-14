

class Circle:
    fill = None

    def __init__(self, coordinates, radius):
        self.coordinates = coordinates
        self.radius = radius

    def build_tikz_string(self):
        x, y, r = self.coordinates[0], self.coordinates[1], self.radius
        f = self.fill
        if not f:
            return f"\\draw ({x}, {y}) circle ({r});"
        else:
            return f"\\filldraw[color=black, fill={f}] ({x}, {y}) circle ({r});"
