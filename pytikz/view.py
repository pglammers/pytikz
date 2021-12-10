from .shape import ClosedPath
from .shape_style import ShapeStyle
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
        *,
        clip: Union[ClosedPath, None] = None,
        background: Union[ShapeStyle, None] = None,
        boundary: Union[ShapeStyle, None] = None,
    ):
        self._list = []
        self.transformation = transformation
        self.clip = clip
        self.background = background
        self.boundary = boundary

    @dispatch
    def _view(
        self, item: Union[Transformable, VectorType]
    ) -> Union[Transformable, VectorType]:
        return self.transformation(item)

    @dispatch
    def copy(self) -> "View":
        view = View(
            self.transformation,
            clip=self.clip,
            background=self.background,
            boundary=self.boundary,
        )
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
    data_clipped = data if object.clip is None else object.clip.clip(data)
    data_clipped = (
        data_clipped
        if object.background is None
        else f"{object_string(object.background(object.clip))}\n{data_clipped}"
    )
    data_clipped = (
        data_clipped
        if object.boundary is None
        else f"{data_clipped}\n{object_string(object.boundary(object.clip))}"
    )
    return data_clipped
