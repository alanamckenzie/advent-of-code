"""
--- Day 21: Scrambled Letters and Hash ---

The computer system you're breaking into uses a weird scrambling function to store its passwords.
It shouldn't be much trouble to create your own scrambled password so you can add it to the system;
you just have to implement the scrambler.

The scrambling function is a series of operations (the exact list is provided in your puzzle input).
Starting with the password to be scrambled, apply each operation in succession to the string.
The individual operations behave as follows:

    swap position X with position Y means that the letters at indexes X and Y (counting from 0)
    should be swapped.
    swap letter X with letter Y means that the letters X and Y should be swapped (regardless of
    where they appear in the string).
    rotate left/right X steps means that the whole string should be rotated; for example, one right
    rotation would turn abcd into dabc.
    rotate based on position of letter X means that the whole string should be rotated to the right
    based on the index of letter X (counting from 0) as determined before this instruction does any
    rotations. Once the index is determined, rotate the string to the right one time, plus a number
    of times equal to that index, plus one additional time if the index was at least 4.
    reverse positions X through Y means that the span of letters at indexes X through Y
    (including the letters at X and Y) should be reversed in order.
    move position X to position Y means that the letter which is at index X should be removed from
    the string, then inserted such that it ends up at index Y.

For example, suppose you start with abcde and perform the following operations:

    swap position 4 with position 0 swaps the first and last letters, producing the input for the
    next step, ebcda.
    swap letter d with letter b swaps the positions of d and b: edcba.
    reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
    rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the
    end of the string: bcdea.
    move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position
    4 (the end of the string): bdeac.
    move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position
    0 (the front of the string): abdec.
    rotate based on position of letter b finds the index of letter b (1), then rotates the string
    right once plus a number of times equal to that index (2): ecabd.
    rotate based on position of letter d finds the index of letter d (4), then rotates the string
    right once, plus a number of times equal to that index, plus an additional time because the
    index was at least 4, for a total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can access the system. Given the
list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

Your puzzle answer was cbeghdaf.
--- Part Two ---

You scrambled the password correctly, but you discover that you can't actually modify the password
file on the system. You'll need to un-scramble one of the existing passwords by reversing the
scrambling process.

What is the un-scrambled version of the scrambled password fbgdceah?

Your puzzle answer was bacdefgh.
"""

import utils


def swap_position(message, pos_x, pos_y):
    """swap the letters at indexes X and Y (counting from 0)"""
    m_list = list(message)
    m_list[pos_x], m_list[pos_y] = m_list[pos_y], m_list[pos_x]
    return ''.join(m_list)


def swap_letter(message, letter1, letter2):
    """swap the letters X and Y (regardless of where they appear in the string)"""
    message = message.replace(letter1, '?')
    message = message.replace(letter2, letter1)
    message = message.replace('?', letter2)
    return message


def rotate_right(message, pos):
    """rotate the whole string to the right"""
    length = len(message)
    return message[length - pos:] + message[:length - pos]


def rotate_left(message, pos):
    """rotate the whole string to the left"""
    return message[pos:] + message[:pos]


def rotate_by_position(message, letter):
    """rotate the whole string to the right based on the index of letter X (counting from 0)
     as determined before this instruction does any rotations. Once the index is determined,
     rotate the string to the right one time, plus a number of times equal to that index,
     plus one additional time if the index was at least 4."""
    pos = message.find(letter)
    if pos >= 4:
        pos += 1
    return rotate_right(message, pos + 1)


def reverse_rotate_by_position(message, letter):
    """reverse the rotate_by_position function"""
    for i in range(len(message)):
        unscrambled_message = rotate_left(message, i)
        if message == rotate_by_position(unscrambled_message, letter):
            return unscrambled_message


def reverse(message, start_pos, end_pos):
    """the span of letters at indexes X through Y (including the letters at X and Y)
    should be reversed in order."""
    return message[:start_pos] + message[start_pos:end_pos + 1][::-1] + message[end_pos + 1:]


def move(message, old_pos, new_pos):
    """the letter which is at index X should be removed from the string,
    then inserted such that it ends up at index Y"""
    letter = message[old_pos]
    message = message[:old_pos] + message[old_pos + 1:]
    return message[:new_pos] + letter + message[new_pos:]


def scramble(instructions, message):
    for instruction in instructions:
        action, *params = instruction.split(' ')

        if action == 'swap':
            if params[0] == 'position':
                # swap position X with position Y
                message = swap_position(message, int(params[1]), int(params[4]))

            elif params[0] == 'letter':
                # swap letter X with letter Y
                message = swap_letter(message, params[1], params[4])

        elif action == 'rotate':
            if params[0] == 'left':
                # rotate left X steps
                message = rotate_left(message, int(params[1]))

            elif params[0] == 'right':
                # rotate right X steps
                message = rotate_right(message, int(params[1]))

            elif params[0] == 'based':
                # rotate based on position of letter X
                message = rotate_by_position(message, params[5])

        elif action == 'reverse':
            # reverse positions X through Y
            message = reverse(message, int(params[1]), int(params[3]))

        elif action == 'move':
            # move position X to position Y
            message = move(message, int(params[1]), int(params[4]))

    return message


def unscramble(instructions, message):
    for instruction in instructions:
        action, *params = instruction.split(' ')
        if action == 'swap':
            if params[0] == 'position':
                # reverse: swap position X with position Y
                message = swap_position(message, int(params[4]), int(params[1]))

            elif params[0] == 'letter':
                # reverse: swap letter X with letter Y
                message = swap_letter(message, params[4], params[1])

        elif action == 'rotate':
            if params[0] == 'left':
                # reverse: rotate left X steps
                message = rotate_right(message, int(params[1]))

            elif params[0] == 'right':
                # reverse: rotate right X steps
                message = rotate_left(message, int(params[1]))

            elif params[0] == 'based':
                # reverse: rotate based on position of letter X
                message = reverse_rotate_by_position(message, params[5])

        elif action == 'reverse':
            # reverse: reverse positions X through Y
            message = reverse(message, int(params[1]), int(params[3]))

        elif action == 'move':
            # reverse: move position X to position Y
            message = move(message, int(params[4]), int(params[1]))

    return message


def run_tests():
    instructions = [
        'swap position 4 with position 0',
        'swap letter d with letter b',
        'reverse positions 0 through 4',
        'rotate left 1',
        'move position 1 to position 4',
        'move position 3 to position 0',
        'rotate based on position of letter b',
        'rotate based on position of letter d'
    ]

    message = 'abcde'
    scrambled_message = 'decab'

    act_res = scramble(instructions, message)
    assert act_res == scrambled_message, 'SCRAMBLED MESSAGE: %r != %r (EXPECTED)' % \
                                         (act_res, scrambled_message)

    act_res = unscramble(instructions[::-1], scrambled_message)
    assert act_res == message, 'UNSCRAMBLED MESSAGE: %r != %r (EXPECTED)' % (act_res, message)


if __name__ == '__main__':
    run_tests()

    filename = 'dec21_input.txt'
    inputs = utils.read_file(filename)

    print('SCRAMBLED MESSAGE: %s' % (scramble(inputs, 'abcdefgh')))
    print('UNSCRAMBLED MESSAGE: %s' % (unscramble(inputs[::-1], 'fbgdceah')))
