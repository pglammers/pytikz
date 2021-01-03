from .abstract import AbstractDrawable, AbstractObject


class Node(AbstractObject, AbstractDrawable):
    def __init__(self, position, text, anchor=None):
        self._position = position
        self.text = text
        self.anchor = anchor

    @property
    def position(self):
        return self._view(self._position)

    def __str__(self):
        return f"\\node at {str(self.position)} {{{self.text}}};"

    def apply_internally(self, transformation):
        self._position = transformation(self._position)

    def copy(self):
        return Node(self, self._position, self.text, self.anchor)
