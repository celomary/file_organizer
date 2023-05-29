import os, stat
from . import join_path

def create_directory(root:str, filename:str) -> None:
    """function that creates new directory based on the file
     extension or wether it's executable or not

    Args:
        root (str): Location where the directory will be created.
        filename (str): filename that will be used to help us
        name the directory
    """
    _, ext = os.path.splitext(filename)
    if filename.startswith('.'):
        return
    if ext and not os.path.exists(os.path.join(root, ext[1:])):
        os.mkdir( join_path(root, ext[1:]))
    else:
        stat_result = os.stat( join_path(root, filename))
        if stat_result.st_mode & stat.S_IXUSR and stat.S_ISREG:
           not os.path.exists( join_path(root, "executables")) and \
            os.mkdir( join_path(root, "executables"))
        else:
           not os.path.exists( join_path(root, "files")) and \
            os.mkdir( join_path(root, "files"))
