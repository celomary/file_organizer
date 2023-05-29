import os
from . import join_path

def bring_files_to_root(root: str) -> None:
    """ bring_files_to_root - function that brings files inside
    of the nested directory and place them in the root directory

    Args:
        root (str): the folder to be organized
    """
    for dirpath, _, filenames in os.walk(root):
        if os.path.split(dirpath)[1].startswith('.'):
            continue
        for filename in filenames:
            os.rename( join_path(dirpath, filename), 
                       join_path(root, filename))