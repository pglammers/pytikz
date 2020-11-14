class Rectangle:
    fill = None

    def __init__(self, vector_1, vector_2):
        self.x0 = min(vector_1[0], vector_2[0])
        self.x1 = max(vector_1[0], vector_2[0])
        self.y0 = min(vector_1[1], vector_2[1])
        self.y1 = max(vector_1[1], vector_2[1])

    def build_tikz_string(self):
        x0, x1, y0, y1 = self.x0, self.x1, self.y0, self.y1
        f = self.fill
        if not f:
            return f"\\draw ({x0}, {y0}) rectangle ({x1}, {y1});"
        else:
            return f"\\filldraw[color=black, fill={f}] ({x0}, {y0}) rectangle ({x1}, {y1});"
