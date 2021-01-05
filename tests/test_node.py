import pytest
import pytikz as pt
import numpy as np


def test_node():
    n = pt.Node(pt.Vector(1), "test")
    assert str(n) == "\\node at (1) {test};"

    m = pt.Node(pt.vector.AnchoredVector(pt.Vector(3), pt.Vector(5)), "test")
    assert str(m) == "\\node at (8) {test};"

    t = pt.vector.Transformation(lambda x: 2 * x)
    assert str(t(n)) == "\\node at (2) {test};"
    assert str(t(m)) == "\\node at (11) {test};"

    assert str(n) == "\\node at (1) {test};"
    assert str(m) == "\\node at (8) {test};"

    t(n, True)
    t(m, True)

    assert str(n) == "\\node at (2) {test};"
    assert str(m) == "\\node at (11) {test};"

    n = pt.Node(pt.Vector(1), "test", pt.Orientation.SOUTH_EAST)
    assert str(n) == "\\node[anchor=south east] at (1) {test};"
