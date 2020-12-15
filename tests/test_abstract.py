import pytikz, pytest


def test_abstract():
    class TestList(pytikz.AbstractList):

        _type = int

        def __init__(self):
            self._list = []

        def _view(self, item):
            return item + 1

    l = TestList()
    l.append(1)
    assert [x for x in l] == [2]
