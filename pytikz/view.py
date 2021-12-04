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
    data = "\n".join(object_string(d) for d in object)
    return data if object.clip is None else object.clip.clip(data)
