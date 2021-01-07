from .abstract import Drawable
from .vector import Transformable


class Node(Drawable, Transformable):
    def __init__(self, position, text, orientation=None):
        self.position = position
        self.text = text
        self.orientation = orientation

    def __str__(self):
        options = f"[anchor={self.orientation.value}]" if self.orientation else ""
        return f"\\node{options} at {self.position} {{{self.text}}};"

    def apply(self, transformation):
        self.position = transformation(self.position)

    def copy(self):
        return Node(self.position, self.text, self.orientation)
