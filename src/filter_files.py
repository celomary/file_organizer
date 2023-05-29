import shutil, stat, os
from . import join_path

def filter_files(root:str)-> None:
    """function used to place each file inside of it's respective
        folder

    Args:
        root (str): script starting point
    """
    for _, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            _, ext = os.path.splitext(filename)
            if ext and os.path.exists( join_path(root, filename)):
                shutil.move( join_path(root, filename),  join_path(root, ext[1:]))
            elif os.path.exists( join_path(root, filename)):
                stat_result = os.stat( join_path(root, filename))
                if stat_result.st_mode & stat.S_IXUSR and stat.S_ISREG:
                    shutil.move( join_path(root, filename),  join_path(root, "executables"))
                else:
                    shutil.move( join_path(root, filename),  join_path(root, "files"))