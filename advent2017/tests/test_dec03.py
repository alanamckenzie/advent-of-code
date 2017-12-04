from advent2017.code import dec03


def _run_test(input, value):
    assert dec03.get_spiral_distance(input) == value


def tests():
    _run_test(1, 0)
    _run_test(12, 3)
    _run_test(23, 2)
    _run_test(1024, 31)
