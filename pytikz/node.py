from .abstract import Drawable
from .vector import Transformable


class Node(Drawable, Transformable):
    def __init__(self, position, text):
        self.position = position
        self.text = text

    def __str__(self):
        return f"\\node at {str(self.position)} {{{self.text}}};"

    def apply(self, transformation):
        self.position = transformation(self.position)

    def copy(self):
        return Node(self.position, self.text)
