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
    def view(self, item):
        pass

    def __getitem__(self, k):
        return self.view(self._list[k])

    def __iter__(self):
        for k in range(len(self._list)):
            yield self[k]
