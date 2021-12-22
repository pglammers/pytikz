from .abstract import Drawable
from .vector import VectorLike, Transformable, Transformation, coordinate_string
from .constants import Orientation
from typing import Union
from plum import dispatch


class Node(Drawable, Transformable):
    @dispatch
    def __init__(
        self,
        position: VectorLike,
        text: str,
        orientation: Union[None, Orientation] = None,
    ):
        self.position = position
        self.text = text
        self.orientation = orientation

    @dispatch
    def copy(self) -> "Node":
        return Node(self.position, self.text, self.orientation)

    @dispatch
    def apply(self, transformation: Transformation) -> None:
        self.position = transformation(self.position)


@dispatch
def object_string(object: Node) -> str:
    options = f"[anchor={object.orientation.value}]" if object.orientation else ""
    return f"\\node{options} at {coordinate_string(object.position)} {{{object.text}}};"
