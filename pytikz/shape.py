from abc import ABC, abstractmethod
from .abstract import Drawable, AbstractList
from .vector import Transformable


class Shape(ABC):
    """Abstract Shape class for instances that represent a pgf/tikz path."""

    @abstractmethod
    def __str__(self):
        """Must return the representation of the Shape as a pgf/tikz string."""
        pass


class ClosedShape(Shape, ABC):
    """Abstract ClosedShape class for instances that represent a closed pgf/tikz path.

    Such paths can be filled or used to clip other Drawables.

    """

    def clip(self, text):
        """Wraps the input string in the clipping commands.

        Args:
            text (str): The pgf/tikz string representing the drawables to be clipped.

        Returns:
            str: The input string wrapped in the clipping commands.

        """
        return "\\begin{scope}\n" f"\\clip {self};\n" f"{text}\n" "\\end{scope}"


class StyledShape(Drawable, Transformable):
    """A StyledShape instance combines Shape and ShapeStyle data and can be drawn directly onto the canvas.

    Args:
        shape (Shape): The Shape to be drawn.
        shape_style (ShapeStyle): The ShapeStyle containing the .draw method for drawing the Shape.

    Attributes:
        shape (Shape): The Shape to be drawn.
        shape_style (ShapeStyle): The ShapeStyle containing the .draw method for drawing the Shape.

    """

    def __init__(self, shape, shape_style):
        self.shape = shape
        self.shape_style = shape_style

    def __str__(self):
        """Implements the __str__ method from Drawable.

        Returns:
            str: The shape_style pgf/tikz string representation of the shape.

        """
        return self.shape_style.draw(self.shape)

    def copy(self):
        """Implements the copy method from Shiftable.

        Returns:
            StyledShape: A copy of the StyledShape.

        """
        return StyledShape(self.shape.copy(), self.shape_style)

    def apply(self, transformation):
        """Implements the apply method from Shiftable.

        Applies the transformation to the shape.

        Args:
            transformation (Transformation or function): The transformation to be applied.

        """
        self.shape.apply(transformation)


class ShapeStyle:
    line = True
    line_color = None
    line_width = None
    line_join = None

    fill = False
    fill_color = None

    def __call__(self, shape):
        return StyledShape(shape, self)

    def draw(self, shape):
        if self.fill:
            assert isinstance(shape, ClosedShape)

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


class Path(Shape, Transformable, AbstractList):
    def __str__(self):
        return " -- ".join(str(v) for v in self)

    def apply(self, transformation):
        self._list = [transformation(v) for v in self._list]

    def copy(self):
        return Path(self._list.copy())


class ClosedPath(Path, ClosedShape):
    def __str__(self):
        return super().__str__() + " -- cycle"

    def copy(self):
        return ClosedPath(self._list.copy())


class Circle(ClosedShape, Transformable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"{self.center} circle ({self.radius})"

    def apply(self, transformation):
        self.center = transformation(self.center)

    def copy(self):
        return Circle(self.center, self.radius)
