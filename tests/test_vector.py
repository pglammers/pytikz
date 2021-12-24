import pytest
import pytikz as pt
import numpy as np
from plum import dispatch


# Revised 2021-12-24


class V(pt.vector.EnhancedVector):
    @dispatch
    def vector(self) -> pt.vector.VectorType:
        return pt.Vector(1, 2)


def test_Vector():
    # Test if Vectors are cast to the correct shape under all circumstances
    assert pt.Vector().shape == (0,)
    assert pt.Vector(0).shape == (1,)
    assert pt.Vector(0, 0).shape == (2,)

    # Test casting with Vector
    v = pt.Vector(1, 2, 3)
    assert pt.Vector(v) is v

    # Test casting with EnhancedVector
    assert np.all(pt.Vector(V()) == pt.Vector(1, 2))

    # Test the behaviour of Vectors under linear transformations
    matrix = np.array([[1, 0], [3, 1], [4, 0]])
    assert np.all(pt.Vector(1, 2, 3) @ matrix == pt.Vector(19, 2))


def test_coordinate_string():
    # Test the string representation of a Vector
    assert pt.vector.coordinate_string(pt.Vector(1, 3)) == "(1, 3)"

    # Test the string representation of an EnhancedVector
    assert pt.vector.coordinate_string(V()) == "(1, 2)"

    # Restrict representation to 2D vectors
    with pytest.raises(TypeError):
        pt.vector.coordinate_string(pt.Vector(1, 3, 1))


class GenericTransformable(pt.vector.Transformable):
    @dispatch
    def __init__(self, v: pt.vector.VectorType):
        self.v = v

    @dispatch
    def copy(self) -> "GenericTransformable":
        return GenericTransformable(self.v)

    @dispatch
    def apply(self, transformation: pt.vector.Transformation) -> None:
        self.v = transformation(self.v)


def test_Transformation():
    # Create a generic transformation
    t = pt.vector.Transformation(lambda x: 2 * x)

    # Apply the transformation directly to a Vector
    assert np.all((t(pt.Vector(1, 2))) == pt.Vector(2, 4))

    # Create a Transformable and apply the Transformation internally
    g = GenericTransformable(pt.Vector(3, 3))
    assert t(g, inplace=True) is None
    assert np.all(g.v == pt.Vector(6, 6))

    # Create a Transformable and apply the Transformation
    g = GenericTransformable(pt.Vector(3, 3))
    h = t(g)
    assert np.all(g.v == pt.Vector(3, 3))
    assert np.all(h.v == pt.Vector(6, 6))

    # Create a new tranformation and a new dummy vector
    t2 = pt.vector.Transformation(lambda x: x + pt.Vector(1, 3))
    v = pt.Vector(10, 10)

    # Apply the composed transformation to the dummy vector
    v_transformed = (t2 * t)(v)

    # Check that the output is correct
    assert np.all((v_transformed) == pt.Vector(21, 23))


class A(pt.vector.AnchoredObject):
    def copy(self):
        pass


def test_AnchoredObject():
    # Test that an AnchoredObject cannot be instantiated
    with pytest.raises(TypeError):
        pt.vector.AnchoredObject()

    # Create a generic transformation
    t = pt.vector.Transformation(lambda x: 2 * x)

    # Create an arbitrary anchored object with anchor set to None
    a = A()

    # Test that it cannot be transformed
    with pytest.raises(AttributeError):
        t(a)

    # Set the anchor to something sensible
    a.anchor = pt.Vector(1, 3)

    # Check that the transformation is applied appropriately
    t(a, inplace=True)
    assert np.all((a.anchor) == pt.Vector(2, 6))

    # Check that vectors are resolved correctly
    assert np.all((a.anchor_resolve(pt.Vector(1, 1))) == pt.Vector(3, 7))


def test_AnchoredVector():
    # Create some dummies
    a = pt.Vector(1, 3)
    b = pt.Vector(4, 2)
    t = pt.vector.Transformation(lambda x: 2 * x)

    # Create an AnchoredVector and its transformation
    v = pt.vector.AnchoredVector(a, b)
    v2 = t(v)

    # Verify that they represent the correct vectors
    assert np.all(pt.Vector(v) == pt.Vector(5, 5))
    assert np.all(pt.Vector(v2) == pt.Vector(6, 8))

    # Apply the transformation in place and verify that the result is correct
    t(v, inplace=True)
    assert np.all(pt.Vector(v) == pt.Vector(6, 8))
