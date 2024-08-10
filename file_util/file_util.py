
def read_lines_from(path):
    try:
        with open(path, 'tr', encoding="UTF-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print('File not found: ' + path)
        exit(-1)


