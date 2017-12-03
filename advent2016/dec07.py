"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses
(they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs
support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA
is any four-character sequence which consists of a pair of two different characters followed
by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA
within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is
        outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be
    different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's
        within a larger string).

How many IPs in your puzzle input support TLS?

--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences
(outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB,
anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the
same character twice with a different character between them, such as xyx or aba. A corresponding
BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within
    square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence
    is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb,
    even though zaz and zbz overlap).
"""
import re
import utils


def has_four_letter_palindrome(message):
    for i in range(len(message) - 3):
        if message[i] == message[i + 1]:
            continue
        if message[i:i + 2] == message[i + 2:i + 4][::-1]:
            return True

    return False


def get_abas(message):
    abas = set()
    for i in range(len(message) - 2):
        if message[i] == message[i + 2] and message[i] != message[i + 1]:
            abas.add(message[i:i + 3])
    return abas


def is_valid_tls(message):
    split_message = re.split(r'[\[\]]', message)

    # check [xxxx] hypernet sequences
    for i in range(1, len(split_message), 2):
        if has_four_letter_palindrome(split_message[i]):
            return False

    # check remaining sequences
    for i in range(0, len(split_message), 2):
        if has_four_letter_palindrome(split_message[i]):
            return True

    return False


def is_valid_ssl(message):
    split_message = re.split(r'[\[\]]', message)

    hypernet_abas = set()
    # check [xxxx] hypernet sequences
    for i in range(1, len(split_message), 2):
        hypernet_abas = hypernet_abas.union(get_abas(split_message[i]))

    # check remaining sequences
    for i in range(0, len(split_message), 2):
        for aba in get_abas(split_message[i]):
            bab = '%s%s%s' % (aba[1], aba[0], aba[1])
            if bab in hypernet_abas:
                return True
    return False


def count_tls_messages(messages):
    return sum([is_valid_tls(message) for message in messages])


def count_ssl_messages(messages):
    return sum([is_valid_ssl(message) for message in messages])


def run_tests():
    test_cases = [
        ('abba[mnop]qrst', True),
        ('aaaa[qwer]tyui', False),
        ('ioxxoj[asdfgh]zxcvbn', True)
    ]

    for message, res in test_cases:
        act_res = is_valid_tls(message)
        assert act_res == res, 'IS VALID TLS MESSAGE (%s): %r != %r (EXPECTED)' % \
                               (message, act_res, res)

    test_cases = [
        ('aba[bab]xyz', True),
        ('xyx[xyx]xyx', False),
        ('aaa[kek]eke', True),
        ('zazbz[bzb]cdb', True)
    ]

    for message, res in test_cases:
        act_res = is_valid_ssl(message)
        assert act_res == res, 'IS VALID MESSAGE SSH (%s): %r != %r (EXPECTED)' % \
                               (message, act_res, res)


if __name__ == '__main__':
    run_tests()

    filename = 'dec07_input.txt'
    inputs = utils.read_file(filename)

    print('NUMBER OF VALID TLS MESSAGES: %s' % count_tls_messages(inputs))
    print('NUMBER OF VALID SSL MESSAGES: %s' % count_ssl_messages(inputs))
