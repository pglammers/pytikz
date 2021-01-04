from abc import ABC, abstractmethod


# Definition of Drawable


class Drawable(ABC):
    @abstractmethod
    def __str__(self):
        pass


class AbstractList(ABC):
    """Wrapped list which transforms elements through the .view method upon access."""

    _list = None

    def __init__(self, data=None):
        self._list = []
        if data is not None:
            self._list = data

    def _view(self, item):
        return item

    def append(self, item):
        self._list.append(item)

    def __setitem__(self, k, value):
        self._list[k] = value

    def __getitem__(self, k):
        return self._view(self._list[k])

    def __iter__(self):
        for k in range(len(self._list)):
            yield self[k]
