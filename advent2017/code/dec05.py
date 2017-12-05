"""
--- Day 5: A Maze of Twisty Trampolines, All Alike ---

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump instructions, and it would like assistance from any programs with spare cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3

Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example, these offset values will be written all on one line, with the current instruction marked in parentheses. The following steps would be taken before an exit is found:

    (0) 3  0  1  -3  - before we have taken any steps.
    (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
     2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
     2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
     2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
     2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?

--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""

from collections import defaultdict


class InstructionJumps:

    def get_offset_increase(self, jump_value):
        """Offset the instruction value by this amount
        
        :param int jump_value: total jump value 
        :return: offset amount
        :rtype: int
        """
        return 1

    def get_num_exit_moves(self, instructions, max_moves=10**8):
        """Find the number of moves required to exit the instruction list.
        Once an instruction is followed, it is offset by get_offset_increase
        
        :param list(int) instructions: base instructions for the next jump 
        :param int max_moves: stop the search after max_moves 
        :return: number of moves required to exit the instruction list
        :rtype: int
        """
        offsets = defaultdict(int)

        this_index = 0
        for i in range(1, max_moves):
            jump_value = instructions[this_index] + offsets[this_index]
            offsets[this_index] += self.get_offset_increase(jump_value)
            this_index += jump_value

            if this_index >= len(instructions):
                return i

        raise Exception(f'Still inside instruction list after {i} jumps')


class InstructionJumpsModified(InstructionJumps):

    def get_offset_increase(self, jump_value):
        return 1 if jump_value < 3 else -1


if __name__ == '__main__':
    import utils

    input = utils.read_file(r'../inputs/dec05_input.txt')
    formatted_input = [int(line) for line in input]

    num_jumps = InstructionJumps().get_num_exit_moves(formatted_input)
    print(f'The number of jumps to exist the instruction list is: {num_jumps}')

    num_jumps_mod = InstructionJumpsModified().get_num_exit_moves(formatted_input)
    print(f'The number of jumps to exist the instruction list with modified offsets is: {num_jumps_mod}')
