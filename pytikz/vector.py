import numpy as np


def _tikz_representation(array):
    """Alternative .__str__ method for np.ndarray."""
    if array.ndim == 1:
        return f"({', '.join([str(c) for c in array])})"
    elif array.ndim == 2:
        return " -- ".join(str(v) for v in array)
    else:
        raise ValueError(
            f"Arrays of dimension {array.ndim} have no TikZ representation."
        )


np.set_string_function(
    _tikz_representation, False
)  # Presents this .__str__ method to np.


def Vector(*args):
    """Generates a vector; used to control its generation."""
    return np.array(list(args))
