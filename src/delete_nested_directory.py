import shutil, os
from . import join_path

def delete_nested_directory(root: str) -> None:
    """ it goes through subdirectories in the root direcotry and 
    delete the subdirectories and it's children

    Args:
        root (str): the script starting directory
    """
    for _, dirnames, _ in os.walk(root):
        for dirname in dirnames:
            if dirname.startswith("."):
                continue
            shutil.rmtree( join_path(root, dirname))
        break