import pytikz as pt


def test_log_round():
    round_down = [
        (0.2, 0.2),
        (0.1, 0.1),
        (0.11, 0.1),
        (101, 100),
        (100, 100),
        (0.9999999, 0.5),
        (2001, 2000),
    ]
    round_up = [
        (0.2, 0.2),
        (0.1, 0.1),
        (0.11, 0.2),
        (101, 200),
        (100, 100),
        (0.9999999, 1),
        (2001, 5000),
    ]
    for a, b in round_down:
        assert pt.graph._log_round(a) == b
    for a, b in round_up:
        assert pt.graph._log_round(a, True) == b
