from .abstract import Drawable, AbstractList


class View(Drawable, AbstractList):
    """Bundles a list of drawables with a common transformation."""

    def __init__(self, transformation=lambda v: v, clip=None):
        self._list = []
        self.transformation = transformation
        self.clip = clip

    def _view(self, item):
        return self.transformation(item)

    def __str__(self):
        data = "\n".join(str(d) for d in self)
        return data if self.clip is None else self.clip.clip(data)
