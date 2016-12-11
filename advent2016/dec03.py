"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture
that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are
covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of
these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example,
the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

import utils

def is_triangle(sides):
    if len(sides) < 3:
        return False

    sides = sorted(sides)
    return sides[2] < sides[0] + sides[1]

def count_triangles(side_list):
    num_triangles = 0
    for sides_text in side_list:
        sides = [int(s) for s in sides_text.split()]

        if is_triangle(sides):
            num_triangles += 1

    return num_triangles

def get_next_three_horizontal_sides(lines):
    num_lines = 3
    for i in range(0, len(lines), num_lines):
        result = []
        for j in range(3):
            result.append([int(s) for s in lines[i+j].split()])
        yield result

def count_vertical_triangles(text):
    num_triangles = 0

    horizontal_side_gen = get_next_three_horizontal_sides(text)
    for horizontal_side_list in horizontal_side_gen:
        for i in range(3):
            ## use the ith column value for each side
            vertical_sides = [s[i] for s in horizontal_side_list]
            if is_triangle(vertical_sides):
                num_triangles += 1

    return num_triangles

def run_tests():

    test_cases = [
        (['1 5 7', '10 5 2', '11 6 6'], 1),
    ]

    for seq, res in test_cases:
        act_res = count_triangles(seq)
        assert act_res == res, 'COUNT TRIANGLES: %r != %r (EXPECTED)' % (act_res, res)

    test_cases = [
        (['1 5 7', '10 5 2', '6 6 11'], 1),
    ]

    for seq, res in test_cases:
        act_res = count_vertical_triangles(seq)
        assert act_res == res, 'COUNT VERTICAL TRIANGLES: %r != %r (EXPECTED)' % (act_res, res)

if __name__ == '__main__':

    run_tests()

    filename = 'dec03_input.txt'
    inputs = utils.read_file(filename)

    print('TRIANGLE COUNT: %r' % count_triangles(inputs))
    print('VERTICAL TRIANGLE COUNT: %d' % count_vertical_triangles(inputs))
