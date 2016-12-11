def read_file(filename, line_delimiter='\n'):
    with open(filename, 'r') as fin:
        text = fin.read().strip()
    return text.split(line_delimiter)
