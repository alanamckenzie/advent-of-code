"""--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator
is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save
Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star.
Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as
close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves
intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and
face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then
walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and
work out the destination. Given that you can only walk on the street grid of the city, how far
is the shortest path to the destination?

For example:

    Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
    R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
    R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ
is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4
blocks away, due East.

How many blocks away is the first location you visit twice?
"""
import numpy as np

import utils

LEFT_TURN = np.matrix([[0, -1], [1, 0]])
RIGHT_TURN = np.matrix([[0, 1], [-1, 0]])

ROTATE = {'L': LEFT_TURN, 'R': RIGHT_TURN}

def get_new_location(seq):

    ## start facing north
    direction = np.matrix([0, 1]).T

    ## start at 0, 0
    location = np.matrix([0, 0]).T

    moves = seq.split(', ')

    for move in moves:

        move_direction, move_distance = move[0], int(move[1:])

        ## rotate to new direction
        direction = ROTATE[move_direction]*direction

        ## jump to new location
        location += direction*move_distance

    return np.sum(np.abs(location))

def get_first_location_twice(seq):

    ## start facing north
    direction = np.matrix([0, 1]).T

    ## start at 0, 0
    location = np.matrix([0, 0]).T

    visited_locations = set(tuple(location.flat))

    moves = seq.split(', ')

    for move in moves:
        move_direction, move_distance = move[0], int(move[1:])

        ## rotate to new direction
        direction = ROTATE[move_direction]*direction

        ## check whether each step has already been visited
        for _ in range(move_distance):
            location += direction
            flattened_location = tuple(location.flat)

            if flattened_location in visited_locations:
                return np.sum(np.abs(location))

            visited_locations.add(flattened_location)

def run_tests():

    test_cases = [
        ('R2, L3', 5),
        ('R2, R2, R2', 2),
        ('R5, L5, R5, R3', 12)
    ]

    for seq, res in test_cases:
        act_res = get_new_location(seq)
        assert act_res == res, 'GET NEW LOCATION: %r != %r (EXPECTED)' % (act_res, res)

    seq, res = 'R8, R4, R4, R8', 4
    act_res = get_first_location_twice(seq)
    assert act_res == res, 'GET FIRST LOCATION: %r != %r (EXPECTED)' % (act_res, res)

if __name__ == '__main__':

    run_tests()

    filename = 'dec01_input.txt'
    inputs = utils.read_file(filename)[0]

    print('SHORTEST PATH TO DESTINATION (BLOCKS): %r' % get_new_location(inputs))
    print('FIRST DESTINATION VISITED TWICE (BLOCKS): %d' % get_first_location_twice(inputs))
