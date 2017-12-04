"""--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

For added security, yet another system policy has been put in place.
Now, a valid passphrase must contain no two words that are anagrams of each other -
that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
"""


def is_unique_words(line):
    """Determine whether the words in line are unique

    :param list(str) line: a list of words 
    :return: True if each word is unique. False otherwise
    :rtype: bool
    """
    unique_words = set()
    for word in line:
        if word in unique_words:
            return False
        unique_words.add(word)

    return True


def is_unique_letters(line):
    """Determine whether the words in line are each composed of unique letters
    
    :param list(str) line: a list of words 
    :return: True if the letters in each word are unique. False otherwise
    :rtype: bool
    """
    unique_letters = set()
    for word in line:
        letters = str(sorted(list(word)))
        if letters in unique_letters:
            return False
        unique_letters.add(letters)

    return True


def get_num_unique_word_lines(input):
    """Get the number of word lists with unique words
    
    :param list(list(str)) input: a list of word lists
    :return: the number of word lists with unique words
    :rtype: int
    """
    return sum([1 for line in input if is_unique_words(line)])


def get_num_unique_letter_lines(input):
    """Get the number of word lists with unique letters in each word

    :param list(list(str)) input: a list of word lists
    :return: the number of word lists with unique letters in each word
    :rtype: int
    """
    return sum([1 for line in input if is_unique_letters(line)])


if __name__ == '__main__':
    import utils

    input = utils.read_file(r'../inputs/dec04_input.txt')
    formatted_input = [line.split() for line in input]

    num_unique_words = get_num_unique_word_lines(formatted_input)
    print(f'The number of lines with unique words is: {num_unique_words}')

    num_unique_letters = get_num_unique_letter_lines(formatted_input)
    print(f'The number of lines with unique letters in each word is: {num_unique_letters}')
