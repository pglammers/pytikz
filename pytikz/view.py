from pytikz.shape import ClosedPath
from .abstract import Drawable, AbstractList
from .vector import Transformable, Transformation, VectorType
from plum import dispatch
from typing import Union


class View(Drawable, Transformable, AbstractList):
    """Matches a list of Drawables with a common transformation.

    Drawables are transformed through this transformation upon access.

    """

    @dispatch
    def __init__(
        self,
        transformation: Transformation = Transformation(lambda x: x),
        clip: Union[ClosedPath, None] = None,
    ):
        self._list = []
        self.transformation = transformation
        self.clip = clip

    @dispatch
    def _view(
        self, item: Union[Transformable, VectorType]
    ) -> Union[Transformable, VectorType]:
        return self.transformation(item)

    @dispatch
    def __str__(self) -> str:
        """Implements the __str__ method from Drawable.

        Returns a string with the transformed Drawables concatenated, and clipped whenever a ClosedShape is provided.

        Returns:
            str: The string pgf/tikz string representation of the view.

        """
        data = "\n".join(str(d) for d in self)
        return data if self.clip is None else self.clip.clip(data)

    @dispatch
    def copy(self) -> "View":
        view = View(self.transformation, self.clip)
        view._list = self._list.copy()
        return view

    @dispatch
    def apply(self, transformation: Transformation) -> None:
        self.transformation = transformation * self.transformation
        if self.clip is not None:
            self.clip = transformation(self.clip)


@dispatch
def object_string(object: View):
    data = "\n".join(str(d) for d in object)
    return data if object.clip is None else object.clip.clip(data)
