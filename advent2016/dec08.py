"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor
authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk).
Then, it displays a code on a little screen, and you type that code on a keypad.
Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart
and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these
instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which
start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is
    A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels.
    Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by
    B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom
    pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the
tiny-code-displaying-screen market. That's what the advertisement on the back of the display
tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe
your card, if the screen did work, how many pixels should be lit?

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
"""
import numpy as np
import utils

def rotate_column(screen, col, num_pixels):
    new_screen = np.array(screen)
    height = screen.shape[0]
    if num_pixels <= 0:
        return new_screen
    new_screen[:num_pixels, col] = screen[height-num_pixels:, col]
    new_screen[num_pixels:, col] = screen[:height-num_pixels, col]

    return new_screen

def rotate_row(screen, row, num_pixels):
    new_screen = np.array(screen)
    width = screen.shape[1]
    if num_pixels <= 0:
        return new_screen
    new_screen[row, :num_pixels] = screen[row, width-num_pixels:]
    new_screen[row, num_pixels:] = screen[row, :width-num_pixels]

    return new_screen

def rect(screen, width, height):
    new_screen = np.array(screen)
    if height <= 0 or width <= 0:
        return new_screen

    new_screen[:height, :width] = '#'
    return new_screen

def get_screen(instructions, screen_width, screen_height):
    screen = np.array(['.']*screen_height*screen_width).reshape((screen_height, screen_width))

    for instruction in instructions:
        action, *params = instruction.split(' ')
        if action == 'rect':
            str_x, str_y = params[0].split('x')
            screen = rect(screen, int(str_x), int(str_y))

        if action == 'rotate':
            ## either: rotate row y=A by B
            ## or rotate column x=A by B
            row_or_column, coord, _, str_num_pixels = params
            _, str_index = coord.split('=')
            if row_or_column == 'row':
                #print('ROW: %d, %d' % (int(str_index), int(str_num_pixels)))
                screen = rotate_row(screen,
                                    int(str_index),
                                    int(str_num_pixels))

            elif row_or_column == 'column':
                screen = rotate_column(screen,
                                       int(str_index),
                                       int(str_num_pixels))

    return screen

def count_screen_on(screen):
    return np.sum(screen == '#')

def run_tests():

    instructions = ['rect 3x2',
                    'rotate column x=1 by 1',
                    'rotate row y=0 by 4',
                    'rotate column x=1 by 1']

    res = np.array([['.', '#', '.', '.', '#', '.', '#'],
                    ['#', '.', '#', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '.', '.', '.']]).tolist()

    act_res = get_screen(instructions, 7, 3).tolist()
    assert act_res == res, 'IS VALID MESSAGE: %r != %r (EXPECTED)' % (act_res, res)

    #res = 'advent'
    #act_res = is_valid_message(message)
    #assert act_res == res, 'MESSAGE BY LEAST COMMON LETTER: %r != %r (EXPECTED)' % (act_res, res)


if __name__ == '__main__':

    run_tests()

    filename = 'dec08_input.txt'
    inputs = utils.read_file(filename)

    screen = get_screen(inputs, 50, 6)
    print('NUMBER OF LIT PIXELS: %s' % count_screen_on(screen))
    print('SCREEN MESSAGE:')
    for row in screen:
        print(''.join(row.tolist()))
