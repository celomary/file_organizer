import os
def  join_path(folder_path: str, filename: str) -> str:
    """function that takes folder and filename and concatenate
    them 

    Args:
        folder_path (str): the folder where the file resides
        filename (str): file to be concatenated with it's directory

    Returns:
        str: full path to the file
    """
    return os.path.join(folder_path, filename)