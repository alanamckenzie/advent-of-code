"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially
jammed, and protocol in situations like this is to switch to a simple repetition code to get the
message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal
(your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example,
suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on.
Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message
being sent?

--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code
instead.

In this modified code, the sender instead transmits what looks like random data, but for each
character, the character they actually want to send is slightly less likely than the others.
Even after signal-jamming noise, you can look at the letter distributions in each column and choose
the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and
so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original
message that Santa is trying to send?
"""
import collections

import utils


def get_message(inputs, position=0):
    num_letters = max([len(line) for line in inputs])
    column_counters = [collections.Counter() for _ in range(num_letters)]

    for line in inputs:
        for i, letter in enumerate(line):
            column_counters[i][letter] = column_counters[i].get(letter, 0) + 1

    # most common returns a list of (value, count) tuples
    # ordered by most to least recent
    message = ''.join([cc.most_common()[position][0][0] for cc in column_counters])
    return message


def run_tests():
    seq = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv",
           "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"]
    res = 'easter'
    act_res = get_message(seq, position=0)
    assert act_res == res, 'MESSAGE BY MOST COMMON LETTER: %r != %r (EXPECTED)' % (act_res, res)

    res = 'advent'
    act_res = get_message(seq, position=-1)
    assert act_res == res, 'MESSAGE BY LEAST COMMON LETTER: %r != %r (EXPECTED)' % (act_res, res)


if __name__ == '__main__':
    run_tests()

    filename = 'dec06_input.txt'
    inputs = utils.read_file(filename)

    print('MESSAGE BY MOST COMMON LETTER: %s' % get_message(inputs, 0))
    print('MESSAGE BY LEAST COMMON LETTER: %s' % get_message(inputs, -1))
