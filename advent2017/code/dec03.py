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

How many steps are required to carry the data from the square identified in your puzzle input
all the way to the access port?

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1.
Then, in the same allocation order as shown above,
they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
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


def get_neighbour_values(spiral, pos_x, pos_y):
    return sum([spiral.get((pos_x + x, pos_y + y), 0) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)])


def get_spiral_sum_position(square_value):
    """Get the spiral position of the first square with value greater than square_value.
     The square value is the value of all neighbouring squares.
     
     The position and value is relative to square 1 at [0, 0].

    :param int square_value: value of the square to find 
    :return: position of the first square with value greater than the input square_value
    :rtype: list(int)
    """

    if square_value == 1:
        return 0, 0

    pos_x, pos_y = 0, 0
    dir_i = 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    spiral = {(0, 0): 1}

    for step in get_steps():
        for _ in range(step):
            pos_x += directions[dir_i][0]
            pos_y += directions[dir_i][1]
            value = get_neighbour_values(spiral, pos_x, pos_y)

            if value >= square_value:
                return pos_x, pos_y
            spiral[(pos_x, pos_y)] = value

        # change direction
        dir_i = (dir_i + 1) % len(directions)

    raise Exception(f'Position for square {square_value} not found')


def get_spiral_distance(input):
    pos_x, pos_y = get_spiral_position(input)
    return abs(pos_x) + abs(pos_y)


def get_spiral_sum_distance(input):
    pos_x, pos_y = get_spiral_sum_position(input)
    return abs(pos_x) + abs(pos_y)


if __name__ == '__main__':
    solution = get_spiral_distance(312051)
    print(f'The spiral distance is: {solution}')

    solution_sum = get_spiral_sum_distance(312051)
    print(f'The spiral sum distance is: {solution_sum}')