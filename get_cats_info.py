from file_util.file_util import read_lines_from


def get_cats_info(path):
    lines = read_lines_from(path)

    cats_info = []
    for line in lines:
        id, name, age = line.split(',')
        cats_info.append({"id": id, "name": name, "age": age})

    return cats_info


def main():
    cats_info = get_cats_info("get_cats_info/cat_data.txt")
    print(cats_info)


if __name__ == '__main__':
    main()
