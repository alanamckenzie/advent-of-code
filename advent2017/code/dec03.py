"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1
and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
(the location of the only access port for this memory system)
by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
"""


def get_steps():
    """Get the maximum number of moves in a single direction"""
    i = 1
    while True:
        yield i
        yield i
        i += 1


def get_spiral_position(square):
    """Get the spiral position of the input square, relative to square 1 at [0, 0].
    
    :param int square: value of the square to find 
    :return: position of the input square
    :rtype: list(int)
    """

    total = 1
    steps = []
    for step in get_steps():
        if total + step > square:
            break
        steps.append(step)
        total += step

    steps.append(square - total)
    pos_x = sum(steps[::4]) - sum(steps[2::4])
    pos_y = sum(steps[1::4]) - sum(steps[3::4])

    return pos_x, pos_y


def get_spiral_distance(input):
    pos_x, pos_y = get_spiral_position(input)
    return abs(pos_x) + abs(pos_y)


if __name__ == '__main__':
    solution = get_spiral_distance(312051)
    print(f'The spiral distance is: {solution}')
