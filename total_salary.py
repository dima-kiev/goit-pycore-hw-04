from file_util.file_util import read_lines_from


def total_salary(path):
    lines = read_lines_from(path)

    total = 0
    for line in lines:
        name, salary = line.split(',')
        total += int(salary)

    average = total / len(lines)

    return total, average


def main():
    total, average = total_salary("total_salary/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    total_salary("no_such_file.txt")


if __name__ == '__main__':
    main()
