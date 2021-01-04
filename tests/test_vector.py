import pytest
import pytikz as pt
import numpy as np


def test_vector():

    # Test if Vectors are cast to the correct shape under all circumstances
    assert pt.Vector().shape == (0,)
    assert pt.Vector(0).shape == (1,)
    assert pt.Vector(0, 0).shape == (2,)

    # Test the string representation of a vector
    assert str(pt.Vector(1, 2, 3)) == "(1, 2, 3)"

    # Test the behaviour of Vectors under linear transformations
    transformation = np.array([[1, 0], [3, 1], [4, 0]])
    assert np.all(pt.Vector(1, 2, 3) @ transformation == pt.Vector(19, 2))

    # Test the string representation of a matrix
    assert str(np.ones((2, 2), dtype=np.int8)) == "(1, 1) -- (1, 1)"


class O(pt.vector.Transformable):
    def __init__(self, v):
        self.v = v

    def copy(self):
        return O(self.v)

    def apply(self, transformation):
        self.v = transformation(self.v)


def test_transformation():

    # Test if Vectors are passed directly to the transformation
    t = pt.vector.Transformation(lambda x: x + pt.Vector(0, 1))
    assert (t(pt.Vector(0, 0)) == pt.Vector(0, 1)).all()

    # Test how transformable objects are passed to the transformation

    o = O(pt.Vector(0, 0))
    assert (t(o).v == pt.Vector(0, 1)).all()
    assert (o.v == pt.Vector(0, 0)).all()
    assert (t(o, True).v == pt.Vector(0, 1)).all()
    assert (o.v == pt.Vector(0, 1)).all()

    # Test if non-transformable objects are rejected
    class N:
        pass

    o = N()
    with pytest.raises(ValueError):
        t(o)


def test_scaling():

    # Test if the transformation is correct
    t = pt.vector.Scaling(3, 5, pt.Vector(1, 1))
    assert (t(pt.Vector(1, 2)) == pt.Vector(4, 11)).all()

    # Test if transformations are not rejected
    t(O(pt.Vector(0, 0)))

    # Test if non-scalable objects are rejected
    class N:
        pass

    o = N()
    with pytest.raises(ValueError):
        t(o)


def test_shift():

    # Test if the transformation is correct
    t = pt.vector.Shift(pt.Vector(1, 100))
    assert (t(pt.Vector(1, 2)) == pt.Vector(2, 102)).all()

    # Test if transformations are not rejected
    t(O(pt.Vector(0, 0)))

    # Test if non-scalable objects are rejected
    class N:
        pass

    o = N()
    with pytest.raises(ValueError):
        t(o)
