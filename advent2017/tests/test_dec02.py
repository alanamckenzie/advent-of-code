from advent2017.code import dec02


def test_max_min_checksum():
    records = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert dec02.get_max_min_checksum(records) == 18
