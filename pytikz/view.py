from .abstract import AbstractList, AbstractDrawable
from .shape import Shape


class View(AbstractList):
    """Bundles a list of drawables with a common transformation."""

    _type = AbstractDrawable
    clip = None

    def __init__(self, transformation=lambda vector: vector):
        self._list = []
        self.transformation = transformation

    def _view(self, item):
        return item.copy().apply(self.transformation)

    def wrap_clip(self, text):
        if self.clip is None:
            return text
        else:
            if not issubclass(type(self.clip), Shape):
                raise TypeError
            if not self.clip.cycle:
                raise ValueError
            return (
                "\\begin{scope}\n"
                f"\\clip {str(self.clip)};\n"
                f"{text}\n"
                "\\end{scope}"
            )

    def __str__(self):
        return self.wrap_clip("\n".join([str(o) for o in self]))
