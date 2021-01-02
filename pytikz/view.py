from .abstract import AbstractList, AbstractDrawable


class View(AbstractList):
    """Bundles a list of drawables with a common transformation."""

    _type = AbstractDrawable

    def __init__(self, transformation=lambda vector: vector):
        self._list = []
        self.transformation = transformation

    def _view(self, item):
        return item.copy().apply(self.transformation)
