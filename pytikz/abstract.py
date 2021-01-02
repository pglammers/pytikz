from abc import ABC, abstractmethod


class AbstractList(ABC):
    _type = None
    _list = None

    @abstractmethod
    def __init__(self):
        self._list = []

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


class AbstractObject(ABC):
    anchor = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def copy(self):
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
