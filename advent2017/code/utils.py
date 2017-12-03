def read_file(filename, line_delimiter='\n'):
    """Read the contents of a file
    
    :param str filename: full path to the text file to open 
    :param line_delimiter: line delimiter used in the file
    :return: contents of the file, with one list item per line
    :rtype: list
    """
    with open(filename, 'r') as fin:
        text = fin.read().strip()
    return text.split(line_delimiter)
