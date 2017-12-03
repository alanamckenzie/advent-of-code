"""--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction.
"You there! Your state appears to be idle.
Come help us repair the corruption in this spreadsheet - if we take another millisecond,
we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum.
For each row, determine the difference between the largest value and the smallest value;
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""


def get_max_min_checksum(records):
    """Calculate the checksum from the input records,
    which is the total of the difference between the max and min value of each row.
    
    :param list(list(int)) records: rows of integers  
    :return: checksum
    :rtype: int
    """
    return sum([max(row) - min(row) for row in records])

if __name__ == '__main__':

    import utils
    input = utils.read_file(r'../inputs/dec02_input.txt')
    formatted_input = [[int(item) for item in line.split()] for line in input]

    max_min_checksum = get_max_min_checksum(formatted_input)
    print(f'The total max-min checksum is: {max_min_checksum}')