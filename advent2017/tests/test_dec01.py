from advent2017.code import dec01


def _run_test(captcha, value):
    assert dec01.get_captcha_match_sum(captcha) == value


def tests():
    _run_test('1122', 3)
    _run_test('1111', 4)
    _run_test('1234', 0)
    _run_test('91212129', 9)