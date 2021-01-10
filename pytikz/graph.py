import math


def _log_round(value, up=False):
    assert value > 0
    normalized_value = 10 ** int(math.floor(math.log10(value)))
    potential_values = [k * normalized_value for k in [1, 2, 5, 10]]
    if up:
        for v in potential_values:
            if v >= value:
                return v
    else:
        potential_values.reverse()
        for v in potential_values:
            if v <= value:
                return v
    raise NotImplementedError(value)
