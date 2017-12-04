from advent2017.code import dec04


def _run_unique_word_test(input, value):
    assert dec04.is_unique_words(input) == value


def _run_unique_letter_test(input, value):
    assert dec04.is_unique_letters(input) == value


def test_words():
    _run_unique_word_test(['aa', 'bb', 'cc', 'dd', 'ee'], True)
    _run_unique_word_test(['aa', 'bb', 'cc', 'dd', 'aa'], False)
    _run_unique_word_test(['aa', 'bb', 'cc', 'dd', 'aaa'], True)


def test_letters():
    _run_unique_letter_test(['abcde', 'fghij'], True)
    _run_unique_letter_test(['abcde', 'xyz', 'ecdab'], False)
    _run_unique_letter_test(['a', 'ab', 'abc', 'abd', 'abf', 'abj'], True)
    _run_unique_letter_test(['iiii', 'oiii', 'ooii', 'oooi', 'oooo'], True)
    _run_unique_letter_test(['oiii', 'ioii', 'iioi', 'iiio', 'o'], False)
