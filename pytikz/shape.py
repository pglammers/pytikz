from abc import ABC
from .abstract import AbstractList
from .vector import Transformable, Transformation, VectorLike, coordinate_string
from plum import dispatch
from numbers import Number


class Shape(ABC):
    """Abstract Shape class for instances that represent a pgf/tikz path."""


class ClosedShape(Shape, ABC):
    """Abstract ClosedShape class for instances that represent a closed pgf/tikz path.

    Such paths can be filled or used to clip other Drawables.

    """

    @dispatch
    def clip(self, text: str) -> str:
        """Wraps the input string in the clipping commands.

        Args:
            text (str): The pgf/tikz string representing the drawables to be clipped.

        Returns:
            str: The input string wrapped in the clipping commands.

        """
        return (
            "\\begin{scope}\n"
            f"\\clip {path_string(self)};\n"
            f"{text}\n"
            "\\end{scope}"
        )


class Path(Shape, Transformable, AbstractList):
    """A Path is an AbstractList of Vectors that evaluate into a path."""

    @dispatch
    def apply(self, transformation: Transformation) -> None:
        self._list = [transformation(v) for v in self._list]

    @dispatch
    def copy(self) -> "Path":
        return type(self)(self._list.copy())


@dispatch
def path_string(path: Path) -> str:
    return " -- ".join(coordinate_string(v) for v in path)


class ClosedPath(Path, ClosedShape):
    """Identical to a Path, except that the last vector is linked to the first vector in the AbstractList."""


@dispatch
def path_string(path: ClosedPath) -> str:
    return path_string.invoke(Path)(path) + " -- cycle"


class Circle(ClosedShape, Transformable):
    """A Circle is a ClosedShape that consists of a Transformable center and a nontransformable radius."""

    @dispatch
    def __init__(self, center: VectorLike, radius: Number):
        self.center = center
        self.radius = radius

    @dispatch
    def apply(self, transformation: Transformation) -> None:
        self.center = transformation(self.center)

    @dispatch
    def copy(self) -> "Circle":
        return Circle(self.center, self.radius)


@dispatch
def path_string(path: Circle) -> str:
    return f"{coordinate_string(path.center)} circle ({path.radius})"


@dispatch
def object_string(path: Path) -> str:
    raise TypeError(f"Variable {path} is a Path, which is not Drawable.")
