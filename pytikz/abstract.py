from abc import ABC, abstractmethod


# Definition of Drawable


class Drawable(ABC):
    @abstractmethod
    def __str__(self):
        pass


class AbstractList(ABC):
    """Wrapped list which transforms elements through the .view method upon access."""

    _type = None
    _list = None

    def __init__(self, data=[]):
        self._list = []
        for d in data:
            self.append(d)

    def append(self, item):
        if not issubclass(type(item), self._type):
            raise TypeError
        self._list.append(item)

    @abstractmethod
    def _view(self, item):
        pass

    def __getitem__(self, k):
        return self._view(self._list[k])

    def __iter__(self):
        for k in range(len(self._list)):
            yield self[k]


class AbstractDrawable(ABC):
    """Abstract class for any object that can be drawn directly on the canvas."""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def apply(self, transformation):
        pass

    @abstractmethod
    def copy(self):
        pass


class AbstractObject(ABC):
    """Abstract class for any object eventually appearing on the canvas.

    Features the .anchor property, which allows only the relative position rather than the whole object to be transformed by the .apply method.
    """

    anchor = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def apply_internally(self, transformation):
        pass

    def apply(self, transformation):
        """Distributes the application of the transformation."""
        if self.anchor is None:
            self.apply_internally(transformation)
        else:
            self.anchor = transformation(self.anchor)
        return self

    def _view(self, item):
        if self.anchor is None:
            return item
        else:
            return self.anchor + item

    @abstractmethod
    def copy(self):
        pass
