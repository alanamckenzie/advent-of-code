"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is
encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby.
Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash,
a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name,
in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and
    then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each),
    the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
from collections import defaultdict
import re

import utils

def extract_input_params(seq):
    pattern = r'(?P<encrypted_name>[a-z\-]+)(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)\]'
    match = re.search(pattern, seq)
    return match.group('encrypted_name'), int(match.group('sector_id')), match.group('checksum')

def get_checksum(encrypted_name):

    ## setup a histogram of letter counts
    hist = defaultdict(int)
    for letter in encrypted_name:
        if letter == '-':
            continue
        hist[letter] += 1

    ## sort by most frequent letter (descending), then letter (ascending)
    sorted_letters = sorted([(freq, letter) for letter, freq in hist.items()],
                            key=lambda x: (-x[0], x[1]))

    ## return the top 5 letters
    return ''.join([letter for freq, letter in sorted_letters[:5]])

def shift_cypher(encrypted_name, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in encrypted_name:
        if letter == '-':
            result.append(' ')
            continue
        i = alphabet.index(letter)
        new_i = (i + shift) % len(alphabet)

        result.append(alphabet[new_i])

    return (''.join(result)).strip()

def get_decrypted_name(seq):
    encrypted_name, sector_id, _ = extract_input_params(seq)

    decrypted_name = shift_cypher(encrypted_name, sector_id)

    return decrypted_name

def get_real_sector_id(seq):
    encrypted_name, sector_id, checksum = extract_input_params(seq)

    if get_checksum(encrypted_name) != checksum:
        return 0

    return sector_id

def sum_real_sector_ids(seq_list):
    return sum([get_real_sector_id(seq) for seq in seq_list])

def get_north_pole_sector_id(seq_list, verbose=False):
    result = None
    for seq in seq_list:
        encrypted_name, sector_id, checksum = extract_input_params(seq)
        if get_checksum(encrypted_name) != checksum:
            continue

        decrypted_name = shift_cypher(encrypted_name, sector_id)
        if 'north' in decrypted_name and 'pole' in decrypted_name:
            result = sector_id
            if verbose:
                print('\tFOUND A CANDIDATE ROOM: %s' % decrypted_name)

    return result

def run_tests():

    test_cases = [
        ('aaaaa-bbb-z-y-x-123[abxyz]', 123),
        ('a-b-c-d-e-f-g-h-987[abcde]', 987),
        ('not-a-real-room-404[oarel]', 404),
        ('totally-real-room-200[decoy]', 0)
    ]

    for seq, res in test_cases:
        act_res = get_real_sector_id(seq)
        assert act_res == res, 'REAL SECTOR ID: %r != %r (EXPECTED)' % (act_res, res)

    seq = 'qzmt-zixmtkozy-ivhz-343[zimtk]'
    res = 'very encrypted name'
    act_res = get_decrypted_name(seq)
    assert act_res == res, 'DECRYPTED NAME: %r != %r (EXPECTED)' % (act_res, res)

if __name__ == '__main__':

    run_tests()

    filename = 'dec04_input.txt'
    inputs = utils.read_file(filename)

    print('SUM OF REAL SECTOR IDS: %r' % sum_real_sector_ids(inputs))
    print('NORTH POLE OBJECTS ARE STORED IN SECTOR ID: %r' \
        % get_north_pole_sector_id(inputs, verbose=True))
