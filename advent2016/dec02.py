"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush
that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks
on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be
written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the
previous button and moving to adjacent buttons on the keypad: U moves up, D moves down,
L moves left, and R moves right. Each line of instructions corresponds to one button, starting at
the previous button (or, for the first line, the "5" button); press whatever button you're on at the
end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom.
You picture a keypad like this:

1 2 3
4 5 6
7 8 9

Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

    You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"),
    so the first button is 1.

    Starting from the previous button ("1"), you move right twice (to "3") and
    then down three times (stopping at "9" after two moves and ignoring the third),
    ending up with 9.

    Continuing from "9", you move left, up, right, down, and left, ending with 8.
    Finally, you move up four times (stopping at "2"), then down once, ending with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk.
What is the bathroom code?

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can
behold the many fancy conference rooms and water coolers on this floor) and go to punch in the
code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead,
you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same instructions as above,
the outcome is very different:

    You start at "5" and don't move at all (up and left are both edges), ending at 5.
    Continuing from "5", you move right twice and down three times
        (through "6", "7", "B", "D", "D"),
    ending at D.
    Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
    Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

"""

import numpy as np

import utils

KEYPAD_1 = np.array([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']])

KEYPAD_2 = np.array([
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]])

## direction: (row, column)
MOVES = {
    'U': np.array([1, 0]),
    'D': np.array([1, 0]),
    'R': np.array([0, 1]),
    'L': np.array([0, -1])
}

def get_position(value, keypad):
    x_vals, y_vals = np.where(keypad == value)
    return np.array([x_vals[0], y_vals[0]])

def get_value(position, keypad):
    column, row = position[0], position[1]
    return keypad[column, row]

def get_next_code_value(start_value, instructions, keypad):

    position = get_position(start_value, keypad)

    for letter in instructions:
        move_direction = MOVES[letter]
        new_position = position + move_direction

        if get_value(new_position, keypad):
            position = new_position

    return get_value(position, keypad)

def get_code(start_value, instructions, keypad):

    code = []
    for line in instructions:
        code.append(get_next_code_value(start_value, line, keypad))
        start_value = code[-1]

    return ''.join(code)

def run_tests():

    start_value, instructions, res = '5', ['ULL', 'RRDDD', 'LURDL', 'UUUUD'], '1985'
    act_res = get_code(start_value, instructions, KEYPAD_1)
    assert act_res == res, 'GET CODE FROM KEYPAD 1: %r != %r (EXPECTED)' % (act_res, res)

    start_value, instructions, res = '5', ['ULL', 'RRDDD', 'LURDL', 'UUUUD'], '5DB3'
    act_res = get_code(start_value, instructions, KEYPAD_2)
    assert act_res == res, 'GET CODE FROM KEYPAD 2: %r != %r (EXPECTED)' % (act_res, res)

if __name__ == '__main__':
    run_tests()

    filename = 'dec02_input.txt'
    inputs = utils.read_file(filename)

    input_start_value = '5'

    print('CODE FROM KEYPAD 1: %s' % get_code(input_start_value, inputs, KEYPAD_1))
    print('CODE FROM KEYPAD 2: %s' % get_code(input_start_value, inputs, KEYPAD_2))
