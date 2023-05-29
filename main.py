#!/usr/bin/python3
import os
from sys import argv
from src import (bring_files_to_root, delete_nested_directory, 
                  create_directory, filter_files, clean_path)
def main(root) -> None:
    """
        main - entry point to our file orgnanize program

        Return:
            (void)
    """
    bring_files_to_root(root)
    delete_nested_directory(root)
    for _ , _, filenames in os.walk(root):
        for filename in filenames:
            create_directory(root, filename)
    filter_files(root)


if __name__ == '__main__':
    root = argv[1] if len(argv) > 1 else os.getcwd()
    if clean_path(os.path.split(__file__)[0]) != os.path.abspath(root):
        main(root)
    else:
        print('Cannot run script on the project directory')
