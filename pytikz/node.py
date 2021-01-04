from .abstract import Drawable
from .vector import Vector, Transformable


class Node(Drawable, Transformable):
    def __init__(self, position, text):
        self._position = position
        self.text = text

    @property
    def position(self):
        return Vector(self._position)

    def __str__(self):
        return f"\\node at {str(self.position)} {{{self.text}}};"

    def apply(self, transformation):
        self._position = transformation(self._position)

    def copy(self):
        return Node(self._position, self.text)
