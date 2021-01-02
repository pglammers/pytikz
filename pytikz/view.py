from .abstract import AbstractList
from .drawable import Drawable


class View(AbstractList):
    """Bundles a list of drawables with a common transformation."""

    _type = Drawable

    def __init__(self, transformation=lambda vector: vector):
        self._list = []
        self.transformation = transformation

    def _view(self, item):
        return item.copy().apply(self.transformation)
