"""--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium
of the last one.
Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a
wall or an open space.
You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y;
negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical.
You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

    Find x*x + 3*x + 2*x*y + y + y*y.
    Add the office designer's favorite number (your puzzle input).
    Find the binary representation of that sum; count the number of bits that are 1.
        If the number of bits that are 1 is even, it's an open space.
        If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as .,
the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1352.

--- Part Two ---

How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?
"""

maze = {}


def get_function(favourite_number):

    def f(x, y):

        if x < 0 or y < 0:
            return False

        value = x*x + 3*x + 2*x*y + y + y*y + favourite_number
        num_ones = sum([int(i) for i in str(bin(value))[2:]])
        return num_ones//2 == num_ones/2

    return f


def get_moves(location, func):
    global maze
    moves = []
    for i, j in ([-1, 0], [0, -1], [1, 0], [0, 1]):

        move = (location[0] + i, location[1] + j)

        if move not in maze:
            maze[move] = func(*move)

        if maze[move]:
            moves.append(move)

    return moves


def print_maze(num_moves):
    results = [[' ']*num_moves for _ in range(num_moves)]
    for move, value in maze.items():
        if not value:
            results[move[1]][move[0]] = '#'
        else:
            results[move[1]][move[0]] = '.'
    print('\n'.join([''.join([r for r in result]) for result in results]))


def run(favourite_number, target=None, max_moves=1000):

    paths = [
        [(1, 1)],
    ]
    func = get_function(favourite_number)
    for move_num in range(1, max_moves+1):

        new_paths = []
        while paths:
            path = paths.pop()
            moves = get_moves(path[-1], func)
            for move in moves:
                if move in path:
                    continue
                new_path = path + [move]
                if target and move == target:
                    raise Exception(f'REACHED {target} IN {move_num} MOVES: {new_path}')

                new_paths.append(new_path)

        paths = new_paths

        if not paths:
            print_maze(move_num)
            raise Exception(f'NO MORE FREE SPACES AFTER MOVE {move_num}')

    if target:
        raise Exception(f'TARGET NOT REACHED AFTER MOVE {move_num}')

    unique_moves = [k for k, v in maze.items() if v]
    print(f'{len(unique_moves)} UNIQUE COORDINATES AFTER {move_num} MOVES')

if __name__ == '__main__':

    # run(1352, (31, 39), None)
    run(1352, None, 50)
