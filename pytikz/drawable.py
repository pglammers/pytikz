from abc import ABC, abstractmethod


class AbstractDrawer(ABC):
    @abstractmethod
    def draw(self, shape):
        pass


class Drawable:
    def __init__(self, drawer, shape):
        self.drawer = drawer
        self.shape = shape

    def copy(self):
        return Drawable(self.drawer, self.shape.copy())

    def apply(self, transformation):
        drawable = self.copy()
        drawable.shape.apply(transformation)
        return drawable

    def __str__(self):
        return self.drawer.draw(self.shape)


class Drawer(AbstractDrawer):
    line = True
    line_color = None
    line_width = None
    line_join = None

    fill = False
    fill_color = None

    def draw(self, shape):
        if self.fill:
            assert shape.cycle

        if not self.line:
            if self.fill:
                return f"\\fill[{self.fill_color}] {shape};"
            if not self.fill:
                return ""

        if self.line:

            options = []
            if self.line_color:
                options.append(self.line_color)
            if self.line_width:
                options.append(self.line_width.value)
            if self.line_join:
                options.append(f"line join={self.line_join.value}")
            if self.fill:
                options.append(f"fill={self.fill_color}")
            options = f"[{', '.join(options)}]" if options else ""

            return f"\\draw{options} {shape};"
