from advent2017.code import dec03


def _run_spiral_test(input, value):
    assert dec03.get_spiral_distance(input) == value


def _run_spiral_sum_test(input, value):
    assert dec03.get_spiral_sum_value(input) == value


def test_spiral():
    _run_spiral_test(1, 0)
    _run_spiral_test(12, 3)
    _run_spiral_test(23, 2)
    _run_spiral_test(1024, 31)


def test_spiral_sum():
    _run_spiral_sum_test(1, 1)
    _run_spiral_sum_test(12, 23)
    _run_spiral_sum_test(23, 23)
    _run_spiral_sum_test(360, 362)
