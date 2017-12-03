from advent2017.code import dec01


def _run_test(captcha, value, offset=1):
    assert dec01.get_captcha_match_sum(captcha, offset=offset) == value


def tests():
    _run_test('1122', 3, offset=1)
    _run_test('1111', 4, offset=1)
    _run_test('1234', 0, offset=1)
    _run_test('91212129', 9, offset=1)

    _run_test('1212', 6, offset=2)
    _run_test('1221', 0, offset=2)
    _run_test('123425', 4, offset=3)
    _run_test('123123', 12, offset=3)
    _run_test('12131415', 4, offset=4)
