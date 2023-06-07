from plum import dispatch
from typing import Union
from ..vector import Transformation, Transformable, VectorType
from ..shape import Path, ClosedPath


class FuzzyTransformation(Transformation):
    # should turn a path into a fuzzy path
    # and a closed path into a fuzzy closed path
    # this means that their behaviour changes when they are actually written to the doc
    def __init__(self):
        raise NotImplementedError

    @dispatch
    def __call__(
        self, subject: Path, *, inplace: bool = False
    ) -> Union[None, Transformable]:
        raise NotImplementedError
