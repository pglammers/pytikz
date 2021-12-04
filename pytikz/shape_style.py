from abc import ABC
from .abstract import Drawable
from .vector import Transformable, Transformation
from .shape import Shape, ClosedShape, path_string
from plum import dispatch


class ShapeStyleFuture(ABC):
    pass


class StyledShape(Drawable, Transformable):
    """A StyledShape instance combines Shape and ShapeStyle data and can be drawn directly onto the canvas."""

    @dispatch
    def __init__(self, shape: Shape, shape_style: ShapeStyleFuture):
        self.shape = shape
        self.shape_style = shape_style

    @dispatch
    def copy(self) -> "StyledShape":
        return StyledShape(self.shape.copy(), self.shape_style)

    @dispatch
    def apply(self, transformation: Transformation) -> None:
        self.shape.apply(transformation)


@dispatch
def object_string(object: StyledShape):
    return object.shape_style.draw(object.shape)


class ShapeStyle(ShapeStyleFuture):
    """Fundamental ShapeStyle class which features the draw method for drawing a Shape.

    Attributes:
        line (bool): If the Shape should be drawn as a line.
        line_width (None or LineWidth): The width of the previous line.
        line_join (None or LineJoin): The way the corners of the previous line should be styled.
        fill (bool): If the Shape should be filled with a color.
        fill_color (None or str): The string representation of the fill color.

    """

    line = True
    line_color = None
    line_width = None
    line_join = None

    fill = False
    fill_color = None

    @dispatch
    def __call__(self, shape: Shape) -> StyledShape:
        return StyledShape(shape, self)

    @dispatch
    def draw(self, shape: Shape) -> str:
        """Turns the provided shape into a pgf/tikz string given the configuration in self.

        Raises:
            AssertionError: Whenever the fill attribute is true, but the Shape not a ClosedShape.

        """
        if self.fill:
            assert isinstance(shape, ClosedShape), f"Shape {shape} is not a ClosedShape"

        if not self.line:
            if self.fill:
                return f"\\fill[{self.fill_color}] {path_string(shape)};"
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

            return f"\\draw{options} {path_string(shape)};"
