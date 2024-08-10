from os import path
import sys
from pathlib import Path
from colorama import Fore


def get_target_dir_from_args():
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        if path.isdir(target_path):
            return target_path
        else:
            print("Specified path is not exist or is not a directory: " + target_path)
            exit(-2)
    else:
        print("Please specify a target path: python dir_tree.py <target path>")
        exit(-1)


def print_tree_entry(deep, suffix, path):
    prefix = (deep - 1) * "| " + "|-"
    if path.is_dir():
        dir_content = path.iterdir()
        for item in dir_content:
            if item.is_dir():
                print(Fore.BLUE + prefix + item.name + "\\" + Fore.RESET)
                print_tree_entry(deep + 1, suffix + "--", item)
            else:
                print(prefix + suffix + item.name)
    else:
        print(suffix + path.name)


def main():
    print_tree_entry(1, "", Path(get_target_dir_from_args()))


if __name__ == '__main__':
    main()
