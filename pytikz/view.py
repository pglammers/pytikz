from .abstract import Drawable, AbstractList
from .vector import Transformable, compose


class View(Drawable, Transformable, AbstractList):
    """Matches a list of Drawables with a common transformation.

    Drawables are transformed through this transformation upon access.

    Args:
        transformation (function): The transformation applied when viewing each Drawable.
        clip (None or ClosedShape): The region to clip when producing a pgf/tikz string of the entire View.

    Attributes:
        _list (list): The wrapped list of Drawables.
        transformation (function): The transformation applied when viewing each Drawable.
        clip (None or ClosedShape): The region to clip when producing a pgf/tikz string of the entire View.

    """

    def __init__(self, transformation=lambda v: v, clip=None):
        self._list = []
        self.transformation = transformation
        self.clip = clip

    def _view(self, item):
        """Returns the transformed item."""
        return self.transformation(item)

    def __str__(self):
        """Returns a string with the transformed Drawables concatenated, and clipped whenever a ClosedShape is provided."""
        data = "\n".join(str(d) for d in self)
        return data if self.clip is None else self.clip.clip(data)

    def copy(self):
        """Returns a copy of the View, where the list is passed as a reference."""
        view = View(self.transformation, self.clip)
        view._list = self._list
        return view

    def apply(self, transformation):
        """Applies the transformation to the View, by composing it with the internal transformation, and applying it to the ClosedShape."""
        self.transformation = compose(transformation, self.transformation)
        if self.clip is not None:
            self.clip = transformation(self.clip)
